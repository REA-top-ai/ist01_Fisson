import os
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import create_engine
from movie_picker import (
    detect_genre, get_movies_from_api, pick_random_movie,
    GENRE_LABELS, save_movie_to_db, init_db,
    create_user, get_user_by_email, get_user_by_id, get_user_history
)

app = Flask(__name__)
app.secret_key = "film_secret_key_2024"

# БД всегда рядом с app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH  = os.path.join(BASE_DIR, "movies.db")

print(f"[DB] База данных: {DB_PATH}")  # покажет путь в терминале

engine = create_engine(f"sqlite:///{DB_PATH}", echo=False)
init_db(engine)



# ГЛАВНАЯ СТРАНИЦА — подбор фильма

@app.route("/", methods=["GET", "POST"])
def index():
    # Если не вошёл - отправляем на логин
    if "user_id" not in session:
        return redirect(url_for("login"))

    user = get_user_by_id(engine, session["user_id"])
    # Если пользователь не найден в БД - сбрасываем
    if user is None:
        session.pop("user_id", None)
        return redirect(url_for("login"))
    movie = None
    genre_label = None
    user_query = ""
    saved_id = None

    if request.method == "POST":
        user_query = request.form.get("query", "").strip()
        if user_query:
            genre = detect_genre(user_query)
            genre_label = GENRE_LABELS.get(genre, genre)
            movies = get_movies_from_api(genre)
            movie = pick_random_movie(movies)
            saved = save_movie_to_db(engine, movie, user_id=session["user_id"])
            saved_id = saved.id

    history = get_user_history(engine, session["user_id"])

    return render_template(
        "index.html",
        movie=movie,
        genre_label=genre_label,
        user_query=user_query,
        saved_id=saved_id,
        username=user.username,
        history=history,
    )



# РЕГИСТРАЦИЯ

@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email    = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        if not username or not email or not password:
            error = "Заполните все поля."
        elif get_user_by_email(engine, email):
            error = "Этот email уже зарегистрирован."
        else:
            password_hash = generate_password_hash(password)
            user = create_user(engine, username, email, password_hash)
            session["user_id"] = user.id
            return redirect(url_for("index"))

    return render_template("register.html", error=error)



# ВХОД

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        email    = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()
        user     = get_user_by_email(engine, email)

        if not user or not check_password_hash(user.password_hash, password):
            error = "Неверный email или пароль."
        else:
            session["user_id"] = user.id
            return redirect(url_for("index"))

    return render_template("login.html", error=error)



# ВЫХОД

@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)