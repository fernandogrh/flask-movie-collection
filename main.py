from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FloatField
from wtforms.validators import DataRequired, Length
import requests
import os
from dotenv import load_dotenv

load_dotenv()
tmdb_url = "https://api.themoviedb.org/3/search/movie"
get_movie_details = "https://api.themoviedb.org/3/movie/{movie_id}"
movie_db_image_url = "https://image.tmdb.org/t/p/w500"
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
bootstrap = Bootstrap5(app)

class EditForm(FlaskForm):
    rating = FloatField("Your rating out of 10 e.g. 7.5", validators=[DataRequired()])
    review = TextAreaField("Your review", validators=[DataRequired()])
    done = SubmitField("Done")

class AddMovieForm(FlaskForm):
    movie_title = StringField('Movie Title', validators=[DataRequired(), Length(min=2, max=100)])
    submit = SubmitField('Add Movie')

class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars().all()
    for i, movie in enumerate(all_movies):
        movie.ranking = i + 1
    db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route("/edit/<int:movie_id>/<title>", methods = ["GET", "POST"])
def edit(movie_id, title):
    edit_form = EditForm()
    movie = db.get_or_404(Movie, movie_id)
    if edit_form.validate_on_submit():
        movie.rating = float(edit_form.rating.data)
        movie.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form = edit_form, title=title)

@app.route("/delete/<int:movie_id>", methods = ["GET", "POST"])
def delete(movie_id):
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddMovieForm()
    if add_form.validate_on_submit():
        return redirect(url_for("select", movie_name=add_form.movie_title.data))
    return render_template("add.html", add_form=add_form)

@app.route("/select/<movie_name>", methods=["GET", "POST"])
def select(movie_name):
    similar_results = requests.get(tmdb_url, params={"api_key": TMDB_API_KEY, "query": movie_name}).json()["results"]
    return render_template("select.html", movie=movie_name, results=similar_results)

@app.route("/movie/<movie_id>", methods=["GET", "POST"])
def add_movie(movie_id):
    movie_details = requests.get(get_movie_details.format(movie_id=movie_id), params={"api_key": TMDB_API_KEY}).json()
    existing_movie = db.session.execute(db.select(Movie).where(Movie.title == movie_details["original_title"])).scalar()
    if existing_movie:
        return redirect(url_for("home"))
    movie_to_add = Movie(
        title=movie_details["original_title"],
        year=int(movie_details["release_date"].split("-")[0]),
        description=movie_details["overview"],
        img_url=f'{movie_db_image_url}{movie_details["poster_path"]}'
    )
    db.session.add(movie_to_add)
    db.session.commit()
    return redirect(url_for("edit", movie_id=movie_to_add.id, title=movie_details["original_title"]))

if __name__ == '__main__':
    app.run(debug=True)