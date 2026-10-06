def get_record_key(record):
    """
    Create a unique key for a record.

    We primarily use source_url because
    it identifies the original page.
    """

    source = record.get("source")
    source_url = record.get("source_url")

    if source_url:
        return (
            str(source).strip().lower(),
            str(source_url).strip().lower()
        )

    # Fallback if source_url is unavailable
    title = record.get("name_or_title")

    return (
        str(source).strip().lower()
        if source
        else "",
        str(title).strip().lower()
        if title
        else ""
    )


def remove_duplicates(records):
    """
    Remove duplicate records.

    Keeps the first occurrence of each record.
    """

    unique_records = []
    seen_keys = set()

    duplicate_records = []

    for record in records:

        key = get_record_key(record)

        if key in seen_keys:

            duplicate_records.append(record)

        else:

            seen_keys.add(key)
            unique_records.append(record)

    return unique_records, duplicate_records


if __name__ == "__main__":

    test_records = [

        {
            "source": "Books to Scrape",
            "source_url": "https://books.toscrape.com/book1",
            "name_or_title": "Book One"
        },

        {
            "source": "Books to Scrape",
            "source_url": "https://books.toscrape.com/book2",
            "name_or_title": "Book Two"
        },

        # Duplicate of Book One
        {
            "source": "Books to Scrape",
            "source_url": "https://books.toscrape.com/book1",
            "name_or_title": "Book One"
        }
    ]

    unique_records, duplicate_records = remove_duplicates(
        test_records
    )

    print(f"Original records: {len(test_records)}")
    print(f"Unique records: {len(unique_records)}")
    print(f"Duplicates removed: {len(duplicate_records)}")

    print("\nUnique records:")

    for record in unique_records:
        print(record)