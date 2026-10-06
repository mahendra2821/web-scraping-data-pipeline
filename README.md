# Web Scraping & Data Processing Pipeline

A Python-based web scraping and data processing pipeline that collects structured data from multiple public demo websites, cleans and validates the collected records, removes duplicates, and exports the final dataset in JSON and CSV formats.

---

## 📌 Project Overview

This project demonstrates an end-to-end web scraping workflow using Python.

The application:

1. Scrapes data from multiple websites
2. Handles pagination
3. Handles HTTP errors and retries
4. Converts data into a common schema
5. Cleans the scraped data
6. Validates records
7. Removes duplicate records
8. Generates JSON and CSV files
9. Maintains application logs
10. Provides automated unit tests

The project is designed with a modular structure so that scraping, processing, validation, deduplication, testing, and output generation are separated into independent components.

---

## 🌐 Data Sources

### 1. Books to Scrape

Source:

https://books.toscrape.com/

The Books scraper collects information such as:

- Book title
- Product URL
- Price
- Rating
- Availability
- Source
- Scraped timestamp

Only information available from the source is collected. Missing information is represented as `None` rather than being invented.

---

### 2. Quotes to Scrape

Source:

https://quotes.toscrape.com/

The Quotes scraper collects:

- Quote text
- Author
- Tags
- Source
- Page URL
- Scraped timestamp

Fields that are not available from the source are kept as `None`.

---

# 🏗️ Project Architecture

The application follows a simple pipeline architecture:

```text
             ┌─────────────────────┐
             │   Books Scraper     │
             └──────────┬──────────┘
                        │
                        │
             ┌──────────▼──────────┐
             │   Quotes Scraper    │
             └──────────┬──────────┘
                        │
                        ▼
               ┌────────────────┐
               │  Raw Records   │
               └───────┬────────┘
                       │
                       ▼
               ┌────────────────┐
               │ Data Cleaning  │
               └───────┬────────┘
                       │
                       ▼
               ┌────────────────┐
               │   Validation   │
               └───────┬────────┘
                       │
                       ▼
               ┌────────────────┐
               │ Deduplication  │
               └───────┬────────┘
                       │
             ┌─────────┴─────────┐
             │                   │
             ▼                   ▼
       ┌───────────┐       ┌───────────┐
       │   JSON    │       │    CSV    │
       └───────────┘       └───────────┘
             │                   │
             └─────────┬─────────┘
                       ▼
                  Final Dataset
```

---

# 📂 Project Structure

```text
scraping_assignment/
│
├── main.py
├── logging_config.py
├── requirements.txt
├── README.md
├── AI_USAGE.md
├── .gitignore
│
├── scrapers/
│   ├── __init__.py
│   ├── books_scraper.py
│   └── quotes_scraper.py
│
├── processing/
│   ├── __init__.py
│   ├── cleaning.py
│   ├── validation.py
│   └── deduplication.py
│
├── tests/
│   ├── test_cleaning.py
│   ├── test_validation.py
│   └── test_deduplication.py
│
├── output/
│   ├── scraped_data.csv
│   └── scraped_data.json
│
└── logs/
    └── scraper.log
```

---

# 🧰 Technologies Used

| Technology          | Purpose                              |
| ------------------- | ------------------------------------ |
| Python              | Core programming language            |
| Requests            | HTTP requests and web access         |
| BeautifulSoup       | HTML parsing and data extraction     |
| Pytest              | Automated testing                    |
| JSON                | Structured data export               |
| CSV                 | Tabular data export                  |
| Logging             | Application monitoring and debugging |
| Virtual Environment | Dependency isolation                 |

---

# 📋 Common Data Schema

All scraped records are converted into a common structure.

```text
source
source_url
name_or_title
category
price
rating
author
tags
description
availability
scraped_at
```

# 🔄 Processing Pipeline

## 1. Scraping

The application collects data from:

- Books to Scrape
- Quotes to Scrape

Both scrapers support pagination and use a common record structure.

---

## 2. Data Cleaning

The cleaning module:

- Removes unnecessary whitespace
- Normalizes multiple spaces
- Cleans text fields
- Cleans price values
- Cleans tag lists
- Preserves missing values as `None`

## 3. Data Validation

The validation module checks:

### Required fields

- `source`
- `source_url`
- `name_or_title`
- `scraped_at`

### URL validation

The application verifies that URLs contain:

- `http`
- or `https`

and a valid network location.

## 4. Deduplication

Duplicate records are removed before generating the final output.

