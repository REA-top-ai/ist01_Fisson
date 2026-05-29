from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///blog.db", echo=False)
Session = sessionmaker(bind=engine)


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)

    posts = relationship("Post", back_populates="author")

    def __repr__(self):
        return f"<Author(id={self.id}, name='{self.name}')>"


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(Text)
    published = Column(Boolean, default=False)
    pub_date = Column(Date)
    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Author", back_populates="posts")
    comments = relationship("Comment", back_populates="post")

    def __repr__(self):
        return f"<Post(id={self.id}, title='{self.title}', published={self.published})>"


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"))

    post = relationship("Post", back_populates="comments")

    def __repr__(self):
        return f"<Comment(id={self.id}, content='{self.content[:30]}...')>"


def init_db():
    Base.metadata.create_all(engine)