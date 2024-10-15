# Ml powered Movie Recommendation System 🎬

A Machine Learning-based movie recommendation system that suggests movies based on user preferences such as genres, keywords, cast, director, and more. This project is built using **Flask** for the web application framework and various **ML algorithms** to recommend movies. 

---

### Try It Out on Colab

If you'd like to experiment with the recommendation system without setting it up locally, you can use this [Google Colab Notebook]([https://colab.research.google.com/your-colab-link-here](https://colab.research.google.com/drive/1pG2efa89l1aoJYm6VPVV9-4FVWwuAmFk?usp=sharing)) to try it out directly in your browser.

---

## Table of Contents
1. Project Overview
2. Features
3. Folder Structure
4. Tech Stack
5. How It Works
6. Setup Instructions
7. Memory Limitations
8. Screenshots
9. Demo Video
10. Future Improvements

---

## Project Overview

The **Movie Recommendation System** allows users to input their preferences (like genres, keywords, actors, or directors), and based on those preferences, it generates a list of recommended movies. The recommendation algorithm uses content-based filtering to suggest movies similar to the user’s input.

Due to high memory requirements, this project cannot be deployed on free platforms, but it can be run locally. Below are detailed instructions on how to set up and run the project.

---

## Features

- Input preferences such as genres, keywords, cast, directors, etc.
- Movie recommendations based on content similarity using **machine learning algorithms**.
- User-friendly web interface built with **Flask**.
- Customizable recommendation logic.
- Data-driven recommendations using metadata such as popularity, budget, etc.

---

## Folder Structure

Here’s an overview of the project structure:

```
├── app/
│   ├── static/                # CSS, JavaScript, and images
│   ├── templates/             # HTML templates for Flask
│   ├── __init__.py            # Initializes the Flask app
│   ├── routes.py              # Defines Flask routes (URLs)
│   ├── recommendation.py      # Contains the recommendation logic (ML algorithms)
│   └── models/                # Stores ML models and data
├── data/
│   ├── movies_metadata.csv     # The movie dataset (metadata)
│   ├── links.csv               # Links to movie information (IMDB, TMDB)
│   └── ratings.csv             # User ratings data
├── screenshots/               # Screenshots of the app running
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── run.py                     # Main script to start the Flask app
```

### Key Files:
- **`app/__init__.py`**: Initializes the Flask app and configures routes.
- **`app/routes.py`**: Contains the route definitions for user inputs and displaying recommendations.
- **`app/recommendation.py`**: The core logic for making movie recommendations based on user inputs.
- **`templates/`**: Contains HTML files for rendering the web pages.
- **`static/`**: Stores static assets like CSS files and images for the web interface.
- **`data/`**: Stores the movie metadata and ratings used for training and recommendations.

---

## Tech Stack

- **Backend**: Flask (Python)
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Frontend**: HTML, CSS, Bootstrap (via Flask templates)
- **Database**: CSV files for the movie dataset
- **Tools**: Jupyter Notebook (for data preprocessing and ML training)

---

## How It Works

1. **User Input**: The user selects their preferences like genres, keywords, cast, and directors.
2. **Recommendation Algorithm**:
   - The system uses **content-based filtering** to match the input data to similar movies in the dataset.
   - Movies are ranked based on similarity, using metadata like genres, keywords, and popularity.
3. **Movie Suggestions**: The system returns a list of recommended movies based on the preferences.

---

## Setup Instructions

### Prerequisites

- **Python 3.8+** installed on your local machine.
- Basic understanding of Python, Flask, and Machine Learning.

### Steps to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/movie-recommendation-system.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd movie-recommendation-system
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app**:
   ```bash
   python run.py
   ```

5. **Access the web application**:
   Open your browser and go to `http://127.0.0.1:5000/`.

6. **Input Preferences**:
   Use the web interface to enter your movie preferences, and the system will display recommended movies.

---

## Memory Limitations

This project requires more memory than most free hosting platforms (like Heroku or Render) can provide. The large movie dataset and the recommendation algorithm's memory usage make it impractical for free-tier deployments.

### Workaround:
- Run the application **locally** on your machine.
- You can showcase the app using a **video walkthrough** (see [Demo Video](#demo-video)).

---

## Screenshots

Below are some screenshots of the app running locally:

1. **Home Page**:
   ![Home Page](./screenshots/home_page.png)

2. **Recommendation Results**:
   ![Recommendations](./screenshots/recommendations.png)

---

## Demo Video

Since deploying this project is memory-intensive, here’s a [video demo](https://youtu.be/demo-link) showing the app in action. You can watch the entire process from user input to movie recommendations.

---

## Future Improvements

- **Model Optimization**: Reduce memory usage to enable deployment on cloud platforms.
- **Collaborative Filtering**: Add user-based collaborative filtering to improve recommendations by considering user ratings.
- **Scalability**: Deploy the system on a paid cloud platform with higher memory resources (e.g., AWS, Google Cloud).
- **Improved UI**: Make the user interface more interactive with advanced filtering options.

---

## Conclusion

This **Movie Recommendation System** is a powerful tool that demonstrates the integration of machine learning and web development to create personalized movie recommendations. Despite deployment limitations, the project can be run locally and showcases your ability to work with real-world datasets and build a complete web application.

Feel free to explore the code, run it locally, and check out the demo video!

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

This README provides a comprehensive overview of your project, making it easy for others to understand your work, run it locally, and view it in action through a video or screenshots.
