# parsing_data_saving_results
# Divan.ru Lights Scraper

This project is a web scraper for the [Divan.ru](https://www.divan.ru/category/potolocnye-svetilniki) website, which extracts information about ceiling lights, including the name, price, and product URL. The data is saved in a CSV file.

## Description

The program uses the Selenium library to automate interaction with the web page and extract data. For each light fixture, the following details are extracted:

- Name of the light
- Price of the light
- URL of the product page

The data is saved in the `ligths.csv` file in CSV format, where each row corresponds to one product.

## Requirements

To run the program, you need to have the following installed:

- Python 3.x
- [Selenium](https://pypi.org/project/selenium/) library
- A web driver for your browser (e.g., [geckodriver](https://github.com/mozilla/geckodriver/releases) for Firefox or [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) for Chrome)

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/divan-lights-scraper.git
    cd divan-lights-scraper
    ```

2. Install the required libraries:

    ```bash
    pip install selenium
    ```

3. Ensure that the web driver for your browser is in your PATH or in the project directory.

## Usage

1. Run the script:

    ```bash
    python scraper.py
    ```

2. The script will automatically open a browser, navigate to the ceiling lights page, and start extracting data. The names, prices, and product links will be printed in the console.

3. After completing the extraction, the browser will close automatically, and the data will be saved to the `ligths.csv` file.

## Error Handling

The program handles possible errors during data extraction from the web page using `try` and `except` blocks. If an error occurs, the message "Failed to retrieve..." will be written to the CSV file in place of the missing value, and an error message will be printed in the console.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact

If you have any questions or suggestions, feel free to contact me via email: [your.email@example.com](mailto:your.email@example.com).
