
import time
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import chromedriver_autoinstaller
from django.core.management.base import BaseCommand

from testapp.utils import scraper

class Command(BaseCommand):
    def handle(self, *args, **options) -> None:

        keyword = "soccer"
        pages = 1

        scraper = scraper.WebScraper(search_term = keyword, num_pages = pages)
        links = scraper.search()

        print('Searched for: ', keyword)
        print(links)


        return