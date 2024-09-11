import difflib
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the dataset
data = pd.read_csv("G:/Workspace-ML/MLProjects/MRS/movies_info.csv")

# Required features
Required_features = ['genres', 'keywords', 'title', 'overview', 'cast', 'director', 
                    'popularity', 'production_companies', 'budget', 'release_date', 
                    'revenue', 'runtime', 'original_language']

# Handling null values
data = data[data['genres'].notna()]
for feature in Required_features:
    data[feature] = data[feature].fillna(" ")

# Combine all features into a single string
combined_features = (
    data['genres'] + ' ' +
    data['keywords'] + ' ' +
    data['title'] + ' ' +
    data['overview'] + ' ' +
    data['cast'] + ' ' +
    data['director'] + ' ' +
    data['popularity'].astype(str) + ' ' +
    data['production_companies'] + ' ' +
    data['budget'].astype(str) + ' ' +
    data['release_date'].astype(str) + ' ' +
    data['revenue'].astype(str) + ' ' +
    data['runtime'].astype(str) + ' ' +
    data['original_language'])
# Vectorization
vectorize = TfidfVectorizer()
vectorized_features = vectorize.fit_transform(combined_features)

# Similarity
similarity_list = cosine_similarity(vectorized_features)

# Making movie list
movie_list = data["title"].str.lower().tolist()

def is_valid_input(user_input):
    # Check for non-alphanumeric characters and length
    return len(user_input) >= 3 and user_input.replace(" ", "").isalnum()

user_input = input("Enter a movie :").lower()

if is_valid_input(user_input):
    # Fuzzy matching logic here
    matching = difflib.get_close_matches(user_input, movie_list, n=1, cutoff=0.6)
    if matching:
        closest_match = matching[0]
        print(f"Did you mean: '{closest_match}'?")
        verification = input("Type 'yes' to confirm or 'no' to enter a different title: ").lower()
        
        if verification == 'yes':
            # Getting index of closest match
            movie_index = data[data['title'].str.lower() == closest_match]["index"].values[0]
            
            # Similarity score for all movies
            similarity_score = list(enumerate(similarity_list[movie_index]))
            
            # Sort and get the most similar movies
            sorted_similarities = sorted(similarity_score, key=lambda x: x[1], reverse=True)
            
            # Suggest
            print("Suggestions:\n")
            for x, i in enumerate(sorted_similarities):
                index = i[0]
                title_movie_index = data.iloc[index]["title"]
                if x < 30:  # Limit to the top 30 suggestions
                    print(f"{x + 1}. {title_movie_index}")
        else:
            print("Please try again with a different title.")
    else:
        print("No matches found for the entered movie.")
else:
    print("Invalid input. Please enter a valid movie name.")
