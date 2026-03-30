# 🎬 Movie Collection App

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web_App-000000?logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00)
![TMDB API](https://img.shields.io/badge/API-TMDB-01D277)

### A full-stack Flask web application that allows users to search movies via the TMDB API, build a personal collection, rate them, and automatically rank them.
This project demonstrates real-world backend development with Flask, database management with SQLAlchemy, form handling with WTForms, and integration with an external API.

## 🚀 Features
- Search movies using TMDB API

- Add movies to a personal collection

- Edit ratings and reviews

- Automatically rank movies by rating

- Delete movies from the collection

- Clean UI using Bootstrap

- Environment variable management with python-dotenv

## ⚙️ How It Works

1. User searches for a movie

2. App fetches results from TMDB API

3. User selects a movie

4. Movie is stored in SQLite database

5. User adds rating & review

6. Movies are ranked dynamically

## 🛠 Tech Stack
- Python

- Flask

- Flask-SQLAlchemy

- Flask-WTF

- Bootstrap-Flask

- TMDB API

- SQLite

- python-dotenv

## 📁 Project Structure

    movie-collection/
    │
    ├── main.py
    ├── requirements.txt
    ├── README.md
    ├── .env.example
    ├── .gitignore
    │
    ├── templates/
    │  ├── index.html
    │  ├── edit.html
    │  ├── add.html
    │  ├── base.html
    │  └── select.html
    │
    └── static/
       └── css/


## 📦 Installation

Clone the repository:

    git clone https://github.com/fernandogrh/flask-movie-collection.git
    cd flask-movie-collection

Create a virtual environment:

    python -m venv .venv

Activate it:

**Mac/Linux**

    source .venv/bin/activate

**Windows**

    .venv\Scripts\activate

Install dependencies:

    pip install -r requirements.txt



## 🔑 Environment Setup

Copy `.env.example` and rename it to `.env`.

Add your credentials: 
    
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

> ️️️️️️⚠️ The database file is not included in the repository.
> It will be automatically created when the application runs.

## ⚠️ Notes
- TMDB API responses are validated to prevent crashes
- Network errors are handled gracefully
- Duplicate movies are prevented

## 📚 API Attribution

This product uses the TMDB API but is not endorsed or certified by TMDB.

https://www.themoviedb.org/

## 👨‍💻 Author

Built by **Fernando Ramirez**

