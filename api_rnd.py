import requests
from bs4 import BeautifulSoup
import csv
import optparse
import googlemaps
import argparse

import sys

from neighborhood import Neighborhood

def get_neighborhood_prices(city, state, workplace, client):
    '''
        Given a city name and the state it's in, return a dict of
        neighborhood: rent_price values.
    '''
    prices = {}
    with open('1_bedroom_rent.csv', newline='') as csvfile:
        n_reader = csv.reader(csvfile, delimiter=',')
        for row in n_reader:
            if row[1] == city and row[2] == state:
                nh = Neighborhood(
                    f"{row[0]}, {row[1]}, {row[2]}",
                    row[-1],
                    workplace,
                    client
                    )
                duration = nh.find_transit_duration()
                print(f"{nh.name} to {nh.workplace} takes {nh.duration}.")
                prices[f"{row[0]}, {row[1]}, {row[2]}"] = row[-1]
    return prices

def main():
    '''
        Driver function that takes in command-line options city and state,
        and does magic with the parameters.
    '''
    parser = argparse.ArgumentParser(
        description='Find cheap neighborhoods around a city.'
    )
    parser.add_argument('--city', required=True,
        help='Select the city you want to work in')
    parser.add_argument('--state', required=True,
        help='Select the state you want to work in (two characters)')
    parser.add_argument('--place', required=True,
        help='Enter address of your workplace (in quotes)')


    args = parser.parse_args()
    city = args.city
    state = args.state
    place = args.place
    if len(state) != 2:
        print("Please enter a valid state name (two characters exactly).")
        sys.exit(1)
    with open('maps.key', 'r') as f:
        key = f.readline().rstrip('\n')
        client = googlemaps.Client(key=key)
    prices = get_neighborhood_prices(city, state, place, client)


    # print(prices)


if __name__ == '__main__':
    main()
