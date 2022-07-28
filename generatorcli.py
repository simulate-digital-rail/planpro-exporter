from planprogenerator import Generator, Node, Edge, Signal
import re


nodes = []
edges = []
signals = []


def find_node_with_identifier(_identifier):
    for _node in nodes:
        if _node.identifier == _identifier:
            return _node
    return None


def find_edge_by_nodes(_node_a, _node_b):
    for _edge in edges:
        if _edge.is_node_connected(_node_a) and _edge.is_node_connected(_node_b):
            return _edge
    return None


print("Welcome to the PlanPro Generator")
print("Usage:")
print("Create a node (end or point): node <id> <x> <y> <description>")
print("Create an edge: edge <node id a> <node id b>")
print("Create a signal: signal <node id from> <node id to> <distance to node from> <function> <kind>")
print("Generate the plan pro file: generate")
print("Exit without generate: exit")
print()

filename = input("Please enter the file name (without suffix): ")

with open(f"{filename}.input", "w") as input_file_output:
    command = ""
    while command != "exit" and command != "generate":
        command = input("#: ")

        is_valid = False
        if command == "":
            continue
        elif re.match(r'^node [a-zA-Z_0-9]+ -?\d+(\.\d+)? -?\d+(\.\d+)?( [a-zA-Z_0-9]+)?$', command):
            splits = command.split(" ")
            identifier = splits[1]
            x = float(splits[2]) + 4533770.0
            y = float(splits[3]) + 5625780.0
            desc = ""
            if len(splits) > 4:
                desc = splits[4]

            if find_node_with_identifier(identifier) is None:
                is_valid = True
                node = Node(identifier, x, y, desc)
                nodes.append(node)
            else:
                print(f"Node with id {identifier} already exists. Please use a different id.")
        elif re.match(r'edge [a-zA-Z_0-9]+ [a-zA-Z_0-9]+', command):
            splits = command.split(" ")
            node_a_id = splits[1]
            node_b_id = splits[2]

            node_a = find_node_with_identifier(node_a_id)
            node_b = find_node_with_identifier(node_b_id)

            if node_a is None:
                print(f"Node with ID {node_a_id} does not exists. Please create it first.")
            elif node_b is None:
                print(f"Node with ID {node_b_id} does not exists. Please create it first.")
            else:
                if find_edge_by_nodes(node_a, node_b) is None:
                    is_valid = True
                    edge = Edge(node_a, node_b)
                    node_a.connected_nodes.append(node_b)
                    node_b.connected_nodes.append(node_a)
                    edges.append(edge)
                else:
                    print(f"The nodes {node_a_id} and {node_b_id} are already connected.")
        elif re.match(r'signal [a-zA-Z_0-9]+ [a-zA-Z_0-9]+ -?\d+(\.\d+)? .+ .+', command):
            splits = command.split(" ")
            node_a_id = splits[1]
            node_b_id = splits[2]
            distance = float(splits[3])
            function = splits[4]
            kind = splits[5]

            if function not in Signal.get_supported_functions():
                print(f"Function {function} is not supported. Choose any from: {Signal.get_supported_functions()}")
                continue
            if kind not in Signal.get_supported_kinds():
                print(f"Kind {kind} is not supported. Choose any from: {Signal.get_supported_kinds()}")
                continue

            node_a = find_node_with_identifier(node_a_id)
            node_b = find_node_with_identifier(node_b_id)
            if node_a is None:
                print(f"Node with ID {node_a_id} does not exists. Please create it first.")
                continue
            if node_b is None:
                print(f"Node with ID {node_b_id} does not exists. Please create it first.")
                continue

            edge = find_edge_by_nodes(node_a, node_b)
            if edge is None:
                print(f"The nodes {node_a_id} and {node_b_id} are not connected. Please connect them first.")
                continue

            if distance > edge.get_length():
                print("Distance is greater than edge length. Choose a smaller distance.")
                continue

            is_valid = True
            effective_direction = "in"
            if edge.node_b.identifier == node_a_id and edge.node_a.identifier == node_b_id:
                effective_direction = "gegen"
                distance = edge.get_length() - distance

            signal = Signal(edge, distance, effective_direction, function, kind)
            signals.append(signal)
        elif command != "generate" and command != "exit":
            print("Command does not exists")

        if is_valid:
            input_file_output.write(f"{command}\n")
    if command == "generate":
        generator = Generator()
        generator.generate(nodes, edges, signals, filename)
        print("Generation completed")
    print("Generator terminates.")
