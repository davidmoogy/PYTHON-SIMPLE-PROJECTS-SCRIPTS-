import requests
import pandas as pd

# Configuration
api_url = 'https://jsonplaceholder.typicode.com/posts'
csv_filename = 'api_data.csv'

# Function to fetch data from the API
def fetch_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Function to save data to a CSV file
def save_to_csv(data, filename):
    try:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data: {e}")

if __name__ == "__main__":
    print("Fetching data from API...")
    data = fetch_data(api_url)
    if data:
        print("Data fetched successfully.")
        save_to_csv(data, csv_filename)
        print("Process complete.")
