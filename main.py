# import json
# import csv
# import os
# import logging

# from fastapi import logger


# from logging_config import setup_logging
# from scrapers.books_scraper import scrape_books
# from scrapers.quotes_scraper import scrape_quotes

# from processing.cleaning import clean_records
# from processing.validation import validate_records
# from processing.deduplication import remove_duplicates


# OUTPUT_DIR = "output"


# def save_json(records, filename):
#     """
#     Save records to a JSON file.
#     """

#     filepath = os.path.join(
#         OUTPUT_DIR,
#         filename
#     )

#     with open(
#         filepath,
#         "w",
#         encoding="utf-8"
#     ) as file:

#         json.dump(
#             records,
#             file,
#             indent=4,
#             ensure_ascii=False
#         )

#     print(f"Saved JSON: {filepath}")


# def save_csv(records, filename):
#     """
#     Save records to a CSV file.
#     """

#     if not records:
#         print("No records to save to CSV.")
#         return

#     filepath = os.path.join(
#         OUTPUT_DIR,
#         filename
#     )

#     fieldnames = [
#         "source",
#         "source_url",
#         "name_or_title",
#         "category",
#         "price",
#         "rating",
#         "author",
#         "tags",
#         "description",
#         "availability",
#         "scraped_at"
#     ]

#     with open(
#         filepath,
#         "w",
#         newline="",
#         encoding="utf-8"
#     ) as file:

#         writer = csv.DictWriter(
#             file,
#             fieldnames=fieldnames
#         )

#         writer.writeheader()

#         for record in records:

#             row = record.copy()

#             # CSV cannot directly store Python lists
#             if isinstance(row.get("tags"), list):
#                 row["tags"] = ", ".join(
#                     row["tags"]
#                 )

#             writer.writerow(row)

#     print(f"Saved CSV: {filepath}")

# def main():

#     logger = setup_logging()

#     logger.info("Scraping pipeline started")

#     print("=" * 60)
#     print("WEB SCRAPING PIPELINE")
#     print("=" * 60)

#     # Make sure output directory exists
#     os.makedirs(
#         OUTPUT_DIR,
#         exist_ok=True
#     )

#     # --------------------------------------------------
#     # 1. SCRAPING
#     # --------------------------------------------------

#     print("\n[1] Scraping Books...")

#     logger.info("Starting Books scraper")

#     books = scrape_books()

#     logger.info(
#         "Books scraping completed: %d records",
#         len(books)
#     )

#     print(
#         f"Books scraped: {len(books)}"
#     )

#     print("\n[2] Scraping Quotes...")

#     logger.info("Starting Quotes scraper")

#     quotes = scrape_quotes()

#     logger.info(
#         "Quotes scraping completed: %d records",
#         len(quotes)
#     )

#     print(
#         f"Quotes scraped: {len(quotes)}"
#     )

#     all_records = books + quotes

#     logger.info(
#         "Total scraped records: %d",
#         len(all_records)
#     )

#     print(
#         f"\nTotal scraped records: {len(all_records)}"
#     )

#     # --------------------------------------------------
#     # 2. CLEANING
#     # --------------------------------------------------

#     print("\n[3] Cleaning records...")

#     logger.info("Starting data cleaning")

#     cleaned_records = clean_records(
#         all_records
#     )

#     logger.info(
#         "Cleaning completed: %d records",
#         len(cleaned_records)
#     )

#     print(
#         f"Records cleaned: {len(cleaned_records)}"
#     )

#     # --------------------------------------------------
#     # 3. VALIDATION
#     # --------------------------------------------------

#     print("\n[4] Validating records...")

#     logger.info("Starting validation")

#     valid_records, invalid_records = validate_records(
#         cleaned_records
#     )

#     logger.info(
#         "Validation completed | Valid: %d | Invalid: %d",
#         len(valid_records),
#         len(invalid_records)
#     )

#     print(
#         f"Valid records: {len(valid_records)}"
#     )

#     print(
#         f"Invalid records: {len(invalid_records)}"
#     )

#     # Log validation errors
#     for invalid_record in invalid_records:

#         logger.warning(
#             "Invalid record: %s",
#             invalid_record["errors"]
#         )

#     # --------------------------------------------------
#     # 4. DEDUPLICATION
#     # --------------------------------------------------

#     print("\n[5] Removing duplicates...")

#     logger.info("Starting deduplication")

#     unique_records, duplicate_records = remove_duplicates(
#         valid_records
#     )

#     logger.info(
#         "Deduplication completed | "
#         "Unique: %d | Duplicates: %d",
#         len(unique_records),
#         len(duplicate_records)
#     )

#     print(
#         f"Unique records: {len(unique_records)}"
#     )

#     print(
#         f"Duplicates removed: {len(duplicate_records)}"
#     )

#     # --------------------------------------------------
#     # 5. SAVE OUTPUT
#     # --------------------------------------------------

#     print("\n[6] Saving output...")

#     logger.info("Saving JSON output")

