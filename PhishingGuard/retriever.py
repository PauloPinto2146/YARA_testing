import requests
import os
import json

from dotenv import load_dotenv

def get_phishing_data():
    api_url = "https://api.phishstats.info/api/phishing"

    response = requests.get(api_url)
    response.raise_for_status()

    data = response.json()

    print(json.dumps(data, indent=4))
if __name__ == "__main__":
	get_phishing_data()