import requests
from bs4 import BeautifulSoup
from .models import ScrapedData

def scrape_data():
    url = "https://www.nseindia.com/"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            headlines = soup.find_all('h2')  

            ScrapedData.objects.all().delete()

            for headline in headlines:
                title = headline.text.strip()
                if title:  # Only create if there's a title
                    ScrapedData.objects.create(title=title)
                    print(f"Saved headline: {title}") 
        else:
            print(f"Failed to retrieve data: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}") 
