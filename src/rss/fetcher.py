# src/rss/fetcher.py

import logging
import feedparser
import pandas as pd
from datetime import datetime
from typing import Dict
from .config import RSS_SOURCES

logger = logging.getLogger(__name__)


class RssFetcher:
    def __init__(self, sources: Dict[str, str] = RSS_SOURCES):
        self.sources = sources

    def parse_feed(self, feed: feedparser.FeedParserDict) -> pd.DataFrame:
        entries = [
            {
                "title": entry.get("title", ""),
                "link": entry.get("link", ""),
                "published": entry.get("published", ""),
                "summary": entry.get("summary", "")
            }
            for entry in feed.entries
        ]
        return pd.DataFrame(entries)

    def fetch(self) -> pd.DataFrame:
        all_data = []

        for name, url in self.sources.items():
            logger.info(f"🔎 Fetching {name}...")
            feed = feedparser.parse(url)

            if feed.entries:
                logger.info(f"✅ Found {len(feed.entries)} entries.")
                df = self.parse_feed(feed)
                df["source"] = name
                df["text"] = df["title"].fillna("") + " " + df["summary"].fillna("")
                all_data.append(df)
            else:
                logger.warning(f"⚠️ No entries found in {name}")

        if not all_data:
            logger.error("❌ No data retrieved from any feed.")
            return pd.DataFrame()

        return pd.concat(all_data, ignore_index=True)

    def save_to_file(self, df: pd.DataFrame, folder: str = "data") -> str:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        output_path = f"{folder}/classified_news_{timestamp}.json"
        df.to_json(output_path, orient="records", force_ascii=False, indent=2)
        logger.info(f"💾 Saved to {output_path}")
        return output_path
