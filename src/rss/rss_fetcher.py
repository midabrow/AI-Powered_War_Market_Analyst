import feedparser
import pandas as pd
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from datetime import datetime

rss_dict = {
    # 'WaronTheRocks': 'https://warontherocks.com/feed/'
    'BreakingDefense': 'https://breakingdefense.com/full-rss-feed/?v=2'
    # 'DefenseOne': 'https://www.defenseone.com/rss/all/'
    # 'TheDrive': 'https://www.thedrive.com/rss',
    # 'MilitaryTimes': 'https://www.militarytimes.com/rss/',
    # 'TheNationalInterest': 'https://nationalinterest.org/rss.xml'
    # 'TheNewYorkTimes': 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
    # 'DefencePost': 'https://thedefensepost.com/feed/',
    # 'TheEconomist': 'https://www.economist.com/sections/international/rss',
    # 'BBC': 'http://feeds.bbci.co.uk/news/world/rss.xml',
    # 'CNN': 'http://rss.cnn.com/rss/edition_world.rss',
    # 'TheGuardian': 'https://www.theguardian.com/world/rss',
}
def parse_feed(feed: feedparser.FeedParserDict) -> pd.DataFrame:   
    data = []
    for entry in feed.entries:
        data.append({
            'title': entry.get('title', ''),
            'link': entry.get('link', ''),
            'published': entry.get('published', ''),
            'summary': entry.get('summary', '')
        })
    
    return pd.DataFrame(data)

def fetch_all_rss(urls: dict) -> pd.DataFrame:
    """Parses RSS feeds from the provided URLs and returns a concatenated DataFrame."""
    all_data = []

    for source_name, source_url in urls.items():
        print(f"\nParsing feed from {source_name}...")
        feed = feedparser.parse(source_url)

        if 'entries' in feed and len(feed.entries) > 0:
            print(f"✅ Found {len(feed.entries)} entries.")
            df = parse_feed(feed)
            df["source"] = source_name 
            df["text"] = df["title"].fillna("") + " " + df["summary"].fillna("")
            all_data.append(df)
        else:
            print("⚠️ No entries found or feed is malformed.")
    
    df_concat = pd.concat(all_data, ignore_index=True) if all_data else pd.DataFrame()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    output_path = f"data/classified_news_{timestamp}.json"

    df.to_json(output_path, orient="records", force_ascii=False, indent=2)
    
    return df_concat