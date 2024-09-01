import requests
from bs4 import BeautifulSoup

# URL of the e-commerce website or product page
url = 'https://asana.com/product'  # Replace with the actual URL

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all products on the page
    products = soup.find_all('div', class_='product-item')  # Replace with the actual class or tag
    
    # Iterate over each product and extract relevant data
    for product in products:
        # Extract product name
        name = product.find('h2', class_='product-title').get_text(strip=True)  # Replace with actual tag and class
        
        # Extract product price
        price = product.find('span', class_='product-price').get_text(strip=True)  # Replace with actual tag and class
        
        # Extract product reviews
        reviews = product.find('div', class_='product-reviews').get_text(strip=True)  # Replace with actual tag and class
        
        # Extract competitor information (assuming it’s included in the product info)
        competitors = product.find('div', class_='competitor-info').get_text(strip=True)  # Replace with actual tag and class
        
        # Print or store the extracted data
        print(f'Product Name: {name}')
        print(f'Price: {price}')
        print(f'Reviews: {reviews}')
        print(f'Competitor Info: {competitors}')
        print('-' * 40)

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
