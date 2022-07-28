import uuid
import math


class Edge(object):

    def __init__(self, node_a, node_b):
        self.node_a = node_a
        self.node_b = node_b
        self.geo_edge_uuid = str(uuid.uuid4())
        self.top_edge_uuid = str(uuid.uuid4())

    def is_node_connected(self, other_node):
        return self.node_a == other_node or self.node_b == other_node

    def get_other_node(self, node):
        if self.node_a == node:
            return self.node_b
        return self.node_a

    def get_uuids(self):
        return [self.geo_edge_uuid, self.top_edge_uuid]

    def get_length(self):
        min_x = min(self.node_a.x, self.node_b.x)
        min_y = min(self.node_a.y, self.node_b.y)
        max_x = max(self.node_a.x, self.node_b.x)
        max_y = max(self.node_a.y, self.node_b.y)
        return math.sqrt(math.pow(max_x - min_x, 2) + math.pow(max_y - min_y, 2))
