# 🎬 Movie Collection App

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web_App-000000?logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00)
![WTForms](https://img.shields.io/badge/WTForms-Forms_Framework-3C6E71)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?logo=bootstrap&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-HTTP_Client-2B5B84)
![TMDB API](https://img.shields.io/badge/API-TMDB-01D277)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite&logoColor=white)

### A Flask web application that allows users to search for movies using the TMDB API, add them to a personal collection, rate them, and automatically rank them.



### This project demonstrates backend development with Flask, database management with SQLAlchemy, form handling with WTForms, and integration with an external API.

## 🚀 Features
- Search movies using TMDB API

- Add movies to a personal collection

- Edit ratings and reviews

- Automatically rank movies by rating

- Delete movies from the collection

- Clean UI using Bootstrap

- Environment variable management with python-dotenv

## 🛠 Tech Stack
- Python

- Flask

- Flask-SQLAlchemy

- Flask-WTF

- Bootstrap-Flask

- TMDB API

- SQLite

## 📦 Installation

Clone the repository:

    git clone https://github.com/fernandogrh/flask-movie-application.git
    cd flask-movie-application

Create a virtual environment:

    python -m venv .venv

Activate it:

**Mac/Linux**

    source .venv/bin/activate

**Windows**

    .venv\Scripts\activate

Install dependencies:

    pip install -r requirements.txt



## 🔑 Environment Variables

Create a .env file in the project root:
    
    TMDB_API_KEY=your_tmdb_api_key_here
    SECRET_KEY=your_flask_secret_key_here

You can obtain a free API key from:

https://www.themoviedb.org/

## ▶️ Run the Application

Start the Flask server:

    python main.py

Open your browser and go to:

    http://127.0.0.1:5000

## 🗄 Database

The application automatically creates a SQLite database:

    movies.db

It stores:

- movie title

- release year

- description

- rating

- ranking

- review

- poster image

## 📚 API Attribution

This product uses the TMDB API but is not endorsed or certified by TMDB.

https://www.themoviedb.org/

## 👨‍💻 Author

Built by **Fernando Ramirez**

