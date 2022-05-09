package de.hpi.osm.planpro.generator;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {

	private static ArrayList<Node> nodes = new ArrayList<>();

	private static ArrayList<Edge> edges = new ArrayList<>();

	private static ArrayList<Signal> signals = new ArrayList<>();

	public static void main(final String[] args) {
		System.out.println("Welcome to the PlanPro Generator");
		System.out.println("Usage:");
		System.out.println("Create a node (end or point): node <id> <x> <y> <description>");
		System.out.println("Create an edge: edge <node id a> <node id b>");
		System.out.println(
				"Create a signal: signal <node id from> <node id to> <distance to node from> <function> <kind>");
		System.out.println("Generate the plan pro file: generate");
		System.out.println("Exit without generate: exit");
		System.out.println();
		try (final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in))) {
			System.out.print("Please enter the file name (without suffix): ");
			final String filename = reader.readLine();

			try (final BufferedWriter writer = new BufferedWriter(new FileWriter(filename + ".input"))) {
				String command = "";
				while (!command.equals("generate") && !command.equals("exit")) {
					System.out.print("#: ");
					command = reader.readLine();
					boolean isValid = false;
					if (command.isEmpty()) {
						continue;
					} else if (command.matches("node [a-zA-Z_0-9]+ -?\\d+\\.\\d+ -?\\d+\\.\\d+( [a-zA-Z_0-9]+)?")) {
						final String[] splits = command.split(" ");
						final String id = splits[1];
						// Coordinates + shift in DB.Ref coordinate system
						final double x = Double.parseDouble(splits[2]) + 4533770.0;
						final double y = Double.parseDouble(splits[3]) + 5625780.0;
						String description = "";
						if (splits.length > 4) {
							description = splits[4];
						}
						if (nodes.stream().anyMatch(node -> node.getId().equals(id))) {
							System.out.println("Node with id " + id + " already exists. Please use a different id.");
						} else {
							isValid = true;
							final Node n = new Node(id, x, y, description);
							nodes.add(n);
						}
					} else if (command.matches("edge [a-zA-Z_0-9]+ [a-zA-Z_0-9]+")) {
						final String[] splits = command.split(" ");
						final String nodeAID = splits[1];
						final String nodeBID = splits[2];

						final Node nodeA = nodes.stream().filter(node -> node.getId().equals(nodeAID)).findAny()
								.orElse(null);
						final Node nodeB = nodes.stream().filter(node -> node.getId().equals(nodeBID)).findAny()
								.orElse(null);
						if (nodeA == null) {
							System.out.println("Node with ID " + nodeAID + " does not exists. Please create it first.");
						} else if (nodeB == null) {
							System.out.println("Node with ID " + nodeBID + " does not exists. Please create it first.");
						} else {
							// Edges are bidirectional
							final boolean alreadyConnected = nodeA.getConnectedNodes().stream()
									.anyMatch(connectedNode -> connectedNode.getId().equals(nodeB.getId()));
							if (alreadyConnected) {
								System.out.println(
										"The nodes " + nodeAID + " and " + nodeBID + " are already connected.");
							} else {
								isValid = true;
								final Edge e = new Edge(nodeA, nodeB);
								edges.add(e);
								nodeA.getConnectedNodes().add(nodeB);
								nodeB.getConnectedNodes().add(nodeA);
							}
						}
					} else if (command.matches("signal [a-zA-Z_0-9]+ [a-zA-Z_0-9]+ -?\\d+\\.\\d+ .+ .+")) {
						final String[] splits = command.split(" ");
						final String nodeAID = splits[1];
						final String nodeBID = splits[2];
						double distance = Double.parseDouble(splits[3]);
						final String function = splits[4];
						final String kind = splits[5];
						if (!Signal.supportedFunctions.contains(function)) {
							System.out.println("Function \"" + function + "\" is not supported. Choose any from "
									+ String.join(",", Signal.supportedFunctions));
						} else if (!Signal.supportedKinds.contains(kind)) {
							System.out.println("Kind \"" + kind + "\" is not supported. Choose any from "
									+ String.join(",", Signal.supportedKinds));
						} else {
							final Node nodeA = nodes.stream().filter(node -> node.getId().equals(nodeAID)).findAny()
									.orElse(null);
							final Node nodeB = nodes.stream().filter(node -> node.getId().equals(nodeBID)).findAny()
									.orElse(null);
							if (nodeA == null) {
								System.out.println(
										"Node with ID " + nodeAID + " does not exists. Please create it first.");
							} else if (nodeB == null) {
								System.out.println(
										"Node with ID " + nodeBID + " does not exists. Please create it first.");
							} else {
								final Edge edge = edges.stream()
										.filter(e -> e.getNodeA().equals(nodeA) && e.getNodeB().equals(nodeB)
												|| e.getNodeA().equals(nodeB) && e.getNodeB().equals(nodeA))
										.findAny().orElse(null);
								if (edge == null) {
									System.out.println("Node " + nodeAID + " and node " + nodeBID
											+ " are not connected. Create edge first.");
								} else {
									if (distance > edge.getLength()) {
										System.out.println(
												"Distance is greater than edge length. Choose a smaller distance.");
									} else {
										isValid = true;
										String effectiveDirection = "in";
										if (edge.getNodeA().equals(nodeB) && edge.getNodeB().equals(nodeA)) {
											effectiveDirection = "gegen";
											distance = edge.getLength() - distance;
										}
										final Signal signal = new Signal(null, edge, distance, effectiveDirection,
												function, kind);
										signals.add(signal);
									}
								}
							}
						}

					} else if (!command.equals("generate") && !command.equals("exit")) {
						System.out.println("Command does not exists.");
					}

					if (isValid) {
						writer.write(command + "\n");
					}
				}
				if (command.equals("generate")) {
					final ArrayList<Route> routes = new ArrayList<>();
					final Route route = new Route(edges);
					signals.forEach(signal -> signal.setRoute(route));
					routes.add(route);

					final ArrayList<RunningTrack> runningTracks = RunningTrack.generateRunningTracks(nodes, edges,
							signals);

					final Generator g = new Generator(nodes, edges, signals, routes, runningTracks);
					g.generate(filename);
					System.out.println("Generation completed");
				}
				System.out.println("Generator terminates.");
			} catch (final IOException e) {
				e.printStackTrace();
			}
		} catch (final IOException e1) {
			e1.printStackTrace();
		}
	}
}