### Books

The scraping layer includes:

- Request timeout handling
- HTTP error handling
- Retry mechanism
- Handling of HTTP `429`
- Handling of HTTP `5xx` errors
- Pagination handling
- Safe URL joining
- Logging of scraping progress
- Graceful handling of request failures

The HTTP client uses retries with backoff for temporary server/network failures.

---

# 🧪 Testing

The project includes automated tests for:

- Data cleaning
- Data validation
- URL validation
- Rating validation
- Deduplication

Run all tests with:

```cmd
python -m pytest
```

Current test result:

```text
6 passed
```

Example:

```text
============================= test session starts =============================

6 passed

============================== 6 passed in 0.11s ==============================
```

---

# 📤 Output

After running the application, the final dataset is generated inside:

```text
output/
```

# ▶️ Installation

## 1. Clone or download the project

Open a terminal and navigate to the project directory.

Example:

```cmd
cd /d "C:\Users\HP\Downloads\frontend\scraping_assignment"
```

---

## 2. Create a virtual environment

```cmd
python -m venv venv
```

---

## 3. Activate the virtual environment

Windows:

```cmd
venv\Scripts\activate
```

After activation, the terminal should show:

```text
(venv)
```

---

## 4. Install dependencies

```cmd
pip install -r requirements.txt
```

---

# 🚀 Running the Application

From the project root:

```cmd
python main.py
```

The pipeline will automatically:

```text
Scrape
   ↓
Combine
   ↓
Clean
   ↓
Validate
   ↓
Deduplicate
   ↓
Export JSON
   ↓
Export CSV
   ↓
Write Logs
```

---

# 📊 Expected Result

After successful execution, the application generates:

```text
output/
├── scraped_data.csv
└── scraped_data.json
```

and:

```text
logs/
└── scraper.log
```

A successful execution displays a summary similar to:

```text
===================================
SCRAPING PIPELINE COMPLETED
===================================

Books scraped      : ...
Quotes scraped     : ...
Total scraped      : ...
Valid records      : ...
Invalid records    : ...
Duplicates removed : ...
Final records      : ...

Output files:
JSON: output\scraped_data.json
CSV : output\scraped_data.csv

===================================
```

The exact record counts may vary depending on the source websites and scraping results.

---

# 🔍 Running Individual Components

## Books Scraper

```cmd
python scrapers\books_scraper.py
```

## Quotes Scraper

```cmd
python scrapers\quotes_scraper.py
```

## Cleaning

```cmd
python processing\cleaning.py
```

## Validation

```cmd
python processing\validation.py
```

## Deduplication

```cmd
python processing\deduplication.py
```

---

# 🧪 Development Workflow

A typical development workflow is:

```text
1. Modify code
      ↓
2. Run individual component
      ↓
3. Run automated tests
      ↓
4. Run complete pipeline
      ↓
5. Check output files
      ↓
6. Check logs
```

Commands:

```cmd
python -m pytest
```

then:

```cmd
python main.py
```

---

# 📐 Design Principles

The project follows these principles:

### No invented data

If information is not available from the source, the application does not create or guess a value.

### Separation of concerns

Scraping, cleaning, validation, deduplication, logging, and output generation are kept in separate modules.

### Reusable processing

Cleaning, validation, and deduplication functions can be reused with additional data sources.

### Fault tolerance

Temporary HTTP failures are handled through retries and error handling.

### Testability

Core processing logic is covered by automated tests.

### Maintainability

The project uses a modular folder structure so individual components can be modified without changing the entire application.

---

# 🤖 AI Usage

AI assistance was used during development for:

- Understanding assignment requirements
- Project planning
- Python explanations
- Debugging
- Code review
- Test design
- Documentation assistance

The final implementation was executed and tested in the local development environment.

More information is available in:

```text
AI_USAGE.md
```

---

# ✅ Project Status

The core scraping pipeline has been implemented and tested.

```text
Books Scraper          ✅
Quotes Scraper         ✅
Pagination             ✅
Common Schema          ✅
Data Cleaning          ✅
Data Validation        ✅
Deduplication          ✅
Error Handling         ✅
Retry Mechanism        ✅
Logging                ✅
JSON Export            ✅
CSV Export             ✅
Automated Tests        ✅
Documentation          ✅
```

---

# 👨‍💻 Author

**Mahendra Babu**

B.Tech Computer Science Engineering — CSE (AI)

2026 Graduate

---

## 📄 License

This project was created for educational and technical assessment purposes.
