import pandas as pd
import numpy as np

movies = pd.read_csv('/Users/yashvivyas/Documents/movie-recommender/data/tmdb_5000_movies.csv')
credits = pd.read_csv('/Users/yashvivyas/Documents/movie-recommender/data/tmdb_5000_credits.csv')

print(movies.head())
print(credits.head())

print(movies.columns)
print(credits.columns)

'''print(movies.shape)
print(credits.shape)

print(movies.isnull().sum())

print(movies['genres'][0])'''