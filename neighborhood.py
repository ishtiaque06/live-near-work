import googlemaps


class Neighborhood:

    def __init__(self, name, price, workplace, maps_client):
        self.name = name
        self.price = price
        self.workplace = workplace
        self.client = maps_client
        self._duration = None

    @property
    def duration(self):
        if not self._duration:
            return self.find_transit_duration()
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value

    def find_transit_duration(self):
        response = self.client.directions(
            self.name,
            self.workplace,
            mode='transit'
        )
        details = response[0]
        paths = details['legs'][0]
        self._duration = paths['duration']['text']
        return self.duration
