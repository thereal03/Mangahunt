import requests
from bs4 import BeautifulSoup

# Replace this with the URL of the website you want to scrape
url = 'https://mangasee123.com/'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # You can now use BeautifulSoup to extract data from the page
    # For example, let's extract all the links on the page
    links = soup.find_all('a')
    
    # Print the extracted links
    for link in links:
        print(link.get('href'))

else:
    print(f'Failed to retrieve the web page. Status code: {response.status_code}')
