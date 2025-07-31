from fastapi import APIRouter
from pydantic import BaseModel
from src.rss.fetcher import RssFetcher


router = APIRouter()

@router.get("/rss/fetch")
def fetch_rss_feed() -> dict:
    fetcher = RssFetcher()
    feed = fetcher.fetch()
    return fetch.to_dict(orient="records")