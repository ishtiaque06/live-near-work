import requests
from bs4 import BeautifulSoup
import csv
import optparse
def main():
    url = "https://www.zillow.com/webservice/GetRegionChildren.htm?zws-id=X1-ZWz1hgt8bigpvv_2ca3z&state=ma&city=boston&childtype=neighborhood"

    response = requests.request("GET", url)

    soup = BeautifulSoup(response.text, 'xml')

    hello = {item.string for item in soup.find_all('name')}
    # [print(item.string) for item in soup.find_all('longitude')]
    # [print(item.string) for item in soup.find_all('latitude')]

    here = {}
    with open('1_bedroom_rent.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            if row[1] == 'Boston':
                here[row[0]] = row[-1]

    print(len(hello))
    print(here)
    print(len(here))
    # for item in hello:
        # print(item in here)


if __name__ == '__main__':
    main()
