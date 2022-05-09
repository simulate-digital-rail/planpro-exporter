package de.hpi.osm.planpro.generator;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class RunningTrack {

	private String runningTrackUUID;
	private final HashSet<Edge> edges;
	private int vHG;
	private Signal startSignal;
	private Signal endSignal;

	public RunningTrack(final int vHG, final Signal startSignal) {
		this.runningTrackUUID = Generator.getRandomUUID();
		this.vHG = vHG;
		this.edges = new HashSet<>();

		this.startSignal = startSignal;
		this.edges.add(startSignal.getEdge());
		this.endSignal = null;
	}

	public String getRunningTrackUUID() {
		return this.runningTrackUUID;
	}

	public void setRunningTrackUUID(final String runningTrackUUID) {
		this.runningTrackUUID = runningTrackUUID;
	}

	public void addEdge(final Edge edge) {
		this.edges.add(edge);
	}

	public HashSet<Edge> getEdges() {
		return this.edges;
	}

	public List<Edge> getEdgesInOrder() {
		if (this.getEndSignal() == null) {
			return null;
		}
		final List<Edge> edgesInOrder = new ArrayList<>();
		Edge previousEdge = this.getStartSignal().getEdge();
		Node nextNode = this.getStartSignal().getNodeAfter();
		edgesInOrder.add(this.getStartSignal().getEdge());
		while (!previousEdge.equals(this.getEndSignal().getEdge())) {
			final Node nextNodeFinal = nextNode;
			final Edge previousEdgeFinal = previousEdge;
			final Edge nextEdge = this.getEdges().stream().filter(edge -> edge.isNodeConnected(nextNodeFinal)
					&& !edge.isNodeConnected(previousEdgeFinal.getOtherNode(nextNodeFinal))).findFirst().get();
			edgesInOrder.add(nextEdge);
			nextNode = nextEdge.getOtherNode(nextNode);
			previousEdge = nextEdge;
		}
		return edgesInOrder;
	}

	public int getvHG() {
		return this.vHG;
	}

	public void setvHG(final int vHG) {
		this.vHG = vHG;
	}

	public Signal getStartSignal() {
		return this.startSignal;
	}

	public void setStartSignal(final Signal startSignal) {
		this.startSignal = startSignal;
	}

	public Signal getEndSignal() {
		return this.endSignal;
	}

	public void setEndSignal(final Signal endSignal) {
		this.endSignal = endSignal;
		if (endSignal != null) {
			this.edges.add(endSignal.getEdge());
		}
	}

	public List<String> getUUIDs() {
		return List.of(this.getRunningTrackUUID());
	}

	public RunningTrack duplicate() {
		final RunningTrack newTrack = new RunningTrack(this.getvHG(), this.getStartSignal());
		newTrack.setEndSignal(this.getEndSignal());
		for (final Edge edge : this.getEdges()) {
			newTrack.getEdges().add(edge);
		}
		return newTrack;
	}

	public static ArrayList<RunningTrack> generateRunningTracks(final ArrayList<Node> nodes,
			final ArrayList<Edge> edges, final ArrayList<Signal> signals) {
		final ArrayList<RunningTrack> tracks = new ArrayList<>();

		for (final Signal startSignal : signals) {
			if (startSignal.getFunction().equals("Einfahr_Signal")) {
				final RunningTrack track = new RunningTrack(120, startSignal);
				final Node nextNode = startSignal.getNodeAfter();
				tracks.addAll(dfs(nextNode, startSignal.getNodeBefore(), track, edges, signals));
			}
		}

		return tracks;
	}

	private static List<RunningTrack> dfs(final Node currentNode, final Node previousNode,
			final RunningTrack currentTrack, final List<Edge> edges, final List<Signal> signals) {
		final List<Node> connectedNodes = currentNode.getPossibleFollowers(previousNode);
		if (connectedNodes == null || connectedNodes.isEmpty()) {
			return new ArrayList<>();
		}

		final ArrayList<RunningTrack> tracks = new ArrayList<>();
		for (final Node connectedNode : connectedNodes) {
			final Edge edge = getEdgeFromTo(edges, currentNode, connectedNode);
			if (edge == null) {
				System.out.println("Bad error, edge not found, datstructure broken.");
				continue;
			}
			final RunningTrack trackWithEdge = currentTrack.duplicate();
			trackWithEdge.addEdge(edge);

			final List<Signal> signalsAtEdge = getSignalsAtEdge(edge, signals);
			for (final Signal signal : signalsAtEdge) {
				if (signal.getFunction().equals("Ausfahr_Signal")) {
					final RunningTrack closedTrack = trackWithEdge.duplicate();
					closedTrack.setEndSignal(signal);
					tracks.add(closedTrack);
				}
			}
			tracks.addAll(dfs(connectedNode, currentNode, trackWithEdge, edges, signals));
		}

		return tracks;
	}

	private static List<Signal> getSignalsAtEdge(final Edge edge, final List<Signal> signals) {
		final List<Signal> foundSignals = new ArrayList<>();
		for (final Signal signal : signals) {
			if (signal.getEdge().equals(edge)) {
				foundSignals.add(signal);
			}
		}
		return foundSignals;
	}

	private static Edge getEdgeFromTo(final List<Edge> edges, final Node from, final Node to) {
		if (from.equals(to)) {
			return null;
		}
		return edges.stream().filter(edge -> edge.isNodeConnected(from) && edge.isNodeConnected(to)).findFirst()
				.orElse(null);
	}
}
