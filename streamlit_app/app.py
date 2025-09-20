import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import os  # <-- you were missing this

# ---------------------------
# Page layout
# ---------------------------
st.set_page_config(page_title="CORD-19 Data Explorer", layout="wide")
st.title("CORD-19 Data Explorer")
st.write("""
Explore COVID-19 research papers from the CORD-19 dataset.
Filter by year, see top journals, and visualize common words in titles.
""")

# ---------------------------
# Load data
# ---------------------------
@st.cache_data
def load_data():
    # Get the directory of the current script (app.py)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    # Build the full path to metadata.csv
    data_path = os.path.join(BASE_DIR, "..", "data", "metadata.csv")
    
    # Load the CSV
    df = pd.read_csv(data_path)
    
    # Data cleaning
    df_clean = df.dropna(subset=['title', 'publish_time'])
    df_clean['abstract'] = df_clean['abstract'].fillna("No abstract")
    
    # Convert publish_time to datetime and extract year
    df_clean['publish_time'] = pd.to_datetime(df_clean['publish_time'], errors='coerce')
    df_clean['year'] = df_clean['publish_time'].dt.year
    
    return df_clean

# Call the function and assign df_clean
df_clean = load_data()

# ---------------------------
# Year filter slider
# ---------------------------
min_year = int(df_clean['year'].min())
max_year = int(df_clean['year'].max())
year_range = st.slider("Select Year Range", min_year, max_year, (min_year, max_year))

# Filter dataframe based on selected years
df_filtered = df_clean[(df_clean['year'] >= year_range[0]) & (df_clean['year'] <= year_range[1])]
st.write(f"Showing papers from {year_range[0]} to {year_range[1]}")
st.dataframe(df_filtered[['title', 'journal', 'year']].head(10))  # show first 10 rows

# ---------------------------
# Number of papers by year
# ---------------------------
papers_per_year = df_filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(8,4))
sns.barplot(x=papers_per_year.index, y=papers_per_year.values, palette="viridis", ax=ax)
ax.set_title("Number of Papers by Year")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
st.pyplot(fig)

# ---------------------------
# Top journals
# ---------------------------
top_journals = df_filtered['journal'].value_counts().head(10)
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x=top_journals.values, y=top_journals.index, palette="coolwarm", ax=ax)
ax.set_title("Top 10 Journals")
ax.set_xlabel("Number of Papers")
ax.set_ylabel("Journal")
st.pyplot(fig)

# ---------------------------
# Word Cloud for titles
# ---------------------------
all_titles = " ".join(df_filtered['title'].astype(str))
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)
fig, ax = plt.subplots(figsize=(15,7))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)

# ---------------------------
# Dropdown to select journals
# ---------------------------
journals = df_filtered['journal'].dropna().unique()
selected_journal = st.selectbox("Select Journal", ["All"] + list(journals))


# ---------------------------
# Search box for keywords in title or abstract
# ---------------------------
if selected_journal != "All":
    df_filtered = df_filtered[df_filtered['journal'] == selected_journal]



# ---------------------------
# Distribution of papers by source
# ---------------------------

source_counts = df_filtered['source_x'].value_counts().head(10)
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x=source_counts.values, y=source_counts.index, palette="magma", ax=ax)
ax.set_title("Top Sources")
ax.set_xlabel("Number of Papers")
ax.set_ylabel("Source")
st.pyplot(fig)


num_rows = st.slider("Select number of rows to view", 5, 50, 10)
st.dataframe(df_filtered.head(num_rows))
