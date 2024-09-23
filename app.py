from flask import Flask, render_template, request
import time
import difflib
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

class Movie_Recomendation_System:

    def __init__(self):
        # Load dataset
        self.data = pd.read_csv("/static/datasets/movies_info.csv")
        
        # Required features for movie recommendation
        self.Required_features = ['genres', 'keywords', 'title', 'overview', 'cast', 'director', 
                                 'popularity', 'production_companies', 'budget', 'release_date', 
                                 'revenue', 'runtime', 'original_language']

        # Fill missing values
        self.data = self.data[self.data['genres'].notna()]
        for feature in self.Required_features:
            self.data[feature] = self.data[feature].fillna(" ")

        # Combine all the features into a single string
        self.data['combined_features'] = (
            self.data['genres'] + ' ' +
            self.data['keywords'] + ' ' +
            self.data['title'] + ' ' +
            self.data['overview'] + ' ' +
            self.data['cast'] + ' ' +
            self.data['director'] + ' ' +
            self.data['popularity'].astype(str) + ' ' +
            self.data['production_companies'] + ' ' +
            self.data['budget'].astype(str) + ' ' +
            self.data['release_date'].astype(str) + ' ' +
            self.data['revenue'].astype(str) + ' ' +
            self.data['runtime'].astype(str) + ' ' +
            self.data['original_language']
        )

        # Vectorize combined features
        self.vectorizer = TfidfVectorizer()
        self.vectorized_features = self.vectorizer.fit_transform(self.data['combined_features'])

        # Cosine similarity
        self.similarity_list = cosine_similarity(self.vectorized_features)

        # Movie list
        self.movie_list = self.data["title"].str.lower().tolist()
    
    def is_valid_input(self, user_input):
        return len(user_input) >= 3 and user_input.replace(" ", "").isalnum()

    def get_movie_recommendations(self, user_input):
        user_input = user_input.lower()

        if self.is_valid_input(user_input):
            matching = difflib.get_close_matches(user_input, self.movie_list, n=1, cutoff=0.6)
            if matching:
                closest_match = matching[0]
                return f"Did you mean: '{closest_match}' ?", closest_match
            else:
                return "No matches found for the entered movie.", None
        else:
            return "Invalid input. Please enter a valid movie name.", None

    def suggest_movies(self, closest_match):
        movie_index = self.data[self.data['title'].str.lower() == closest_match]["index"].values[0]
        similarity_score = list(enumerate(self.similarity_list[movie_index]))
        sorted_similarities = sorted(similarity_score, key=lambda x: x[1], reverse=True)

        recommendations = []
        for x, i in enumerate(sorted_similarities):
            index = i[0]
            title_movie_index = self.data.iloc[index]["title"]
            if x < 30:  # Top 30 recommendations
                # recommendations.append(f"{x + 1}. {title_movie_index}")
                recommendations.append(f"{title_movie_index}")
        return recommendations


# Initialize movie recommendation system
mrs = Movie_Recomendation_System()

@app.route('/', methods=['GET', 'POST'])
def index():
    movie = None
    message = None
    recommendations = []
    closest_match = None
    show_buttons = False

    if request.method == 'POST':
        if 'movie' in request.form:  # Initial movie search
            movie = request.form['movie']
            message, closest_match = mrs.get_movie_recommendations(movie)
            show_buttons = closest_match is not None
        elif 'response' in request.form:  # Handle Yes/No response
            response = request.form['response']
            closest_match = request.form['closest_match']
            if response == 'yes':
                time.sleep(0.5)
                recommendations = mrs.suggest_movies(closest_match)
            else:
                message = "Please try again with a different title."

    return render_template('index.html', movie=movie, message=message, 
                           recommendations=recommendations, closest_match=closest_match, 
                           show_buttons=show_buttons)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
