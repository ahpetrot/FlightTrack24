#!/usr/bin/env python

import requests
import json
import random
import argparse
from prettytable import PrettyTable


def random_headers():
    return {'User-Agent': random.choice(desktop_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}


def table_header_text():
    return (
        ['Mode(S)', 'Lat.', 'Long.', 'Heading', 'Alt.', 'Speed', 'Squak', '8', 'Equipment', 'CallSign', 'Epoch',
         'Source',
         'Destination', 'Flight #', '15', '16', '17', '18', 'Country Code (ICAO)'])


def flight_count(flights):
    number_of_flights = len(flights)
    return (number_of_flights)


def random_flight(flights):
    single_random_flight = random.choice(flights)
    # print("Random Flight: ", random_flight)

    table = PrettyTable(table_header_text())
    table.add_row(data.get(single_random_flight))
    print(table)

    # return (data.get(random_flight))


def all_flights(flights):
    table = PrettyTable(table_header_text())

    x = 0
    for flight in flights:

        table.add_row(data.get(flight))
        x += 1
        if (x == 20):
            print(table)
            table = PrettyTable(table_header_text())

            x = 0

    print(table)


def debug(flights):
    print(flights)

    # for flight in flights:

    #       type(flight)
    #       print(data.get(flight))


def show_stats(values):
    print(values)


desktop_agents = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']

url = "https://data-live.flightradar24.com/zones/fcgi/feed.js?faa=1&mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&maxage=7200&gliders=1&stats=1"

responce = requests.get(url, headers=random_headers())

data = json.loads(responce.text)

# print(type(data));
# print(data)

# stats = data['full_count']
# data_verion = data['version']
# data_stats = data['stats']


data_stats = {
    "full_count": data['full_count'],
    "version": data['version'],
    "staticts": data['stats']
}

# print(data_stats)

del data['full_count']
del data['version']
del data['stats']

# raise SystemExit
# // Pull Key's from Dict and create a new List.


flight_list = list(data.keys())

# print ("Number of Flights:", flight_count(flight_list))

# print (random_flight(flight_list))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="List FlightRadar24 Tracks",
        allow_abbrev='True',
        add_help='True'
    )

    parser.add_argument('-r',
                        '--random',
                        action='store_true',
                        help='List Random Flight')
    parser.add_argument('-l',
                        '--list',
                        action='store_true',
                        help='List of Current Flights')

    parser.add_argument('--debug',
                        action='store_true',
                        help='Debug: List Flights List')

    parser.add_argument('--stats',
                        action='store_true',
                        help='Show Stats on Next Data Pull')

    args = parser.parse_args()

# print(args)

if args.random:
    print(random_flight(flight_list))
elif args.list:
    all_flights(flight_list)
elif args.debug:
    debug(flight_list)
elif args.stats:
    show_stats(data_stats)

# print (type(data.get('1f89480e')))

# Get a random flight from the flight list
# and pull the flight information from data.


# Description of information from each flight
# 0 - Mode S
# 1 - Latitude
# 2 - Longitude
# 3 - Heading
# 4 - Altitude
# 5 - Speed/Knots
# 6
# 7
# 8 - Type Code
# 9 - Registration
# 10
# 11 - Source Airport Code
# 12 - Destination Airport Code
# 13 - Flight # Airline/Operator
# 14 - Empty
# 15 - Empty
# 16 -
# 17 - Empty
# 18 - Country Code
