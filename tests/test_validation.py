from processing.validation import (
    is_valid_url,
    validate_rating,
    validate_record
)


def create_valid_record():

    return {
        "source": "Books to Scrape",
        "source_url": "https://books.toscrape.com/",
        "name_or_title": "A Light in the Attic",
        "category": None,
        "price": "£51.77",
        "rating": 3,
        "author": None,
        "tags": None,
        "description": None,
        "availability": "In stock",
        "scraped_at": "2026-10-06T16:00:00"
    }


def test_valid_url():

    assert is_valid_url(
        "https://books.toscrape.com/"
    )


def test_invalid_url():

    assert not is_valid_url(
        "not-a-url"
    )


def test_valid_rating():

    record = create_valid_record()

    assert validate_rating(record) == []


def test_invalid_rating():

    record = create_valid_record()

    record["rating"] = 8

    errors = validate_rating(record)

    assert len(errors) > 0


def test_valid_record():

    record = create_valid_record()

    errors = validate_record(record)

    assert errors == []


def test_missing_title():

    record = create_valid_record()

    record["name_or_title"] = ""

    errors = validate_record(record)

    assert len(errors) > 0