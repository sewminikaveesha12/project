# University Management System

## Project Overview

The **University Management System** is a Python-based application designed to simulate the management of a university environment. The system models key entities such as students, faculty, staff, courses, and departments using **object-oriented programming (OOP)** principles, including **inheritance**, **encapsulation**, and **polymorphism**.

The system provides a practical demonstration of core OOP concepts while implementing essential functionalities for academic administration.

### Key Features

  * **Class Hierarchy** - Implements a structured hierarchy with the base class `Person` and derived classes: `Student`, `Faculty`, and `Staff`.

\<hr\>

  * **Student Management**
      * Course enrollment and dropping.
      * GPA calculation and academic status tracking.
      * Advanced student management using **encapsulation** through a secure student record with input validation.


  * **Encapsulation**
      * Sensitive student information is securely stored and managed with controlled access and validation.


  * **Polymorphism**
      * Role-specific behaviors and workloads are implemented, allowing uniform handling of different person types.


  * **Department and Course Management**
      * Departments and courses are modeled with enrollment limits and prerequisites.
      * Provides management and display of course and department information.

## Project Structure

```
UniversityManagementSystem/
├── Main.py              # Entry point: demonstrates system functionalities
├── person.py            # Base class Person, with Staff, Student, Faculty subclasses
├── student.py           # Student classes: Undergraduate, Graduate, SecureStudentRecord
├── faculty.py           # Faculty classes: Professor, Lecturer, Teaching Assistant (TA)
├── department.py        # Department and Course classes
└── README.md            # Project documentation
```

## Usage Instructions

### Download or Clone the Project

Ensure all files (`Main.py`, `person.py`, `student.py`, `faculty.py`, `department.py`) are located in the same directory.

### Run the Main File

Open a terminal in the project directory and execute the following command.

```bash
python Main.py
```

### Demonstrations

  * Creation of professors, students, and teaching assistants.
  * Method calls across the class hierarchy demonstrating **inheritance**.
  * Advanced student management operations (enroll, drop, GPA, academic status).
  * Secure student records illustrating **encapsulation** and validation.
  * **Polymorphic** behavior across different person types.
  * Department creation and course management including prerequisites and enrollment information.

-----

# Data Analysis: E-commerce Data Analysis

## Project Overview

This project demonstrates a complete end-to-end workflow for **web scraping**, **data processing**, **statistical analysis**, and **visualization** using Python. The workflow covers three major data sources:

1.  **Books Data:** Scraped from Books to Scrape.
2.  **E-commerce Products Data:** Scraped from WebScraper.io test e-commerce site.
3.  **RSS News Feed:** Parsed from the BBC News RSS feed.

The project also includes cleaning and transforming the data, conducting descriptive and inferential statistical analyses, applying machine learning models for prediction, and producing visualizations for insights.

### Prerequisites

The following Python packages are required:

  * `requests`
  * `BeautifulSoup4` (`bs4`)
  * `pandas`
  * `numpy`
  * `scipy`
  * `matplotlib`
  * `seaborn`
  * `scikit-learn`
  * `plotly`
  * `lxml`

Python version **3.8+** is recommended.

### Installation

Install required packages using `pip`:

```bash
pip install requests beautifulsoup4 pandas numpy scipy matplotlib seaborn scikit-learn plotly lxml
```

## Data Collection

### 1\. Books Data

Scraped from `http://books.toscrape.com`.

Collected information:

  * `title`
  * `price`
  * `stock availability`
  * `rating`
  * `category` (from book detail page)

Scraping includes 20 pages and respects polite crawling delays.

Output saved as **`books.csv`** and **`books.json`**.

### 2\. E-commerce Products

Scraped from `https://webscraper.io/test-sites/e-commerce/allinone`.

Collected information:

  * `product name`
  * `price`
  * `category`
  * `subcategory`
  * `product link`

Data saved as **`shop.csv`** and **`shop.json`**.

### 3\. RSS Feed

Parsed from `http://feeds.bbci.co.uk/news/rss.xml`.

Collected information:

  * `title`
  * `link`
  * `publication date`

Data saved as **`rss.csv`** and **`rss.json`**.

## Data Processing

### Data Cleaning

  * **Price** values cleaned and converted to numeric.
  * **Stock availability** converted to numeric ($\\text{0} = \\text{out of stock}, \\text{1} = \\text{in stock}$).
  * **Ratings** converted to numeric ($\\text{One}=1, \\text{Two}=2, \\ldots \\text{Five}=5$).
  * **Dates** from RSS feed parsed into `datetime` objects.

### Data Transformation

  * Aggregated categories and subcategories for books and e-commerce products.
  * Prepared dataframes (`books_df`, `shop_df`, `rss_df`) for analysis.

## Data Analysis

### 1\. Books Analysis

  * **Descriptive statistics:** mean, median, mode, standard deviation of prices.
  * **Outlier detection** using IQR.
  * **Frequency distribution** for book ratings.
  * **Correlation analysis** between price, rating, and stock.
  * **Hypothesis testing:** t-test comparing mean prices of Fiction vs Non-Fiction.
  * **Regression analysis:** Linear regression predicting price based on rating.
  * Average price per category calculated.

### 2\. E-commerce Analysis

  * Descriptive statistics for prices.
  * Outlier detection.
  * Frequency distribution of categories and subcategories.

### 3\. RSS Feed Analysis

  * Frequency distribution of news articles by publication date.

## Data Visualization

  * **Histograms** for price distributions by category.
  * **Boxplots** for book prices by category.
  * **Scatter plots** showing:
      * Rating vs Price
      * Stock vs Price
  * **Bar charts** for:
      * Category popularity
      * Average rating per category

Boxplots and scatterplots use `matplotlib` and `seaborn` for aesthetic and informative visuals.
