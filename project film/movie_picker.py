import random
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Session, relationship



# ШАБЛОН ОТВЕТА TasteDive API (структура из docs)

MOCK_API_RESPONSE = {
    "Similar": {
        "Info": [{"Name": "Movies", "Type": "movie"}],
        "Results": [
            # комедия
            {
                "Name": "The Grand Budapest Hotel",
                "Type": "movie",
                "wTeaser": (
                    "Консьерж знаменитого европейского отеля оказывается втянут "
                    "в кражу бесценной картины и семейную борьбу за наследство."
                ),
                "wUrl": "https://en.wikipedia.org/wiki/The_Grand_Budapest_Hotel",
                "genre": "Comedy",
                "rating": 8.1,
            },
            {
                "Name": "Superbad",
                "Type": "movie",
                "wTeaser": (
                    "Два неразлучных старшеклассника пытаются раздобыть алкоголь "
                    "для вечеринки, но всё идёт совсем не по плану."
                ),
                "wUrl": "https://en.wikipedia.org/wiki/Superbad",
                "genre": "Comedy",
                "rating": 7.6,
            },
            {
                "Name": "Game Night",
                "Type": "movie",
                "wTeaser": (
                    "Компания друзей на вечере игр неожиданно оказывается "
                    "втянута в настоящее криминальное расследование."
                ),
                "wUrl": "https://en.wikipedia.org/wiki/Game_Night_(film)",
                "genre": "Comedy",
                "rating": 7.0,
            },
            {
                "Name": "Knives Out",
                "Type": "movie",
                "wTeaser": (
                    "Детектив расследует смерть патриарха эксцентричной семьи. "
                    "Изящный детектив с элементами чёрной комедии."
                ),
                "wUrl": "https://en.wikipedia.org/wiki/Knives_Out",
                "genre": "Comedy",
                "rating": 7.9,
            },
            {
                "Name": "About Time",
                "Type": "movie",
                "wTeaser": (
                    "В 21 год Тим узнаёт, что мужчины в его семье умеют "
                    "путешествовать во времени. Он использует этот дар, "
                    "чтобы найти любовь и стать счастливее."
                ),
                "wUrl": "https://en.wikipedia.org/wiki/About_Time_(film)",
                "genre": "Comedy",
                "rating": 7.8,
            },
            # ужасы
            {
                "Name": "Hereditary",
                "Type": "movie",
                "wTeaser": (
                    "После смерти бабушки семья Грэм начинает вскрывать "
                    "тёмные семейные тайны. Атмосферный хоррор о наследии зла."
                ),
                "wUrl": "https://en.wikipedia.org/wiki/Hereditary_(film)",
                "genre": "Horror",
                "rating": 7.3,
            },
            {
                "Name": "Get Out",
                "Type": "movie",
                "wTeaser": (
                    "Молодой афроамериканец едет знакомиться с семьёй своей "
                    "девушки и постепенно понимает, что попал в ловушку."
                ),
                "wUrl": "https://en.wikipedia.org/wiki/Get_Out",
                "genre": "Horror",
                "rating": 7.7,
            },
            {
                "Name": "A Quiet Place",
                "Type": "movie",
                "wTeaser": (
                    "Семья живёт в тишине, потому что слепые монстры охотятся "
                    "на звук. Любой шум может стать последним."
                ),
                "wUrl": "https://en.wikipedia.org/wiki/A_Quiet_Place",
                "genre": "Horror",
                "rating": 7.5,
            },
            {
                "Name": "Midsommar",
                "Type": "movie",
                "wTeaser": (
                    "Пара отправляется на летний фестиваль в Швецию, "
                    "который оказывается жутким языческим ритуалом."
                ),
                "wUrl": "https://en.wikipedia.org/wiki/Midsommar",
                "genre": "Horror",
                "rating": 7.1,
            },
            #  боевики
            {
                "Name": "The Dark Knight",
                "Type": "movie",
                "wTeaser": (
                    "Бэтмен противостоит Джокеру — хаотичному злодею, "
                    "который сеет анархию в Готэм-сити."
                ),
                "wUrl": "https://en.wikipedia.org/wiki/The_Dark_Knight",
                "genre": "Action",
                "rating": 9.0,
            },
            {
                "Name": "Mad Max: Fury Road",
                "Type": "movie",
                "wTeaser": (
                    "В постапокалиптической пустыне Макс и Фуриоса пытаются "
                    "вырваться из лап безумного тирана. Непрерывный экшн."
                ),
                "wUrl": "https://en.wikipedia.org/wiki/Mad_Max:_Fury_Road",
                "genre": "Action",
                "rating": 8.1,
            },
            {
                "Name": "John Wick",
                "Type": "movie",
                "wTeaser": (
                    "Бывший наёмный убийца возвращается к прошлому, когда "
                    "сын русского гангстера убивает его собаку."
                ),
                "wUrl": "https://en.wikipedia.org/wiki/John_Wick",
                "genre": "Action",
                "rating": 7.4,
            },
            {
                "Name": "Top Gun: Maverick",
                "Type": "movie",
                "wTeaser": (
                    "Легендарный пилот Мэверик тренирует новое поколение "
                    "лётчиков для опасной секретной миссии."
                ),
                "wUrl": "https://en.wikipedia.org/wiki/Top_Gun:_Maverick",
                "genre": "Action",
                "rating": 8.3,
            },
            #  Drama
            {
                "Name": "The Shawshank Redemption",
                "Type": "movie",
                "wTeaser": (
                    "Банкир, осуждённый за убийство, находит смысл жизни "
                    "и дружбу в жестоких условиях тюрьмы Шоушенк."
                ),
                "wUrl": "https://en.wikipedia.org/wiki/The_Shawshank_Redemption",
                "genre": "Drama",
                "rating": 9.3,
            },
            {
                "Name": "Forrest Gump",
                "Type": "movie",
                "wTeaser": (
                    "Жизнь простодушного Форреста Гампа случайно пересекается "
                    "с ключевыми событиями американской истории."
                ),
                "wUrl": "https://en.wikipedia.org/wiki/Forrest_Gump",
                "genre": "Drama",
                "rating": 8.8,
            },
            {
                "Name": "Parasite",
                "Type": "movie",
                "wTeaser": (
                    "Бедная семья постепенно проникает в жизнь богатой, "
                    "пока всё не заканчивается непредвиденной катастрофой."
                ),
                "wUrl": "https://en.wikipedia.org/wiki/Parasite_(2019_film)",
                "genre": "Drama",
                "rating": 8.5,
            },
            # драма
            {
                "Name": "La La Land",
                "Type": "movie",
                "wTeaser": (
                    "Джазовый музыкант и начинающая актриса встречаются "
                    "в Лос-Анджелесе и влюбляются, преследуя свои мечты."
                ),
                "wUrl": "https://en.wikipedia.org/wiki/La_La_Land",
                "genre": "Romance",
                "rating": 8.0,
            },
            {
                "Name": "Notting Hill",
                "Type": "movie",
                "wTeaser": (
                    "Скромный владелец книжного магазина в Лондоне случайно "
                    "влюбляется в самую знаменитую актрису мира."
                ),
                "wUrl": "https://en.wikipedia.org/wiki/Notting_Hill_(film)",
                "genre": "Romance",
                "rating": 7.1,
            },
            {
                "Name": "The Notebook",
                "Type": "movie",
                "wTeaser": (
                    "История любви бедного юноши и богатой девушки, "
                    "разлучённых семьёй и войной, но не забывших друг друга."
                ),
                "wUrl": "https://en.wikipedia.org/wiki/The_Notebook",
                "genre": "Romance",
                "rating": 7.8,
            },
        ],
    }
}



