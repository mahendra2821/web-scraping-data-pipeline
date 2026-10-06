# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime


# BASE_URL = "https://quotes.toscrape.com/"


# def scrape_quotes():
#     quotes = []
#     current_url = BASE_URL

#     while current_url:

#         print(f"Scraping: {current_url}")

#         try:
#             response = requests.get(
#                 current_url,
#                 timeout=10
#             )

#             response.raise_for_status()

#         except requests.RequestException as error:
#             print(f"Failed to scrape {current_url}: {error}")
#             current_url = None
#             continue

#         soup = BeautifulSoup(
#             response.text,
#             "html.parser"
#         )

#         quote_cards = soup.select(".quote")

#         for quote in quote_cards:

#             # Quote text
#             text_element = quote.select_one(".text")

#             text = (
#                 text_element.get_text(strip=True)
#                 if text_element
#                 else None
#             )

#             # Author
#             author_element = quote.select_one(".author")

#             author = (
#                 author_element.get_text(strip=True)
#                 if author_element
#                 else None
#             )

#             # Tags
#             tag_elements = quote.select(".tags .tag")

#             tags = [
#                 tag.get_text(strip=True)
#                 for tag in tag_elements
#             ]

#             # Author profile URL
#             author_url = None

#             author_link = quote.select_one(
#                 ".author + a"
#             )

#             if author_link:
#                 author_url = requests.compat.urljoin(
#                     current_url,
#                     author_link.get("href")
#                 )

#             # Standardized record
#             quote_data = {
#                 "source": "Quotes to Scrape",
#                 "source_url": author_url,
#                 "name_or_title": text,
#                 "category": None,
#                 "price": None,
#                 "rating": None,
#                 "author": author,
#                 "tags": tags,
#                 "description": None,
#                 "availability": None,
#                 "scraped_at": datetime.now().isoformat()
#             }

#             quotes.append(quote_data)

#         # Pagination
#         next_button = soup.select_one(
#             "li.next a"
#         )

#         if next_button:
#             next_page = next_button.get("href")

#             current_url = requests.compat.urljoin(
#                 current_url,
#                 next_page
#             )
#         else:
#             current_url = None

#     return quotes


# if __name__ == "__main__":

#     quotes = scrape_quotes()

#     print(
#         f"\nTotal quotes scraped: {len(quotes)}"
#     )

#     print("\nFirst quote:")

#     if quotes:
#         print(quotes[0])




import logging
import requests

from bs4 import BeautifulSoup
from datetime import datetime
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


BASE_URL = "https://quotes.toscrape.com/"

logger = logging.getLogger("scraper")


def create_session():
    """
    Create a requests session with retry support.
    """

    session = requests.Session()

    session.headers.update({
        "User-Agent": (
            "Mozilla/5.0 "
            "(Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 "
            "(KHTML, like Gecko) "
            "Chrome/154.0 Safari/537.36"
        )
    })

    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[
            429,
            500,
            502,
            503,
            504
        ],
        allowed_methods=[
            "GET"
        ]
    )

    adapter = HTTPAdapter(
        max_retries=retry_strategy
    )

    session.mount(
        "http://",
        adapter
    )

    session.mount(
        "https://",
        adapter
    )

    return session


def scrape_quotes():

    quotes = []

    current_url = BASE_URL

    session = create_session()

    while current_url:

        logger.info(
            "Scraping quotes page: %s",
            current_url
        )

        try:

            response = session.get(
                current_url,
                timeout=10
            )

            response.raise_for_status()

        except requests.RequestException as error:

            logger.error(
                "Failed to scrape %s: %s",
                current_url,
                error
            )

            break

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        quote_cards = soup.select(
            ".quote"
        )

        logger.info(
            "Found %d quotes on page",
            len(quote_cards)
        )

        for quote in quote_cards:

            # -----------------------------
            # Quote text
            # -----------------------------

            text_element = quote.select_one(
                ".text"
            )

            text = (
                text_element.get_text(
                    strip=True
                )
                if text_element
                else None
            )

            # -----------------------------
            # Author
            # -----------------------------

            author_element = quote.select_one(
                ".author"
            )

            author = (
                author_element.get_text(
                    strip=True
                )
                if author_element
                else None
            )

            # -----------------------------
            # Tags
            # -----------------------------

            tag_elements = quote.select(
                ".tags .tag"
            )

            tags = [
                tag.get_text(
                    strip=True
                )
                for tag in tag_elements
            ]

            # -----------------------------
            # Author URL
            # -----------------------------

            author_url = None

            author_link = quote.select_one(
                ".author + a"
            )

            if author_link:

                href = author_link.get(
                    "href"
                )

                if href:

                    author_url = requests.compat.urljoin(
                        current_url,
                        href
                    )

            # -----------------------------
            # Standardized record
            # -----------------------------

            quote_data = {

                "source": "Quotes to Scrape",

                "source_url": author_url,

                "name_or_title": text,

                "category": None,

                "price": None,

                "rating": None,

                "author": author,

                "tags": tags,

                "description": None,

                "availability": None,

                "scraped_at": datetime.now().isoformat()
            }

            quotes.append(
                quote_data
            )

        # -----------------------------
        # Pagination
        # -----------------------------

        next_button = soup.select_one(
            "li.next a"
        )

        if next_button:

            next_page = next_button.get(
                "href"
            )

            if next_page:

                current_url = requests.compat.urljoin(
                    current_url,
                    next_page
                )

            else:

                current_url = None

        else:

            current_url = None

    logger.info(
        "Quotes scraping completed: %d records",
        len(quotes)
    )

    return quotes


if __name__ == "__main__":

    quotes = scrape_quotes()

    print(
        f"\nTotal quotes scraped: {len(quotes)}"
    )

    if quotes:

        print("\nFirst quote:")

        print(quotes[0])