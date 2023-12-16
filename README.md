# web-scraping-python
A beginner code for web scraping by Python as a Challenge

## Purpose
The Python script aims to scrape a specific Amazon Egypt page to extract and display mobile phone discounts available during Black Friday.

## Steps

1. **Imports**
    - Imported required libraries:
        - `BeautifulSoup` from `bs4`
        - `requests`

2. **Fetch URL**
    - Used the `requests.get()` method to retrieve the HTML content from the target Amazon Egypt URL.

3. **Create BeautifulSoup Object**
    - Created a `BeautifulSoup` object to interact with the HTML structure retrieved from the URL.
    - Chose `lxml` parser due to its capability to handle potentially broken HTML code better than `HTMLParser`.

4. **Find Mobile Cards**
    - Located all HTML elements representing mobile cards by searching for spans with the class `a-list-item`.

5. **Iterate Over Mobile Cards**
    - For each mobile card found:
        - Checked if it had a discounted price by searching for the presence of the `a-text-strike` class within the mobile card.
        
6. **Extract Mobile Information**
    - If a mobile card had a discount:
        - Extracted the mobile name by locating the anchor element (`a-size-base`) and stripped whitespace.
        - Retrieved the real price (with strikeout) and discounted price by locating specific spans with class attributes.
    
7. **Extract Price Values**
    - Filtered out non-digit characters (such as commas and decimals) using the `filter()` method, keeping only the first part of the digit for both real and discounted prices.
    - Converted these extracted strings into integers to perform arithmetic operations for calculating the saved amount.

8. **OutPut**
    - Printed the Black Friday discounts for each qualifying mobile card.
    - Displayed the mobile name, real price vs. discounted price, and the calculated saved amount.


