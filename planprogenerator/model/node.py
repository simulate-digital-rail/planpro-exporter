import uuid
import math
from decimal import Decimal
from .geonode import GeoNode


class Node(object):

    def __init__(self, identifier, x, y, desc):
        self.identifier = identifier
        self.desc = desc
        self.connected_nodes = []
        self.geo_node = GeoNode(x, y)
        self.top_node_uuid = str(uuid.uuid4())

        self.tip_node = None
        self.left_node = None
        self.right_node = None

    def is_node_connected(self, node):
        for connected_node in self.connected_nodes:
            if connected_node.identifier == node.identifier:
                return True
        return False

    def set_tip_node(self, node):
        if self.is_node_connected(node):
            self.tip_node = node
        else:
            raise ValueError("Can not set unconnected node as tip node. Connect the node first by creating an edge.")

    def set_left_node(self, node):
        if self.is_node_connected(node):
            self.left_node = node
        else:
            raise ValueError("Can not set unconnected node as left node. Connect the node first by creating an edge.")

    def set_right_node(self, node):
        if self.is_node_connected(node):
            self.right_node = node
        else:
            raise ValueError("Can not set unconnected node as right node. Connect the node first by creating an edge.")

    def get_uuids(self):
        return [self.top_node_uuid]

    def get_possible_successors(self, source):
        if len(self.connected_nodes) == 1:
            # Node is an end. If the source is None, the only connected node is a possible successor.
            # Otherwise, the returned list is empty.
            if source is None:
                return self.connected_nodes
            return []

        # Otherwise, it's a point.
        if self.tip_node is None or self.left_node is None or self.right_node is None:
            self.calc_anschluss_of_all_nodes()

        if source.identifier == self.tip_node.identifier:
            return [self.left_node, self.right_node]
        return [self.tip_node]

    def get_anschluss_of_other(self, other):
        #  Gets the Anschluss (Ende, Links, Rechts, Spitze) of other node. Idea: We assume, the current node is a point
        #  and we want to estimate the Anschluss of the other node.
        if len(self.connected_nodes) != 3:
            print(f"Try to get Anschluss of Ende (Node ID: {self.identifier})")
            return None

        if self.tip_node is None or self.left_node is None or self.right_node is None:
            self.calc_anschluss_of_all_nodes()

        if other.identifier == self.tip_node.identifier:
            return "Spitze"
        if other.identifier == self.left_node.identifier:
            return "Links"
        if other.identifier == self.right_node.identifier:
            return "Rechts"
        return None

    def calc_anschluss_of_all_nodes(self):

        def get_arc_between_nodes(_node_a, _node_b):
            def length_of_side(__node_a, __node_b):
                pi_over_180  = Decimal(math.pi/180)
                return 2 * 6371000 * math.asin(
                    math.pi/180*math.sqrt(
                    math.pow(math.sin((pi_over_180*(__node_b.geo_node.x - __node_a.geo_node.x))/2),2)+
                    math.cos(pi_over_180*__node_a.geo_node.x)*
                    math.cos(pi_over_180*__node_b.geo_node.x)*
                    math.pow(math.sin((pi_over_180*(__node_b.geo_node.y - __node_a.geo_node.y))/2),2)
                    )
                )

            _a = length_of_side(_node_a, self)
            _b = length_of_side(self, _node_b)
            _c = length_of_side(_node_a, _node_b)

            return math.degrees(math.acos((_a * _a + _b * _b - _c * _c) / (2.0 * _a * _b)))

        current_max_arc = 361
        other_a = None
        other_b = None
        for i in range(len(self.connected_nodes)):
            for j in range(len(self.connected_nodes)):
                if i != j:
                    cur_arc = get_arc_between_nodes(self.connected_nodes[i], self.connected_nodes[j])
                    if cur_arc < current_max_arc:
                        missing_index = sum(range(len(self.connected_nodes))) - (i + j)
                        self.tip_node = self.connected_nodes[missing_index]
                        other_a = self.connected_nodes[i]
                        other_b = self.connected_nodes[j]
                        current_max_arc = cur_arc

        # TODO: Replace this heuristic to determine which node is left and which is right with some suitable algorithm
        if other_a.geo_node.x < self.geo_node.x and other_b.geo_node.x < self.geo_node.x:
            if other_a.geo_node.y < other_b.geo_node.y:
                self.left_node = other_a
                self.right_node = other_b
            else:
                self.left_node = other_b
                self.right_node = other_a
        elif other_a.geo_node.x >= self.geo_node.x and other_b.geo_node.x >= self.geo_node.x:
            if other_a.geo_node.y >= other_b.geo_node.y:
                self.left_node = other_a
                self.right_node = other_b
            else:
                self.left_node = other_b
                self.right_node = other_a
        elif other_a.geo_node.y < self.geo_node.y and other_b.geo_node.y < self.geo_node.y:
            if other_a.geo_node.x >= other_b.geo_node.x:
                self.left_node = other_a
                self.right_node = other_b
            else:
                self.left_node = other_b
                self.right_node = other_a
        elif other_a.geo_node.y >= self.geo_node.y and other_b.geo_node.y >= self.geo_node.y:
            if other_a.geo_node.x < other_b.geo_node.x:
                self.left_node = other_a
                self.right_node = other_b
            else:
                self.left_node = other_b
                self.right_node = other_a
        else:  # If all cases fail, assign more or less randomly.
            self.left_node = other_a
            self.right_node = other_b
