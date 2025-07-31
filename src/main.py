from fastapi import FastAPI
from src.api import rss_fetcher, classifier, sector_mapper, analyzer, rag

app = FastAPI()

app.include_router(rss_fetcher.router)
app.include_router(classifier.router)
app.include_router(sector_mapper.router)
app.include_router(analyzer.router)
app.include_router(rag.router)
