from fastapi import APIRouter
from pydantic import BaseModel
from src.rss.fetcher import RssFetcher


router = APIRouter()

@router.get("/rss/fetch")
def fetch_rss_feed() -> list[dict]:
    fetcher = RssFetcher()
    feed = fetcher.fetch()
    return feed.to_dict(orient="records")