import streamlit as st
import pandas as pd

st.set_page_config(page_title="War Events Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("data/tagged_balanced.csv")  # lub z GSheets

df = load_data()

st.title("📊 War Events Intelligence Dashboard")

# Sidebar filters
st.sidebar.header("🎛️ Filters")

sector_filter = st.sidebar.multiselect("Select sectors:", df['sector'].unique().tolist(), default=df['sector'].unique().tolist())
tag_filter = st.sidebar.multiselect("Select tags:", df['tag'].unique().tolist(), default=df['tag'].unique().tolist())
search_keyword = st.sidebar.text_input("Search in title/analysis:")

# Apply filters
filtered_df = df[
    (df['sector'].isin(sector_filter)) &
    (df['tag'].isin(tag_filter))
]

if search_keyword:
    filtered_df = filtered_df[
        filtered_df['title'].str.contains(search_keyword, case=False, na=False) |
        filtered_df['analysis'].str.contains(search_keyword, case=False, na=False)
    ]

st.markdown(f"### Showing {len(filtered_df)} events")
st.dataframe(filtered_df.sort_values("date", ascending=False), use_container_width=True)
