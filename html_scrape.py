import requests
from bs4 import BeautifulSoup
import time
import random

class LinkScraper:
    # initialize scraper
    def __init__(self, search_term, pages=5):
        self.search_term = search_term
        self.pages = pages
        self.base_url = f"https://www.amazon.com/s?k={search_term}"
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'
        ]
        self.links = []

    # rotate user agent headers to avoid amazon bot detection
    def get_headers(self):
        return {
            'User-Agent': random.choice(user_agents),
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://www.amazon.com'
        }

    # extract links
    def extract_links_from_page(soup):
        links = []
        # loop over all anchor ('a') tags with specific attributes
        for tag in soup.find_all('a', {'class': 'a-link-normal', 'href': True}):
            href = tag['href']
            # Loop over all anchor ('a') tags with specific attributes
            if '/dp/' in href:   
                full_url = "https://www.amazon.com" + href
                links.append(full_url)
        return links

    def scrape_links(self):
        for page_num in range(0, self.pages):
            soup = self.fetch_page(page_num)
            if soup:
                product_links = self.extract_links_from_page(soup)
                self.all_product_links.extend(product_links)
                print(f"Page {page_num}: Collected {len(product_links)} links")
            time.sleep(0.1)  # small delay to avoid bot detection

        # remove duplicates and return results
        self.all_product_links = list(set(self.all_product_links))
        print(f"Total links collected: {len(self.all_product_links)}")
        return self.all_product_links

search_term = "sweatshirt"
pages = 5
link_scraper = LinkScraper(search_term, pages)
links = link_scraper.scrape_links()
print(all_links)


