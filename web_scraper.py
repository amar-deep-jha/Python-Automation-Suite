# Web scraper script
import requests, pandas as pd
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
print(f"Scraping {url} ...")
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

quotes = []
for q in soup.select(".quote"):
    text = q.find("span", class_="text").get_text(strip=True)
    author = q.find("small", class_="author").get_text(strip=True)
    quotes.append({"Quote": text, "Author": author})

df = pd.DataFrame(quotes)
df.to_csv("data_scraped.csv", index=False, encoding="utf-8-sig")
print("✅ Data saved to data_scraped.csv")
