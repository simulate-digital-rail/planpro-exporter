import uuid
import math
from decimal import Decimal

class Edge(object):

    def __init__(self, node_a, node_b):
        self.node_a = node_a
        self.node_b = node_b
        self.intermediate_geo_nodes = []
        self.top_edge_uuid = str(uuid.uuid4())

    def is_node_connected(self, other_node):
        return self.node_a == other_node or self.node_b == other_node

    def get_other_node(self, node):
        if self.node_a == node:
            return self.node_b
        return self.node_a

    def get_uuids(self):
        return [self.top_edge_uuid]

    def get_length(self):
        geo_node_a = self.node_a.geo_node
        geo_node_b = self.node_b.geo_node
        pi_over_180  = Decimal(math.pi/180)
        return 2 * 6371000 * math.asin(
            math.pi/180*math.sqrt(
                math.pow(math.sin((pi_over_180*(geo_node_b.x - geo_node_a.x))/2),2)+
                math.cos(pi_over_180*geo_node_a.x)*
                math.cos(pi_over_180*geo_node_b.x)*
                math.pow(math.sin((pi_over_180*(geo_node_b.y - geo_node_a.y))/2),2)
            )
        )
