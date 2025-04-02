from yaramo.model import (
    Edge,
    Node,
    Route,
    Signal,
    SignalDirection,
    SignalFunction,
    SignalKind,
    Topology,
    Wgs84GeoNode,
)
from planproexporter.generator import Generator

topology = Topology()
node_1 = Node(geo_node=Wgs84GeoNode(0, 0), name="n1")
node_2 = Node(geo_node=Wgs84GeoNode(0, 10), name="n2")
node_3 = Node(geo_node=Wgs84GeoNode(10, 0), name="n3")  # Point
node_4 = Node(geo_node=Wgs84GeoNode(20, 0), name="n4")  # Point
node_5 = Node(geo_node=Wgs84GeoNode(30, 0), name="n5")
node_6 = Node(geo_node=Wgs84GeoNode(30, 10), name="n6")
edge_1 = Edge(node_1, node_3)
edge_2 = Edge(node_2, node_3)
edge_3 = Edge(node_3, node_4)
edge_4 = Edge(node_4, node_5)
edge_5 = Edge(node_4, node_6)

# Route 1
signal_1 = Signal(
    edge_1, 5.0, SignalDirection.IN, SignalFunction.Block_Signal, SignalKind.Hauptsignal, name="99N1"
)
edge_1.signals.append(signal_1)
signal_2 = Signal(
    edge_3, 3.0, SignalDirection.IN, SignalFunction.Block_Signal, SignalKind.Hauptsignal, name="99N2"
)
edge_3.signals.append(signal_2)
route_1 = Route(signal_1)
route_1.edges.add(edge_1)
route_1.edges.add(edge_3)
route_1.end_signal = signal_2

# Route 2
signal_3 = Signal(
    edge_3, 7.0, SignalDirection.IN, SignalFunction.Block_Signal, SignalKind.Hauptsignal, name="99N3"
)
edge_3.signals.append(signal_3)
signal_4 = Signal(
    edge_4, 5.0, SignalDirection.IN, SignalFunction.Block_Signal, SignalKind.Hauptsignal, name="99N4"
)
edge_4.signals.append(signal_4)
route_2 = Route(signal_3)
route_2.edges.add(edge_3)
route_2.edges.add(edge_4)
route_2.end_signal = signal_4

# Route 3
signal_5 = Signal(
    edge_4, 3.0, SignalDirection.GEGEN, SignalFunction.Block_Signal, SignalKind.Hauptsignal, name="99N5"
)
edge_4.signals.append(signal_5)
signal_6 = Signal(
    edge_1, 3.0, SignalDirection.GEGEN, SignalFunction.Block_Signal, SignalKind.Hauptsignal, name="99N6"
)
edge_1.signals.append(signal_6)
route_3 = Route(signal_5)
route_3.edges.add(edge_4)
route_3.edges.add(edge_3)
route_3.edges.add(edge_1)
route_3.end_signal = signal_6

topology.add_nodes([node_1, node_2, node_3, node_4, node_5, node_6])
topology.add_edges([edge_1, edge_2, edge_3, edge_4, edge_5])
for edge in topology.edges.values():
    edge.update_length()
topology.add_signals([signal_1, signal_2, signal_3, signal_4, signal_5, signal_6])
topology.add_routes([route_1, route_2, route_3])

# topology is a yaramo.models.Topology object
Generator().generate(topology, author_name="Name", organisation="Organisation", filename="out")
