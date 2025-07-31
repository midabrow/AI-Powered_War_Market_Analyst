from src.rss.fetcher import RssFetcher

def fetch_all_news(save: bool = True):
    fetcher = RssFetcher()
    df = fetcher.fetch()
    if save:
        fetcher.save_to_file(df)
    return df
