import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load career dataset
def load_data():
    return pd.read_csv("dataset.csv")


# Create recommendation engine
def recommend_careers(
    user_skills,
    user_interests,
    user_technologies,
    user_level,
    user_domain,
    top_n=5
):
    df = load_data()

    # Combine career attributes into one text field
    df["profile"] = (
        df["skills"].fillna("") + " " +
        df["interests"].fillna("") + " " +
        df["technologies"].fillna("") + " " +
        df["level"].fillna("") + " " +
        df["domain"].fillna("")
    )

    # Create user profile
    user_profile = (
        ", ".join(user_skills) + " " +
        ", ".join(user_interests) + " " +
        ", ".join(user_technologies) + " " +
        user_level + " " +
        user_domain
    )

    # Convert text into numerical vectors
    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words="english"
    )

    career_vectors = vectorizer.fit_transform(df["profile"])
    user_vector = vectorizer.transform([user_profile])

    # Calculate cosine similarity
    similarity_scores = cosine_similarity(
        user_vector,
        career_vectors
    )[0]

    # Convert similarity into percentage
    df["match_score"] = similarity_scores * 100

    # Sort highest match first
    recommendations = df.sort_values(
        by="match_score",
        ascending=False
    ).head(top_n)

    return recommendations