#     save_json(
#         unique_records,
#         "scraped_data.json"
#     )

#     logger.info("Saving CSV output")

#     save_csv(
#         unique_records,
#         "scraped_data.csv"
#     )

#     logger.info(
#         "Output successfully generated"
#     )

#     # --------------------------------------------------
#     # SUMMARY
#     # --------------------------------------------------

#     print("\n" + "=" * 60)
#     print("PIPELINE COMPLETED")
#     print("=" * 60)

#     print(
#         f"Total scraped: {len(all_records)}"
#     )

#     print(
#         f"Valid: {len(valid_records)}"
#     )

#     print(
#         f"Invalid: {len(invalid_records)}"
#     )

#     print(
#         f"Duplicates removed: {len(duplicate_records)}"
#     )

#     print(
#         f"Final records: {len(unique_records)}"
#     )

#     print("\nOutput files:")

#     print(
#         "output\\scraped_data.json"
#     )

#     print(
#         "output\\scraped_data.csv"
#     )

#     logger.info(
#         "Scraping pipeline completed successfully"
#     )




import json
import csv
import os

from scrapers.books_scraper import scrape_books
from scrapers.quotes_scraper import scrape_quotes

from processing.cleaning import clean_records
from processing.validation import validate_records
from processing.deduplication import remove_duplicates

from logging_config import setup_logging


OUTPUT_DIR = "output"


def save_json(records, filename):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4, ensure_ascii=False)

    return filepath


def save_csv(records, filename):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    filepath = os.path.join(OUTPUT_DIR, filename)

    fieldnames = [
        "source",
        "source_url",
        "name_or_title",
        "category",
        "price",
        "rating",
        "author",
        "tags",
        "description",
        "availability",
        "scraped_at"
    ]

    with open(filepath, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for record in records:
            row = record.copy()

            if isinstance(row.get("tags"), list):
                row["tags"] = ", ".join(row["tags"])

            writer.writerow(row)

    return filepath


def main():

    logger = setup_logging()

    logger.info("Scraping pipeline started")

    # -----------------------------
    # STEP 1: SCRAPE BOOKS
    # -----------------------------

    logger.info("Starting Books scraper")

    books = scrape_books()

    logger.info(
        f"Books scraping completed: {len(books)} records"
    )

    # -----------------------------
    # STEP 2: SCRAPE QUOTES
    # -----------------------------

    logger.info("Starting Quotes scraper")

    quotes = scrape_quotes()

    logger.info(
        f"Quotes scraping completed: {len(quotes)} records"
    )

    # -----------------------------
    # STEP 3: COMBINE
    # -----------------------------

    all_records = books + quotes

    logger.info(
        f"Total scraped records: {len(all_records)}"
    )

    # -----------------------------
    # STEP 4: CLEAN
    # -----------------------------

    logger.info("Starting data cleaning")

    cleaned_records = clean_records(all_records)

    logger.info(
        f"Cleaning completed: {len(cleaned_records)} records"
    )

    # -----------------------------
    # STEP 5: VALIDATE
    # -----------------------------

    logger.info("Starting validation")

    valid_records, invalid_records = validate_records(
        cleaned_records
    )

    logger.info(
        f"Validation completed | "
        f"Valid: {len(valid_records)} | "
        f"Invalid: {len(invalid_records)}"
    )

    for invalid in invalid_records:
        logger.warning(
            f"Invalid record: {invalid['errors']}"
        )

    # -----------------------------
    # STEP 6: DEDUPLICATE
    # -----------------------------

    logger.info("Starting deduplication")

    unique_records, duplicate_records = remove_duplicates(
        valid_records
    )

    logger.info(
        f"Deduplication completed | "
        f"Unique: {len(unique_records)} | "
        f"Duplicates: {len(duplicate_records)}"
    )

    # -----------------------------
    # STEP 7: SAVE JSON
    # -----------------------------

    logger.info("Saving JSON output")

    json_file = save_json(
        unique_records,
        "scraped_data.json"
    )

    # -----------------------------
    # STEP 8: SAVE CSV
    # -----------------------------

    logger.info("Saving CSV output")

    csv_file = save_csv(
        unique_records,
        "scraped_data.csv"
    )

    logger.info("Output successfully generated")

    # -----------------------------
    # FINAL SUMMARY
    # -----------------------------

    print("\n===================================")
    print("SCRAPING PIPELINE COMPLETED")
    print("===================================")

    print(f"Books scraped      : {len(books)}")
    print(f"Quotes scraped     : {len(quotes)}")
    print(f"Total scraped      : {len(all_records)}")
    print(f"Valid records      : {len(valid_records)}")
    print(f"Invalid records    : {len(invalid_records)}")
    print(f"Duplicates removed : {len(duplicate_records)}")
    print(f"Final records      : {len(unique_records)}")

    print("\nOutput files:")
    print(f"JSON: {json_file}")
    print(f"CSV : {csv_file}")

    print("\n===================================")

    logger.info("Scraping pipeline completed successfully")


if __name__ == "__main__":
    main()