import requests
from bs4 import BeautifulSoup
from datetime import datetime


BASE_URL = "https://books.toscrape.com/"


def get_rating(book):
    """
    Extract rating from the CSS class.
    Example:
    class="star-rating Three"
    """
    rating_element = book.select_one(".star-rating")

    if not rating_element:
        return None

    rating_classes = rating_element.get("class", [])

    for rating in ["One", "Two", "Three", "Four", "Five"]:
        if rating in rating_classes:
            return {
                "One": 1,
                "Two": 2,
                "Three": 3,
                "Four": 4,
                "Five": 5
            }[rating]

    return None


def scrape_books():
    books = []
    current_url = BASE_URL

    while current_url:

        print(f"Scraping: {current_url}")

        try:
            response = requests.get(
                current_url,
                timeout=10
            )

            response.raise_for_status()

        except requests.RequestException as error:
            print(f"Failed to scrape {current_url}: {error}")
            current_url = None
            continue

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        book_cards = soup.select(
            "article.product_pod"
        )

        for book in book_cards:

            # Title
            title_element = book.select_one("h3 a")
            title = (
                title_element.get("title")
                if title_element
                else None
            )

            # Product URL
            product_url = None

            if title_element:
                product_url = requests.compat.urljoin(
                    current_url,
                    title_element.get("href")
                )

            # Price
            price_element = book.select_one(
                ".price_color"
            )

            price = (
                price_element.get_text(strip=True)
                if price_element
                else None
            )

            # Availability
            availability_element = book.select_one(
                ".availability"
            )

            availability = (
                availability_element.get_text(
                    " ",
                    strip=True
                )
                if availability_element
                else None
            )

            # Rating
            rating = get_rating(book)

            # Standardized record
            book_data = {
                "source": "Books to Scrape",
                "source_url": product_url,
                "name_or_title": title,
                "category": None,
                "price": price,
                "rating": rating,
                "author": None,
                "tags": None,
                "description": None,
                "availability": availability,
                "scraped_at": datetime.now().isoformat()
            }

            books.append(book_data)

        # Pagination
        next_button = soup.select_one(
            "li.next a"
        )

        if next_button:
            next_page = next_button.get("href")

            current_url = requests.compat.urljoin(
                current_url,
                next_page
            )
        else:
            current_url = None

    return books


if __name__ == "__main__":

    books = scrape_books()

    print(
        f"\nTotal books scraped: {len(books)}"
    )

    print("\nFirst book:")

    if books:
        print(books[0])