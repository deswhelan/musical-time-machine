from bs4 import BeautifulSoup
import datetime
import requests

BASE_URL = "https://www.officialcharts.com/charts/irish-singles-chart/"

def get_chart_date():
    """returns a string representing the user's chosen chart date"""
    chart_date = input(f"For which date would you like a playlist? (YYYY-MM-DD)\n")
    while not is_valid_chart_date(chart_date):
        chart_date = input(f"Please use format YYYY-MM-DD\n")

    return chart_date

def is_valid_chart_date(date_text):
    """Returns True if the user input is in the required YYYY-MM-DD format"""
    try:
        datetime.date.fromisoformat(date_text)
        return True
    except ValueError:
        return False

def get_chartlist(chart_date):
    """Returns a list of dictionaries representing irish singles chart entries on the given date"""
    endpoint = f"{chart_date}/ie7501/".replace("-", "")

    # TODO: include header
    response = requests.get(BASE_URL + endpoint)
    response.raise_for_status()

    chartlist = create_chartlist(response)

    return chartlist

def create_chartlist(response):
    """Creates and returns a list of dictionaries representing irish singles chart entries on the given date"""
    soup = BeautifulSoup(response.text, "html.parser")

    raw_chart_entries = soup.find_all(class_="chart-item-content relative flex w-full")
    chartlist = []

    for i, entry in enumerate(raw_chart_entries):
        entry_elements = entry.select(selector="div p a span")
        chartlist.append({
            "chart_position": i + 1,
            "title": entry_elements[1].text,
            "artist": entry_elements[2].text
        })

    return chartlist

# Main work-flow
chart_date = get_chart_date()
chartlist = get_chartlist(chart_date)

for entry in chartlist:
    print(f"#{entry["chart_position"]}) {entry["title"]}\n{entry["artist"]}\n\n############\n\n")

# TODO: Create Spotify playlist comprising 100 scraped singles


