from urllib.parse import urlparse


REQUIRED_FIELDS = [
    "source",
    "source_url",
    "name_or_title",
    "scraped_at"
]


def is_valid_url(url):
    """
    Check whether a value is a valid HTTP/HTTPS URL.
    """

    if not isinstance(url, str):
        return False

    try:
        parsed = urlparse(url)

        return parsed.scheme in ["http", "https"] and bool(
            parsed.netloc
        )

    except Exception:
        return False


def validate_required_fields(record):
    """
    Check that all required fields exist
    and are not empty.
    """

    errors = []

    for field in REQUIRED_FIELDS:

        if field not in record:
            errors.append(
                f"Missing required field: {field}"
            )

        elif record[field] is None:
            errors.append(
                f"Required field is None: {field}"
            )

        elif isinstance(record[field], str) and not record[field].strip():
            errors.append(
                f"Required field is empty: {field}"
            )

    return errors


def validate_rating(record):
    """
    Rating must be between 1 and 5.
    """

    rating = record.get("rating")

    if rating is None:
        return []

    if not isinstance(rating, int):
        return ["Rating must be an integer"]

    if rating < 1 or rating > 5:
        return ["Rating must be between 1 and 5"]

    return []


def validate_url(record):
    """
    Validate source_url.
    """

    url = record.get("source_url")

    if url is None:
        return ["source_url cannot be None"]

    if not is_valid_url(url):
        return ["source_url is not a valid URL"]

    return []


def validate_record(record):
    """
    Validate one complete record.
    """

    errors = []

    errors.extend(
        validate_required_fields(record)
    )

    errors.extend(
        validate_rating(record)
    )

    errors.extend(
        validate_url(record)
    )

    return errors


def validate_records(records):
    """
    Validate multiple records.

    Returns:
        valid_records
        invalid_records
    """

    valid_records = []
    invalid_records = []

    for record in records:

        errors = validate_record(record)

        if errors:
            invalid_records.append({
                "record": record,
                "errors": errors
            })

        else:
            valid_records.append(record)

    return valid_records, invalid_records


if __name__ == "__main__":

    # Valid test record
    valid_record = {
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

    # Invalid test record
    invalid_record = {
        "source": "Books to Scrape",
        "source_url": "not-a-url",
        "name_or_title": "",
        "category": None,
        "price": "£51.77",
        "rating": 8,
        "author": None,
        "tags": None,
        "description": None,
        "availability": "In stock",
        "scraped_at": "2026-10-06T16:00:00"
    }

    print("VALID RECORD")
    print(validate_record(valid_record))

    print("\nINVALID RECORD")
    print(validate_record(invalid_record))