# ЖАНРЫ И МЕТКИ

GENRES = {
    "1": "Comedy",
    "2": "Horror",
    "3": "Action",
    "4": "Drama",
    "5": "Romance",
}

GENRE_LABELS = {
    "Comedy":  " Комедия",
    "Horror":  " Ужасы",
    "Action":  " Боевик",
    "Drama":   " Драма",
    "Romance": " Романтика",
}



# SQLALCHEMY: МОДЕЛИ

class Base(DeclarativeBase):
    pass


class User(Base):
    """Модель пользователя."""
    __tablename__ = "users"

    id            = Column(Integer, primary_key=True, autoincrement=True)
    username      = Column(String(100), nullable=False, unique=True)
    email         = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)

    movies = relationship("Movie", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"


class Movie(Base):
    """ORM-модель таблицы movies."""
    __tablename__ = "movies"

    id          = Column(Integer, primary_key=True, autoincrement=True)
    title       = Column(String(255), nullable=False)
    genre       = Column(String(100), nullable=False)
    rating      = Column(Float, nullable=True)
    description = Column(String(1000), nullable=True)
    user_id     = Column(Integer, ForeignKey("users.id"), nullable=True)

    user = relationship("User", back_populates="movies")

    def __repr__(self):
        return f"<Movie(id={self.id}, title='{self.title}', genre='{self.genre}')>"


def init_db(engine) -> None:
    """Создаёт таблицы если их нет."""
    Base.metadata.create_all(engine)



# ФУНКЦИИ ДЛЯ РАБОТЫ С ПОЛЬЗОВАТЕЛЯМИ

def create_user(engine, username: str, email: str, password_hash: str) -> User:
    """Создаёт нового пользователя в БД."""
    new_user = User(username=username, email=email, password_hash=password_hash)
    with Session(engine) as session:
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user


def get_user_by_email(engine, email: str) -> User | None:
    """Ищет пользователя по email."""
    with Session(engine) as session:
        return session.query(User).filter_by(email=email).first()


def get_user_by_id(engine, user_id: int) -> User | None:
    """Ищет пользователя по id."""
    with Session(engine) as session:
        return session.query(User).filter_by(id=user_id).first()



# ФУНКЦИИ ДЛЯ РАБОТЫ С ФИЛЬМАМИ

def detect_genre(user_query: str) -> str:
    """Определяет жанр - сначала проверяет номер меню, потом ключевые слова."""
    if user_query in GENRES:
        return GENRES[user_query]

    query = user_query.lower()
    genre_map = {
        "Romance": ["романтик", "романтич", "romance", "любовь", "свидание", "чувства", "влюб"],
        "Horror":  ["ужас", "horror", "страшн", "триллер", "пугать", "мистика", "монстр"],
        "Action":  ["экшн", "action", "боевик", "драки", "взрывы", "приключен", "динамик"],
        "Drama":   ["драма", "drama", "артхаус", "глубокий", "серьёзн", "трогател", "плакать"],
        "Comedy":  ["комедия", "comedy", "смешн", "смеяться", "юмор", "вечер", "пошутить"],
    }
    for genre, keywords in genre_map.items():
        if any(kw in query for kw in keywords):
            return genre
    return "Comedy"


def get_movies_from_api(genre: str) -> list[dict]:
    """Фильтрует фильмы по жанру из mock-данных."""
    all_results = MOCK_API_RESPONSE["Similar"]["Results"]
    return [m for m in all_results if m.get("genre", "").lower() == genre.lower()]


def pick_random_movie(movies: list[dict]) -> dict:
    """Случайный выбор одного фильма"""
    if not movies:
        raise ValueError("Список фильмов пуст.")
    return random.choice(movies)


def save_movie_to_db(engine, movie_data: dict, user_id: int = None) -> Movie:
    """Сохраняет выбранный фильм в БД, привязывая к пользователю"""
    new_movie = Movie(
        title=movie_data["Name"],
        genre=movie_data.get("genre", "Unknown"),
        rating=movie_data.get("rating"),
        description=movie_data.get("wTeaser"),
        user_id=user_id,
    )
    with Session(engine) as session:
        session.add(new_movie)
        session.commit()
        session.refresh(new_movie)
        return new_movie


def get_user_history(engine, user_id: int) -> list:
    """Возвращает историю фильмов конкретного пользователя."""
    with Session(engine) as session:
        movies = session.query(Movie).filter_by(user_id=user_id).all()
        session.expunge_all()
        return movies