from models import Session, Author, Post, Comment
from datetime import date


def find_author_by_name(name: str) -> Author | None:

    with Session() as session:
        author = session.query(Author).filter(Author.name == name).first()
        return author


def get_posts_by_date(pub_date: date) -> list[Post]:

    with Session() as session:
        posts = (
            session.query(Post)
            .filter(Post.published == True, Post.pub_date == pub_date)
            .all()
        )
        return posts


def add_authors_bulk(authors_data: list[dict]) -> list[Author]:

    with Session() as session:
        authors = [Author(**data) for data in authors_data]
        session.add_all(authors)
        session.commit()
        for a in authors:
            session.refresh(a)
        return authors


def get_post_with_comments(post_id: int) -> dict | None:

    with Session() as session:
        post = session.query(Post).filter(Post.id == post_id).first()
        if post is None:
            return None
        comments = session.query(Comment).filter(Comment.post_id == post_id).all()
        return {
            "post": post,
            "comments": comments,
        }