import requests
from bs4 import BeautifulSoup
import csv

# Define the URL of the e-commerce page (replace this with the actual URL)
url = 'https://example.com/products'  # Replace with the actual URL of the e-commerce page

# Send a GET request to fetch the page content
response = requests.get(url)

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Open a CSV file to write the product data
with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header row in the CSV file
    writer.writerow(['Product Name', 'Price', 'Rating'])
    
    # Find all the product containers (replace this with actual HTML structure of the site)
    products = soup.find_all('div', class_='product-item')  # Example class name for product container

    for product in products:
        # Extract product name
        name = product.find('h2', class_='product-title').get_text(strip=True)  # Adjust class name
        # Extract product price
        price = product.find('span', class_='price').get_text(strip=True)  # Adjust class name
        # Extract product rating
        rating = product.find('span', class_='rating').get_text(strip=True)  # Adjust class name

        # Write product information to CSV file
        writer.writerow([name, price, rating])

print("Product data has been successfully extracted and stored in products.csv")
