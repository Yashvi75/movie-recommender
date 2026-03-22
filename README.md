# Movie Recommendation System

## Overview
This project is a full-stack movie recommendation system that suggests movies based on content similarity. It integrates a machine learning model with a Django web application and displays results with movie posters using the TMDB API.

## Features
- Search movies by name  
- Content-based recommendations  
- Movie posters via TMDB API  
- Fast results using cosine similarity  
- Web interface built with Django  

## Tech Stack
- Backend: Django  
- Machine Learning: Pandas, NumPy, Scikit-learn  
- Frontend: HTML, CSS, Bootstrap  
- API: TMDB  

## How It Works
- Movie data is processed and combined into text features  
- Text is converted into vectors using CountVectorizer  
- Cosine similarity is used to find similar movies  
- Top recommendations are displayed to the user  

## Setup

bash
git clone <your-repo-url>
cd movie-recommender
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Create .env file: TMDB_API_KEY=your_api_key_here

Run the app:
cd webapp
python manage.py runserver

Open: http://127.0.0.1:8000/


Future Improvements
	•	Hybrid recommendation system
	•	User-based personalization
	•	Deployment

Author
Yashvi Rajiv Vyas
