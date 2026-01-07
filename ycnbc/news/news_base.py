from typing import Dict, Callable
from .news_utils import CNBCNewsUtils
from .uri import _NEWS_URI_


class News:
    def __init__(self) -> None:
        self.news: CNBCNewsUtils = CNBCNewsUtils()

    def latest(self) -> Dict:  # type: ignore
        return self.news.latest()

    def trending(self) -> Dict:  # type: ignore
        return self.news.trending()

    def __getattr__(self, name: str) -> Callable[[], Dict]:
        # Convert method name (e.g., "europe_politics") to category string (e.g., "europe-politics")
        category_name = name.replace('_', '-')
        if category_name in _NEWS_URI_:
            return lambda: self.news.by_category(_NEWS_URI_[category_name])
        raise AttributeError(
            f"'{type(self).__name__}' object has no attribute '{name}'")
