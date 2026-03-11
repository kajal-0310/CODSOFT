import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("movies.csv")

# Convert genre text into vectors
vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(movies["genre"])

# Calculate similarity
similarity = cosine_similarity(genre_matrix)

def recommend(movie_name):
    movie_index = movies[movies["title"] == movie_name].index[0]
    scores = list(enumerate(similarity[movie_index]))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("Recommended Movies:")

    for i in scores[1:4]:
        print(movies.iloc[i[0]]["title"])

movie = input("Enter a movie you like: ")
recommend(movie)