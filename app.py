import streamlit as st
from recommender import recommend_careers


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Career Recommender",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>
.stApp {
background: linear-gradient(135deg, #fdf2f8, #eef2ff, #ecfeff);
}
.hero {
padding: 35px 40px;
border-radius: 20px;
background: linear-gradient(135deg, #7c3aed, #db2777, #2563eb);
color: white;
margin-bottom: 30px;
box-shadow: 0 10px 25px rgba(124,58,237,0.25);
}
.hero h1 {
font-size: 42px;
margin-bottom: 8px;
font-weight: 800;
}
.hero p {
font-size: 18px;
color: #f3e8ff;
margin-bottom: 0;
}
.section-title {
font-size: 26px;
font-weight: 800;
margin-top: 15px;
margin-bottom: 15px;
color: #4c1d95;
}
.career-card {
background: white;
padding: 25px;
border-radius: 18px;
margin-bottom: 20px;
border: 1px solid #e5e7eb;
box-shadow: 0 5px 18px rgba(124,58,237,0.10);
border-left: 6px solid #db2777;
}
.career-title {
font-size: 24px;
font-weight: 800;
color: #4c1d95;
}
.match-score {
font-size: 30px;
font-weight: 800;
color: #db2777;
}
.badge {
display: inline-block;
padding: 6px 12px;
border-radius: 20px;
background: linear-gradient(135deg, #ede9fe, #fce7f3);
color: #7c3aed;
font-size: 13px;
font-weight: 700;
margin-right: 5px;
margin-top: 8px;
}
.why {
background: #faf5ff;
padding: 15px;
border-radius: 12px;
margin-top: 15px;
color: #374151;
border: 1px dashed #d8b4fe;
}
.stButton > button {
width: 100%;
border-radius: 12px;
height: 48px;
font-size: 17px;
font-weight: 700;
background: linear-gradient(135deg, #7c3aed, #db2777);
color: white;
border: none;
}
section[data-testid="stSidebar"] {
background: #ffffff;
}
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

st.markdown("""
<div class="hero">
<h1>🤖 AI Career Recommender</h1>
<p>Discover career paths that match your skills, interests and technology preferences.</p>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown("## 👤 Build Your Profile")

    st.write(
        "Tell us about your skills and interests "
        "to receive personalized career recommendations."
    )

    st.divider()

    skills = st.multiselect(
        "💻 Your Skills",
        [
            "Python",
            "SQL",
            "Machine Learning",
            "Deep Learning",
            "Data Analysis",
            "Statistics",
            "Programming",
            "Problem Solving",
            "Algorithms",
            "Networking",
            "Linux",
            "Databases",
            "Communication",
            "Leadership",
            "Design",
            "Creativity",
            "Research",
            "Writing"
        ]
    )

    interests = st.multiselect(
        "🎯 Your Interests",
        [
            "Artificial Intelligence",
            "Automation",
            "Research",
            "Data",
            "Analytics",
            "Big Data",
            "Software",
            "Technology",
            "Development",
            "Cybersecurity",
            "Ethical Hacking",
            "Cloud",
            "Infrastructure",
            "Robotics",
            "Business",
            "Design",
            "User Experience",
            "Mobile Apps"
        ]
    )

    technologies = st.multiselect(
        "🛠️ Technologies You Like",
        [
            "Python",
            "Scikit-learn",
            "TensorFlow",
            "PyTorch",
            "Pandas",
            "SQL",
            "Power BI",
            "Excel",
            "AWS",
            "Docker",
            "Kubernetes",
            "Git",
            "OpenCV",
            "React",
            "Figma",
            "Flutter",
            "Linux"
        ]
    )

    level = st.selectbox(
        "📊 Experience Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    domain = st.selectbox(
        "🌐 Preferred Domain",
        [
            "Artificial Intelligence",
            "Data Science",
            "Data Analytics",
            "Software Development",
            "Cybersecurity",
            "Cloud Computing",
            "DevOps",
            "Web Development",
            "Design",
            "Robotics",
            "Business Intelligence",
            "Product Management"
        ]
    )

    st.divider()

    get_recommendations = st.button(
        "✨ Find My Career"
    )


# --------------------------------------------------
# MAIN CONTENT
# --------------------------------------------------

if not get_recommendations:

    st.markdown(
        '<div class="section-title">🌟 How It Works</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(
            "### 1️⃣ Build Your Profile\n"
            "Select your skills, interests and technologies."
        )

    with col2:
        st.info(
            "### 2️⃣ AI Matching\n"
            "Our recommendation engine compares your profile "
            "with career profiles using similarity logic."
        )

    with col3:
        st.info(
            "### 3️⃣ Get Recommendations\n"
            "Receive ranked career paths based on your profile."
        )

    st.markdown("---")

    st.markdown(
        '<div class="section-title">💡 Start Your Journey</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Use the profile panel on the left and click "
        "**Find My Career** to generate personalized recommendations."
    )


# --------------------------------------------------
# RECOMMENDATIONS
# --------------------------------------------------

else:

    if not skills and not interests and not technologies:

        st.warning(
            "Please select at least one skill, interest, "
            "or technology before getting recommendations."
        )

    else:

        recommendations = recommend_careers(
            user_skills=skills,
            user_interests=interests,
            user_technologies=technologies,
            user_level=level,
            user_domain=domain,
            top_n=5
        )

        st.markdown(
            '<div class="section-title">🎯 Your Career Recommendations</div>',
            unsafe_allow_html=True
        )

        st.write(
            "Based on your profile, these career paths are the strongest matches:"
        )

        # Top recommendation
        top_match = recommendations.iloc[0]

        st.success(
            f"🏆 Best Match: {top_match['career']} — "
            f"{top_match['match_score']:.1f}% Match"
        )

        st.markdown("---")

        # Display recommendation cards
        for index, (_, career) in enumerate(recommendations.iterrows()):

            score = min(float(career["match_score"]), 100)

            career_skills = [
                skill.strip()
                for skill in str(career["skills"]).split(",")
            ]

            user_skill_lower = [skill.lower() for skill in skills]

            matched_skills = [
                skill for skill in career_skills
                if skill.lower() in user_skill_lower
            ]

            if matched_skills:
                matched_text = " • ".join(matched_skills)
            else:
                matched_text = "Profile similarity detected"

            medal = "🥇" if index == 0 else "🎯"

            card_html = f"""<div class="career-card">
<div style="display:flex; justify-content:space-between; align-items:center;">
<div>
<div class="career-title">{medal} {career['career']}</div>
<span class="badge">{career['domain']}</span>
<span class="badge">{career['level']}</span>
</div>
<div class="match-score">{score:.1f}%</div>
</div>
<p style="margin-top:15px;"><strong>Matched Skills:</strong> {matched_text}</p>
<div class="why">
<strong>💡 Why recommended?</strong><br>
This career profile has strong similarity with your selected skills, interests, technologies and preferred domain.
</div>
</div>"""

            st.markdown(card_html, unsafe_allow_html=True)

            st.progress(score / 100)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.markdown("""
<div style="text-align:center; color:#6b7280; padding:20px;">
<strong style="color:#7c3aed;">🤖 AI Career Recommender</strong><br>
Built with Python • Pandas • Scikit-learn • Streamlit<br>
AI Recommendation Logic Project
</div>
""", unsafe_allow_html=True)