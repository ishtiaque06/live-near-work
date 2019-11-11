import requests
from bs4 import BeautifulSoup
import csv
import optparse
import googlemaps

def main():
    # with open('zillow.key', 'r') as file:
    #     key = file.readline().rstrip('\n')
    # url = "https://www.zillow.com/webservice/GetRegionChildren.htm"
    # state = "ma"
    # city = "boston"
    # childtype = "neighborhood"
    # url = url + '?zws-id=' + key + '&state=' + state \
    #         + '&city=' + city + "&childtype=" + childtype
    #
    # response = requests.request("GET", url)
    #
    # soup = BeautifulSoup(response.text, 'xml')

    here = {}
    with open('1_bedroom_rent.csv', newline='') as csvfile:
        n_reader = csv.reader(csvfile, delimiter=',')
        for row in n_reader:
            if row[1] == 'Boston':
                here[f"{row[0]}, {row[1]}, {row[2]}"] = row[-1]

    # print(len(hello))
    print(here)
    # for item in hello:
        # print(item in here)


if __name__ == '__main__':
    main()
