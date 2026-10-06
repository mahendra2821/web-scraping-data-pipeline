import logging
import os


LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "scraper.log")


def setup_logging():
    """
    Configure application logging.
    """

    os.makedirs(LOG_DIR, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(
                LOG_FILE,
                encoding="utf-8"
            ),
            logging.StreamHandler()
        ],
        force=True
    )

    return logging.getLogger("scraper")