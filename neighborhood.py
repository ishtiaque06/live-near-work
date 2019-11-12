import googlemaps


class Neighborhood:

    def __init__(self, name, price, workplace, maps_client):
        self.name = name
        self.price = price
        self.workplace = workplace
        self.client = maps_client
        self.duration = None

    def find_transit_duration(self):
        if not self.duration:
            response = self.client.directions(
                self.name,
                self.workplace,
                mode='transit'
            )
            details = response[0]
            paths = details['legs'][0]
            self.duration = paths['duration']['text']
        return self.duration
