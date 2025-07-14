import feedparser
import pandas as pd
from typing import List, Dict

rss_dict = {
    'WaronTheRocks': 'https://warontherocks.com/feed/',
    'BreakingDefense': 'https://breakingdefense.com/full-rss-feed/?v=2',
    'DefenseOne': 'https://www.defenseone.com/rss/all/',
    'TheDrive': 'https://www.thedrive.com/rss',
    'MilitaryTimes': 'https://www.militarytimes.com/rss/',
    'TheNationalInterest': 'https://nationalinterest.org/rss.xml',
    'TheNewYorkTimes': 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
    'DefencePost': 'https://thedefensepost.com/feed/',
    'TheEconomist': 'https://www.economist.com/sections/international/rss',
    'BBC': 'http://feeds.bbci.co.uk/news/world/rss.xml',
    'CNN': 'http://rss.cnn.com/rss/edition_world.rss',
    'TheGuardian': 'https://www.theguardian.com/world/rss',
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
    
    return pd.concat(all_data, ignore_index=True) if all_data else pd.DataFrame()


if __name__ == "__main__":
    df = fetch_all_rss(rss_dict)
    df.to_csv("../data/raw_rss.csv", index=False)
    print(f"✅ Saved {len(df)} articles to data/raw_rss.csv")
