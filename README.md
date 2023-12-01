# Mercedez-Benz.io Quality Assurance Technical Challenge

Developed by pfariaj@gmail.com

## Overview

This project demonstrates the use of Playwright with Python to validate the negative path of enquiring the highest price at Mercedes-Benz. The script automates the process of accessing the Mercedes-Benz website, attempting to inquire about the highest price, and validating the expected negative behavior.

## Requirements

- Python 3.x
- Playwright for Python

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/pfariaj/mercedezbenz.git
cd mercedezbenz
```

1. Install the required Python packages using requirements.txt:
```bash
pip install -r requirements.txt
```
This will install Playwright and its dependencies.

## Usage

1. Modify the script or add your Playwright test file to suit your specific test scenario.

2. Run the script:
```bash
pytest tests/test_highest_price.py  
```
This will execute the Playwright script to validate the negative path of enquiring the highest price at Mercedes-Benz.

## Script Explanation
- The script is designed to automate the negative path scenario by interacting with the Mercedes-Benz website.
- It uses Playwright to locate elements, perform actions, and validate the expected behavior.
- Make sure to adjust the script according to your specific test case and website changes.

