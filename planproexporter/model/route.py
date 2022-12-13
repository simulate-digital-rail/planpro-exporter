import uuid


class Route(object):

    def __init__(self, v_hg, start_signal):
        self.route_uuid = str(uuid.uuid4())
        self.v_hg = v_hg
        self.edges = set()

        self.start_signal = start_signal
        self.edges.add(start_signal.edge)
        self.end_signal = None

    def get_edges_in_order(self):
        if self.end_signal is None:
            return None

        previous_edge = self.start_signal.edge
        next_node = self.start_signal.get_node_after()
        edges_in_order = [previous_edge]

        while previous_edge is not self.end_signal.edge:
            next_edge = None
            for edge in self.edges:
                if edge.is_node_connected(next_node) and \
                   not edge.is_node_connected(previous_edge.get_other_node(next_node)):
                    next_edge = edge

            edges_in_order.append(next_edge)
            next_node = next_edge.get_other_node(next_node)
            previous_edge = next_edge

        return edges_in_order