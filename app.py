import streamlit as st
import pandas as pd
import joblib

# Set Streamlit page configuration
st.set_page_config(page_title="🎥 Movie Popularity Predictor", layout="wide")

# Background Image (Cinema theme)
page_bg_img = """
<style>
.stApp {
    background-image: url("https://tse4.mm.bing.net/th/id/OIP.9R4_7wsayFgr8hZbSEytLwHaEK?r=0&rs=1&pid=ImgDetMain&o=7&rm=3");
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
    color: white;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Title and Subheading
st.markdown("<h1 style='text-align: center; color: white;'>🍿 AI-Powered Movie Popularity Predictor</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: white;'>Fill in your movie details and let the machine learning model predict how popular your movie will be!</h4>", unsafe_allow_html=True)

# Load the trained model
model = joblib.load("popular_movies.pkl")

# Input Form
with st.form("movie_form"):
    st.markdown("### 🎬 Enter Movie Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        budget = st.number_input("💰 Budget (USD)", min_value=0, value=50000000, step=1000000)
        runtime = st.slider("⏱️ Runtime (minutes)", min_value=60, max_value=180, value=120)
        vote_average = st.slider("⭐ Average Vote", 0.0, 10.0, 7.0)

    with col2:
        vote_count = st.slider("📢 Vote Count", 0, 20000, 1000)
        revenue = st.number_input("💵 Revenue (USD)", min_value=0, value=100000000, step=1000000)
        genre = st.selectbox("🎭 Genre", ['Action', 'Comedy', 'Drama', 'Fantasy', 'Horror', 'Thriller', 'Animation', 'Science Fiction', 'Mystery', 'Family', 'Unknown'])

    with col3:
        language = st.selectbox("🗣️ Language", ['English', 'Spanish', 'French', 'Hindi', 'Chinese', 'Japanese', 'Russian', 'German', 'Unknown'])
        country = st.selectbox("🌍 Country", ['United States', 'United Kingdom', 'India', 'China', 'Canada', 'France', 'Germany', 'Australia', 'Unknown'])

    submitted = st.form_submit_button("🎯 Predict Popularity")

# When form is submitted
if submitted:
    input_df = pd.DataFrame({
        'budget': [budget],
        'runtime': [runtime],
        'vote_average': [vote_average],
        'vote_count': [vote_count],
        'revenue': [revenue],
        'genre': [genre],
        'language': [language],
        'country': [country]
    })

    prediction = model.predict(input_df)[0]

    st.markdown("---")

    # Show BIG result
    st.markdown(f"<h2 style='text-align: center; color: #FFD700;'>🎯 Predicted Popularity Score: {prediction:.2f}</h2>", unsafe_allow_html=True)

    # Conditional message
    if prediction >= 20:
        st.markdown("<h3 style='text-align: center; color: lightgreen;'>🌟 This movie has great potential to be a HIT! 🌟</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='text-align: center; color: salmon;'>⚠️ This movie might struggle to gain popularity. ⚠️</h3>", unsafe_allow_html=True)

    st.markdown("<p style='text-align: center; color: white;'>📊 The higher the score, the more popular your movie is likely to be based on trends.</p>", unsafe_allow_html=True)

st.markdown("<hr style='border:1px solid white'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>🛠️ Developed by <b>Suleman</b></p>", unsafe_allow_html=True)
