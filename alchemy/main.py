from datetime import date
from models import Session, Author, Post, Comment, init_db
from crud import find_author_by_name, get_posts_by_date, add_authors_bulk, get_post_with_comments


def seed_db():

    with Session() as session:

        a1 = Author(name="Анна Смирнова", email="anna@mail.ru")
        a2 = Author(name="Пётр Иванов", email="petr@mail.ru")
        session.add_all([a1, a2])
        session.flush()


        p1 = Post(
            title="Введение в SQLAlchemy",
            content="SQLAlchemy — мощный ORM для Python.",
            published=True,
            pub_date=date(2024, 5, 10),
            author_id=a1.id,
        )
        p2 = Post(
            title="Работа с сессиями",
            content="Сессии управляют транзакциями.",
            published=True,
            pub_date=date(2024, 5, 10),
            author_id=a2.id,
        )
        p3 = Post(
            title="Черновик",
            content="Этот пост не опубликован.",
            published=False,
            pub_date=date(2024, 5, 10),
            author_id=a1.id,
        )
        session.add_all([p1, p2, p3])
        session.flush()


        c1 = Comment(content="Отличная статья!", post_id=p1.id)
        c2 = Comment(content="Спасибо, очень помогло.", post_id=p1.id)
        c3 = Comment(content="Жду продолжения.", post_id=p2.id)
        session.add_all([c1, c2, c3])
        session.commit()
        print("✓ База данных заполнена тестовыми данными.\n")


def test_find_author_by_name():
    print("=== Тест 1: find_author_by_name ===")
    author = find_author_by_name("Анна Смирнова")
    if author:
        print(f"Найден автор: {author}")
    else:
        print("Автор не найден.")

    missing = find_author_by_name("Не существует")
    print(f"Несуществующий автор: {missing}\n")


def test_get_posts_by_date():
    print("=== Тест 2: get_posts_by_date ===")
    posts = get_posts_by_date(date(2024, 5, 10))
    print(f"Опубликованные посты за 2024-05-10 ({len(posts)} шт.):")
    for p in posts:
        print(f"  {p}")
    print()


def test_add_authors_bulk():
    print("=== Тест 3: add_authors_bulk ===")
    new_authors = [
        {"name": "Мария Козлова", "email": "maria@mail.ru"},
        {"name": "Сергей Новиков", "email": "sergey@mail.ru"},
        {"name": "Елена Фёдорова", "email": "elena@mail.ru"},
    ]
    added = add_authors_bulk(new_authors)
    print(f"Добавлено авторов: {len(added)}")
    for a in added:
        print(f"  {a}")
    print()


def test_get_post_with_comments():
    print("=== Тест 4: get_post_with_comments ===")
    result = get_post_with_comments(1)
    if result:
        print(f"Пост: {result['post']}")
        print(f"Комментарии ({len(result['comments'])} шт.):")
        for c in result["comments"]:
            print(f"  {c}")
    else:
        print("Пост не найден.")

    result_missing = get_post_with_comments(999)
    print(f"\nПост с id=999: {result_missing}\n")


if __name__ == "__main__":
    init_db()
    seed_db()

    test_find_author_by_name()
    test_get_posts_by_date()
    test_add_authors_bulk()
    test_get_post_with_comments()