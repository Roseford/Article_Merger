import requests
from bs4 import BeautifulSoup

def scrape_data_from_url(url):
    try:
        # Set a custom User-Agent header to mimic a web browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }

        # Send an HTTP GET request to the provided URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Here, you can specify the HTML elements you want to scrape
            # For example, let's say you want to scrape all the text within <p> tags
            paragraphs = soup.find_all('p')

            # Initialize a variable to store the scraped data
            scraped_data = []

            # Extract the text from each <p> tag and store it in the variable
            for paragraph in paragraphs:
                scraped_data.append(paragraph.get_text())

            return scraped_data

        else:
            return f"Failed to retrieve data. Status code: {response.status_code}"

    except Exception as e:
        return f"An error occurred: {str(e)}"
