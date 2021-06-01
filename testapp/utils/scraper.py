# imports
import time
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import chromedriver_autoinstaller

class WebScraper:
    """
    Search a keyword across multiple search engines for a pre-defined number of pages
    """

    def __init__(self, search_term, num_pages) -> None:

        self.search_term = search_term
        self.num_pages = num_pages
        return
    
    def search_arxiv(self):
        
        URL_ = 'https://arxiv.org/search/?query='
        url_end = '&searchtype=all&source=header&size=200'
        url_full = URL_ + self.search_term + url_end


        chromedriver_autoinstaller.install()
        driver = webdriver.Chrome()

        arxiv_links = []

        time.sleep(3)

        page_number = 1
        while True:
            if page_number <= self.num_pages:
                try:
                    webPageSource = driver.page_source
                    soup = BeautifulSoup(webPageSource, "html.parser")

                    for i in soup.findAll('a'):
                        try:
                            url = i['href']
                            if 'pdf' in url and url not in arxiv_links:
                                arxiv_links.append(url)
                            else:
                                continue
                        except:
                            pass
                    if page_number <= self.num_pages:
                        nextButton = driver.find_element_by_xpath('//*[@id="main-container"]/div[2]/nav[2]/ul/li[{x}]/a'.format(x=page_number+1))
                        nextButton.click()
                        page_number += 1
                except:
                    print('Arxiv search of', self.num_pages, 'pages on topic of', self.search_term, 'is complete.')
                    print('Found', len(arxiv_links), 'results from', page_number, 'pages.' )
                    driver.quit()
                    break
            else:
                print('Arxiv search is done with', len(arxiv_links), 'results found.')
                driver.quit()
                break
    
        return arxiv_links

        
    def search_basesearch(self):
        
        return

        
    def search_duckduckgo(self):
        
        return

    def search_scholar(self):
        
        return
    
    def search_refseek(self):
        
        return

    def search(self):
        links = self.search_arxiv(search_term = self.search_term, num_pages = self.num_pages)

        return links