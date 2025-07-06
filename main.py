from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json
import pandas as pd
from helper import get_treatment_links

def scrapper():
    options = Options()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    url = "https://www.orthoinfo.org/en/treatment/"
    driver.get(url)
    try:
        while True:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.article-list"))
            )

            soup = BeautifulSoup(driver.page_source, "html.parser")
            sections = soup.select("div.article-list")

            for section in sections:
                articles = section.select("a.article-list-item")
                for article in articles:
                    type_tag = article.select_one("p.article-list-item-type")
                    content_type = type_tag.get_text(strip=True).lower() if type_tag else ""
                    # check to scrape only articles not videos and other content
                    if content_type != "article":
                        continue

                    title_tag = article.select_one("h3.article-list-item-title")
                    title = title_tag.get_text(strip=True) if title_tag else "Unknown Title"

                    link = article['href']
                    full_link = f"https://www.orthoinfo.org{link}"

                    print(f"Now Scraping: {title}")
                    
            try:
                next_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//small[contains(@class, 'pagination-next-text') and text()='Next']"))
                )
                print("going to the next page")
                driver.execute_script("arguments[0].click();", next_button)
            except:
                print("No more pages..")
                break
    finally:
        driver.quit()

def main():
    scrapper()

if __name__ == "__main__":
    main()
