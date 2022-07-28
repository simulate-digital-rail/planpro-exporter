import uuid
import random


class Trip(object):

    def __init__(self, edges):
        self.trip_uuid = str(uuid.uuid4())
        self.trip_name = random.randrange(1000, 10000)
        self.edges = edges

    def get_length(self):
        total_length = 0.0
        for edge in self.edges:
            total_length = total_length + edge.get_length()
        return total_length
