# 🤖 AI Career Recommendation Engine

An AI-powered career recommendation system that recommends suitable career paths based on a user's skills, interests, technologies, experience level, and preferred domain.

This project was developed for the **DecodeLabs Artificial Intelligence Internship – Project 3: AI Recommendation Logic**.

## 🎯 Project Objective

The goal of this project is to build a simple recommendation system based on user preferences.

The system takes user choices and interests, matches them with career profiles using similarity logic, and displays ranked career recommendations.

## ✨ Features

- 👤 User preference input
- 🧠 Similarity-based matching
- 📊 Career match score
- 🏆 Ranked recommendations
- 💡 Recommendation explanations
- 🎨 Interactive Streamlit interface

## 🧮 Recommendation Logic

The user's skills, interests, technologies, experience level, and preferred domain are combined into a profile.

The system uses **TF-IDF Vectorization** and **Cosine Similarity** to compare the user profile with career profiles.

The similarity score is converted into a percentage and careers are ranked from highest to lowest match.

**Match Score = Cosine Similarity × 100**

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- TF-IDF
- Cosine Similarity

## 📊 Dataset

The project contains **20 career profiles** with information about skills, interests, technologies, experience levels, and career domains.

## 📂 Project Structure

- `app.py` — Streamlit web application
- `recommender.py` — Recommendation and similarity logic
- `dataset.csv` — Career dataset
- `requirements.txt` — Project dependencies

## 🎯 Project 3 Requirements

| Requirement | Status |
|---|---|
| User Input | ✅ |
| User Choices / Interests | ✅ |
| Preference Matching | ✅ |
| Similarity Logic | ✅ |
| Recommended Items | ✅ |
| Recommendation Concepts | ✅ |

## 💻 Installation

1. Clone the repository.
2. Open the project folder.
3. Install dependencies using `pip install -r requirements.txt`.
4. Run the application using `streamlit run app.py`.

## 🚀 Future Improvements

- 🎯 Skill-gap analysis
- ⭐ Career rating system
- 📚 Learning resource recommendations
- 📊 Career comparison
- 🤖 Advanced recommendation models
- 🔄 Larger career dataset

## 👩‍💻 Author

**Maria Zafar**

DecodeLabs Artificial Intelligence Internship  
**Project 3 – AI Recommendation Logic**
