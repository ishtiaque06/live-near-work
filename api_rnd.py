import requests
from bs4 import BeautifulSoup
import csv
import optparse
import googlemaps
import argparse

import sys

def get_neighborhood_prices(city, state):
    prices = {}
    with open('1_bedroom_rent.csv', newline='') as csvfile:
        n_reader = csv.reader(csvfile, delimiter=',')
        for row in n_reader:
            if row[1] == city and row[2] == state:
                prices[f"{row[0]}, {row[1]}, {row[2]}"] = row[-1]
    return prices

def main():
    parser = argparse.ArgumentParser(
        description='Find cheap neighborhoods around a city.'
    )
    parser.add_argument('--city', required=True,
        help='Select the city you want to work in')
    parser.add_argument('--state', required=True,
        help='Select the state you want to work in (two characters)')


    args = parser.parse_args()
    city = args.city
    state = args.state
    if len(state) != 2:
        print("Please enter a valid state name (two characters exactly).")
        sys.exit(1)
    print(city, state)
    prices = get_neighborhood_prices(city, state)


    print(prices)


if __name__ == '__main__':
    main()
