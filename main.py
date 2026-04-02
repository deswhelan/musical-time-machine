from bs4 import BeautifulSoup
import datetime
import requests

def is_valid_date_input(date_text):
    try:
        datetime.date.fromisoformat(date_text)
        return True
    except ValueError:
        return False

playlist_date = input(f"For which date would you like a playlist? (YYYY-MM-DD)\n")
while not is_valid_date_input(playlist_date):
    playlist_date = input(f"Please use format YYYY-MM-DD\n")

# TODO: Webscrape top 100 singles for chosen date
# TODO: Create Spotify playlist comprising 100 scraped singles


