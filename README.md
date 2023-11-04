# Web Scraping with BeautifulSoup

This repository contains a Python script that uses BeautifulSoup to scrape titles from a webpage and print them to the console.

## Description

The script sends a GET request to a specified URL, parses the page content using BeautifulSoup, and finds all the elements with the `h1`, `h2`, or `title` tags. It then prints the text of each title found on the page.

## Installation

Before running the script, you need to install the required packages using pip:

```shell
pip install requests beautifulsoup4
```

## Usage

To use the script, simply run it with Python:

```shell
python scrape_titles.py
```

Make sure to modify the `URL` variable in the script to the website you wish to scrape.

