# def clean_text(value):
#     """
#     Clean unnecessary whitespace from text.
#     """

#     if value is None:
#         return None

#     if not isinstance(value, str):
#         return value

#     value = " ".join(value.split())

#     return value.strip()


# def clean_price(price):
#     """
#     Clean price while keeping the original currency.
#     Example:
#     '£51.77' → '£51.77'
#     """

#     if price is None:
#         return None

#     return clean_text(price)


# def clean_tags(tags):
#     """
#     Clean a list of tags.
#     """

#     if tags is None:
#         return None

#     if not isinstance(tags, list):
#         return tags

#     cleaned_tags = []

#     for tag in tags:

#         cleaned_tag = clean_text(tag)

#         if cleaned_tag:
#             cleaned_tags.append(cleaned_tag)

#     return cleaned_tags


# def clean_record(record):
#     """
#     Clean one scraped record.
#     """

#     cleaned_record = record.copy()

#     # Text fields
#     text_fields = [
#         "source",
#         "source_url",
#         "name_or_title",
#         "category",
#         "author",
#         "description",
#         "availability"
#     ]

#     for field in text_fields:

#         if field in cleaned_record:
#             cleaned_record[field] = clean_text(
#                 cleaned_record[field]
#             )

#     # Price
#     if "price" in cleaned_record:
#         cleaned_record["price"] = clean_price(
#             cleaned_record["price"]
#         )

#     # Tags
#     if "tags" in cleaned_record:
#         cleaned_record["tags"] = clean_tags(
#             cleaned_record["tags"]
#         )

#     return cleaned_record


# def clean_records(records):
#     """
#     Clean multiple scraped records.
#     """

#     cleaned_records = []

#     for record in records:

#         cleaned_record = clean_record(record)

#         cleaned_records.append(cleaned_record)

#     return cleaned_records


# if __name__ == "__main__":

#     test_record = {
#         "source": " Books to Scrape ",
#         "source_url": " https://example.com/book ",
#         "name_or_title": "  A   Light   in   the Attic  ",
#         "category": None,
#         "price": " £51.77 ",
#         "rating": 3,
#         "author": None,
#         "tags": [" poetry ", " children "],
#         "description": None,
#         "availability": " In stock ",
#         "scraped_at": "2026-10-06T16:00:00"
#     }

#     cleaned = clean_record(test_record)

#     print("Before cleaning:")
#     print(test_record)

#     print("\nAfter cleaning:")
#     print(cleaned)



def clean_text(value):
    """
    Clean a text value by removing extra spaces.
    """
    if value is None:
        return None

    if not isinstance(value, str):
        return value

    value = " ".join(value.split())

    return value.strip()


def clean_price(price):
    """
    Clean price values.
    """
    if price is None:
        return None

    return clean_text(price)


def clean_tags(tags):
    """
    Clean a list of tags.
    """
    if tags is None:
        return None

    if not isinstance(tags, list):
        return tags

    cleaned_tags = []

    for tag in tags:
        cleaned_tag = clean_text(tag)

        if cleaned_tag:
            cleaned_tags.append(cleaned_tag)

    return cleaned_tags


def clean_record(record):
    """
    Clean one scraped record.
    """

    cleaned_record = record.copy()

    text_fields = [
        "source",
        "source_url",
        "name_or_title",
        "category",
        "author",
        "description",
        "availability"
    ]

    for field in text_fields:

        if field in cleaned_record:
            cleaned_record[field] = clean_text(
                cleaned_record[field]
            )

    if "price" in cleaned_record:
        cleaned_record["price"] = clean_price(
            cleaned_record["price"]
        )

    if "tags" in cleaned_record:
        cleaned_record["tags"] = clean_tags(
            cleaned_record["tags"]
        )

    return cleaned_record


def clean_records(records):
    """
    Clean multiple scraped records.
    """

    cleaned_records = []

    for record in records:

        cleaned_record = clean_record(record)

        cleaned_records.append(cleaned_record)

    return cleaned_records


if __name__ == "__main__":

    test_record = {
        "source": " Books to Scrape ",
        "source_url": " https://example.com/book ",
        "name_or_title": "  A   Light   in   the Attic  ",
        "category": None,
        "price": " £51.77 ",
        "rating": 3,
        "author": None,
        "tags": [" poetry ", " children "],
        "description": None,
        "availability": " In stock ",
        "scraped_at": "2026-10-06T16:00:00"
    }

    print("Before cleaning:")
    print(test_record)

    cleaned = clean_record(test_record)

    print("\nAfter cleaning:")
    print(cleaned)