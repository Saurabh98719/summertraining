import streamlit as st
import pandas as pd
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import KNeighborsClassifier

# 1. PAGE CONFIG - DARK THEME LIKE IMAGE
st.set_page_config(
    page_title="Live Movie Recommendation",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CUSTOM CSS FOR BLACK THEME
st.markdown("""
    <style>
   .stApp {
        background-color: #0e1117;
        color: #fafafa;
    }
    h1, h3 {
        color: #fafafa;
        text-align: center;
    }
   .stButton>button {
        background-color: #00bfff;
        color: black;
        font-weight: bold;
        border-radius: 8px;
        height: 3em;
        width: 100%;
    }
   .stButton>button:hover {
        background-color: #1e90ff;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. LOAD DATA
@st.cache_data
def load_data():
    paths = [
        Path('Data for repository.csv'),
        Path('Data for repository.xlsx'),
        Path('Data for repository.xls')
    ]
    data_path = next((path for path in paths if path.exists()), None)
    if data_path is None:
        raise FileNotFoundError('Dataset file not found. Please add Data for repository.csv or Data for repository.xls in the app folder.')

    try:
        if data_path.suffix.lower() in {'.xls', '.xlsx'}:
            df = pd.read_excel(data_path)
        else:
            df = pd.read_csv(data_path)
    except Exception:
        # Some files may be misnamed .xls/.xlsx but actually contain CSV text.
        df = pd.read_csv(data_path)

    df.columns = df.columns.str.strip()
    df = df.dropna(subset=['Movie_Name', 'Lead_Star', 'Director', 'Genre'])
    df['tags'] = df['Lead_Star'].astype(str) + ' ' + df['Genre'].astype(str)
    return df

try:
    df = load_data()
except FileNotFoundError as error:
    st.error(str(error))
    st.stop()

# 3. TRAIN MODELS
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['tags'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Genre Prediction Model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(tfidf_matrix, df['Genre'])

# 4. UI - SAME AS IMAGE
st.title("🎬 Live Movie Recommendation")
st.caption("Discover recommended movies in real time.")
st.write("")

# DROPDOWNS
lead_star = st.selectbox("Lead Star", sorted(df['Lead_Star'].unique()))
genre = st.selectbox("Genre", sorted(df['Genre'].unique()))
franchise = st.selectbox("Whether Franchise", ["Yes", "No"])

# 5. BUTTON AND LOGIC
if st.button("Predict Genre & Get Recommendations"):
    
    # PREDICT GENRE
    input_text = f"{lead_star} {genre}"
    input_vec = tfidf.transform([input_text])
    predicted_genre = knn.predict(input_vec)[0]
    
    st.success(f"### Predicted Genre: {predicted_genre}")
    
    st.write("---")
    st.subheader("Recommended Movies")
    
    # RECOMMEND MOVIES
    idx = df[df['Lead_Star'] == lead_star].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    movie_indices = [i[0] for i in sim_scores]
    
    recommendations = df.iloc[movie_indices][['Movie_Name', 'Lead_Star', 'Director', 'Genre']]
    st.dataframe(recommendations, use_container_width=True, hide_index=True)