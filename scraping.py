from cgitb import text
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import matplotlib.pyplot as plt
import pandas as pd

# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

url = 'http://quotes.toscrape.com/'
browser.visit(url)
html = browser.html
quote_soup = soup(html, 'html.parser')

quotes = quote_soup.find_all('span', class_ = 'text')

for x in range(1, 6):
    html = browser.html
    quote_soup = soup(html, 'html.parser')
    quotes = quote_soup.find_all('span', class_='text')
    for quote in quotes:
        print('page:', x, '----------')
        print(quote.text)
    browser.links.find_by_partial_text('Next').click()

browser.quit()