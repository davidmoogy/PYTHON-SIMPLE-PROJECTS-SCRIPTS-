import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website to scrape
url = 'http://quotes.toscrape.com'

# Function to scrape quotes
def scrape_quotes():
    quotes = []
    page = 1
    
    while True:
        response = requests.get(f"{url}/page/{page}/")
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all quote containers
        quote_divs = soup.find_all('div', class_='quote')
        if not quote_divs:
            break

        for quote_div in quote_divs:
            text = quote_div.find('span', class_='text').get_text()
            author = quote_div.find('small', class_='author').get_text()
            tags = [tag.get_text() for tag in quote_div.find_all('a', class_='tag')]
            
            quotes.append({
                'Text': text,
                'Author': author,
                'Tags': ', '.join(tags)
            })
        
        page += 1

    return quotes

# Function to save quotes to a CSV file
def save_to_csv(quotes, filename='quotes.csv'):
    df = pd.DataFrame(quotes)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    print("Scraping quotes...")
    quotes = scrape_quotes()
    save_to_csv(quotes)
    print("Scraping complete.")
