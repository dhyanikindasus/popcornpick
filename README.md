# 🎬 Movie Recommendation System

A smart and scalable Movie Recommendation System built using machine learning techniques to suggest movies based on user preferences. Powered by content-based filtering and collaborative filtering models.

---

## 📽 Project Overview

This project uses real-world movie datasets to build a recommendation engine that suggests similar or personalized movie recommendations to users. It aims to enhance the movie-watching experience by intelligently understanding tastes and preferences.

---

## 🚀 Features

- 🔍 *Content-Based Filtering* (based on movie genres, descriptions, keywords, etc.)
- 🧠 *Collaborative Filtering* (based on user ratings and behavior)
- 📊 Interactive UI for input and movie suggestions
- ⚡ Fast and optimized recommendations using cosine similarity
- 🎉 Deployed with Streamlit for an interactive experience

---

## 📦 Tech Stack

- *Python* (Pandas, NumPy, Scikit-learn)
- *Streamlit* (Frontend)
- *Jupyter Notebook* (Development and Testing)
- *TMDB API* (for movie posters and details)

---

## 🛠 Installation

```bash
# Clone the repo
git clone https://github.com/dhyanikindasus/movie-recommendation-system.git
cd movie-recommendation-system

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt

# Run the app
streamlit run app.py
