import logging
from typing import List, Dict, Optional
from lxml import html
from curl_cffi import requests
 

from .uri import _HEADERS_, _BASE_URL_
from ..exceptions import ParsingError

logger = logging.getLogger(__name__)


class CNBCNewsUtils:
    def __init__(self) -> None:
        self.base_url: str = _BASE_URL_
        self.headers: Dict[str, str] = _HEADERS_
        self.request: requests.Session = requests.Session()

    def _fetch_page(self, endpoint: str = "") -> html.HtmlElement:
        """
        Fetches and parses the web page content.

        Args:
            endpoint (str): The specific endpoint to fetch data from.

        Returns:
            html.Element: Parsed HTML tree.
        Raises:
            YCNBCError: If there's an issue fetching the page.
        """
        url: str = f"{self.base_url}/{endpoint}" if endpoint else self.base_url
        logger.info(f"Fetching URL: {url}")
        page: requests.Response = self.request.get(
            url, headers=self.headers, impersonate="chrome110", timeout=30)
        page.raise_for_status()
        return html.fromstring(page.content)

    def trending(self) -> Dict[str, List[Optional[str]]]:
        """
        Fetches trending news.

        Returns:
            dict: Dictionary containing titles and links of trending news.
        Raises:
            DataNotFoundError: If trending news data is not found.
            ParsingError: If there's an issue parsing the data.
        """
        try:
            tree: html.HtmlElement = self._fetch_page()

            trending_news: List[html.HtmlElement] = tree.xpath(
                "//li[contains(@class, 'TrendingNowItem')]")
            if not trending_news:
                logger.warning("Trending news data not found.")
                return []

            parsed_news: List[Dict[str, Optional[str]]] = []
            for i in trending_news:
                text: List[str] = i.xpath(".//a/text()")
                link: Optional[str] = list(i.iterlinks())[
                    0][2] if list(i.iterlinks()) else None
                headline = ' '.join(text).encode('ascii', 'ignore').decode('ascii')
                parsed_news.append({'headline': headline, 'link': link})

            return parsed_news
        except Exception as e:
            logger.error(f"Error parsing trending news: {e}")
            raise ParsingError(f"Error parsing trending news: {e}") from e

    def latest(self) -> List[Dict[str, Optional[str]]]:
        """
        Fetches the latest news by scraping the HTML from the /latest/ page.
        """
        try:
            # Fetch the HTML from the /latest/ endpoint
            tree: html.HtmlElement = self._fetch_page('latest/')
            if isinstance(tree, dict) and 'error' in tree:
                raise ParsingError(f"Failed to fetch page: {tree['error']}")

            parsed_news: List[Dict[str, Optional[str]]] = []

            # Find all the news card containers
            article_elements = tree.xpath("//div[contains(@class, 'Card-card')]")
            
            if not article_elements:
                logger.warning("Could not find article elements on /latest/ page. XPath might be wrong.")
                return []

            for element in article_elements:
                # Extract data from within each card
                headline_list = element.xpath(".//a[contains(@class, 'Card-title')]/text()")
                link_list = element.xpath(".//a[contains(@class, 'Card-title')]/@href")
                time_list = element.xpath(".//span[contains(@class, 'Card-time')]/text()")

                headline = ' '.join(headline_list).strip() if headline_list else None
                link = link_list[0] if link_list else None
                time = ' '.join(time_list).strip() if time_list else None
                
                if headline and link:
                    # Ensure the link is absolute
                    if link.startswith('/'):
                        link = f"https://www.cnbc.com{link}"
                    parsed_news.append({'headline': headline, 'time': time, 'link': link})

            return parsed_news
        except Exception as e:
            logger.error(f"Error parsing latest news from HTML: {e}")
            raise ParsingError(f"Error parsing latest news from HTML: {e}") from e

    def by_category(self, category: str) -> Dict[str, List[Optional[str]]]:
        """
        Fetches news based on the category.

        Args:
            category (str): The news category to fetch.

        Returns: dict: Dictionary containing headlines, post times, and links for the specified category.
        Raises:
            DataNotFoundError: If news for the specified category is not found.
            ParsingError: If there's an issue parsing the data.
        """
        try:
            tree: html.HtmlElement = self._fetch_page(category)

            news_elements: List[html.HtmlElement] = tree.cssselect(
                '.Card-titleContainer a.Card-title')
            post_time_elements: List[html.HtmlElement] = tree.cssselect(
                'span.Card-time')

            if not news_elements or not post_time_elements:
                logger.warning(
                    f"No news elements or post time elements found for category: {category}")
                return []

            parsed_news: List[Dict[str, Optional[str]]] = []
            for news_element, post_time_element in zip(news_elements, post_time_elements):
                headline = news_element.text.strip().encode('ascii', 'ignore').decode('ascii')
                link = news_element.get('href')
                post_time = post_time_element.text.strip()
                parsed_news.append({'headline': headline, 'time': post_time, 'link': link})

            return parsed_news

        except Exception as e:
            logger.error(f"Error parsing news for category {category}: {e}")
            raise ParsingError(
                f"Error parsing news for category {category}: {e}") from e

        except Exception as e:
            logger.error(f"Error parsing news for category {category}: {e}")
            raise ParsingError(
                f"Error parsing news for category {category}: {e}") from e
