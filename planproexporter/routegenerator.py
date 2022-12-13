from railwayroutegenerator import generator
from railwayroutegenerator.model import Topology, Node, Edge, Signal
from .model import Route


class RouteGenerator(object):

    def __init__(self, nodes, edges, signals, default_v_hg=120):
        self.nodes = nodes  # Objects from this library
        self.edges = edges  # Objects from this library
        self.signals = signals  # Objects from this library
        self.default_v_hg = default_v_hg
        pass

    def create_topology(self):
        topology = Topology()

        # Transfer nodes
        nodes = dict()
        for node in self.nodes:
            route_node_obj = Node(node.top_node_uuid)
            nodes[node.top_node_uuid] = route_node_obj
            topology.add_node(route_node_obj)

        for node in self.nodes:
            route_node_obj = nodes[node.top_node_uuid]
            if len(node.connected_nodes) == 1:  # It's an end
                route_node_obj.set_connection_head(nodes[node.connected_nodes[0].top_node_uuid])
            else:  # It's an point
                node.calc_anschluss_of_all_nodes()
                route_node_obj.set_connection_head(nodes[node.tip_node.top_node_uuid])
                route_node_obj.set_connection_left(nodes[node.left_node.top_node_uuid])
                route_node_obj.set_connection_right(nodes[node.right_node.top_node_uuid])

        # Transfer edges
        edges = dict()
        for edge in self.edges:
            route_node_a = nodes[edge.node_a.top_node_uuid]
            route_node_b = nodes[edge.node_b.top_node_uuid]
            route_edge_obj = Edge(edge.top_edge_uuid, route_node_a, route_node_b, edge.get_length())
            edges[edge.top_edge_uuid] = route_edge_obj
            topology.add_edge(route_edge_obj)

        # Transfer signals
        for signal in self.signals:
            route_signal_obj = Signal(signal.signal_uuid)
            route_signal_obj.function = signal.function
            route_signal_obj.distance = signal.distance_edge
            route_signal_obj.wirkrichtung = signal.effective_direction

            if signal.effective_direction == "in":
                route_signal_obj.previous_node = nodes[signal.edge.node_a.top_node_uuid]
                route_signal_obj.next_node = nodes[signal.edge.node_b.top_node_uuid]
            else:
                route_signal_obj.previous_node = nodes[signal.edge.node_b.top_node_uuid]
                route_signal_obj.next_node = nodes[signal.edge.node_a.top_node_uuid]

            edges[signal.edge.top_edge_uuid].signals.append(route_signal_obj)
            topology.add_signal(route_signal_obj)

        return topology

    def convert_routes(self, routes_from_route_generator):
        # Converts the railway route generator routes to the planpro generator routes

        def get_signal_by_uuid(uuid):
            for signal in self.signals:
                if signal.signal_uuid == uuid:
                    return signal
            return None

        def get_edge_by_uuid(uuid):
            for edge in self.edges:
                if edge.top_edge_uuid == uuid:
                    return edge
            return None

        routes = []
        for route_route_obj in routes_from_route_generator:
            start_signal = get_signal_by_uuid(route_route_obj.start_signal.uuid)
            if start_signal is None:
                print("Start signal not found")
                continue
            route = Route(self.default_v_hg, start_signal)

            route.edges = set()
            for route_edge_obj in route_route_obj.edges:
                edge = get_edge_by_uuid(route_edge_obj.uuid)
                route.edges.add(edge)

            route.end_signal = get_signal_by_uuid(route_route_obj.end_signal.uuid)
            if route.end_signal is None:
                print("End signal not found")
                continue
            routes.append(route)
        return routes

    def generate_routes(self):
        topology = self.create_topology()
        routes = generator.generate_from_topology(topology, output_format="python-objects")
        return self.convert_routes(routes)
