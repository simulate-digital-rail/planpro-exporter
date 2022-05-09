package de.hpi.osm.planpro.generator;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Node {
	private String id;
	private double x;
	private double y;
	private String description;
	private final ArrayList<Node> connectedNodes;
	private final String geoPunktUUID;
	private final String geoKnotenUUID;
	private final String topKnotenUUID;

	public Node(final String id, final double x, final double y, final String description) {
		this.id = id;
		this.x = x;
		this.y = y;
		this.description = description;
		this.connectedNodes = new ArrayList<>();
		this.geoPunktUUID = Generator.getRandomUUID();
		this.geoKnotenUUID = Generator.getRandomUUID();
		this.topKnotenUUID = Generator.getRandomUUID();
	}

	public String getId() {
		return this.id;
	}

	public void setId(final String id) {
		this.id = id;
	}

	public double getX() {
		return this.x;
	}

	public void setX(final double x) {
		this.x = x;
	}

	public double getY() {
		return this.y;
	}

	public void setY(final double y) {
		this.y = y;
	}

	public String getDescription() {
		return this.description;
	}

	public void setDescription(final String description) {
		this.description = description;
	}

	public ArrayList<Node> getConnectedNodes() {
		return this.connectedNodes;
	}

	public String getGeoPunktUUID() {
		return this.geoPunktUUID;
	}

	public String getGeoKnotenUUID() {
		return this.geoKnotenUUID;
	}

	public String getTopKnotenUUID() {
		return this.topKnotenUUID;
	}

	public List<String> getUUIDs() {
		return List.of(this.getGeoPunktUUID(), this.getGeoKnotenUUID(), this.getTopKnotenUUID());
	}

	public List<Node> getPossibleFollowers(final Node source) {
		// Node is end. If the source is null (no node) the only connected node is a possible follower.
		// Otherwise return an empty list to indicate the end.
		if (this.getConnectedNodes().size() == 1) {
			if (source == null) {
				return this.getConnectedNodes();
			} else {
				return new ArrayList<>();
			}
		}

		// Otherwise its a point.
		try {
			final String anschlussOfSource = this.getAnschlussOfOther(source);
			if (anschlussOfSource.equals("Spitze")) {
				return this.connectedNodes.stream().filter(node -> !node.equals(source)).collect(Collectors.toList());
			}
			for (final Node other : this.connectedNodes) {
				if (!other.equals(source) && this.getAnschlussOfOther(other).equals("Spitze")) {
					return List.of(other);
				}
			}
			return null;
		} catch (final Exception e) {
			e.printStackTrace();
		}
		return null;
	}

	/**
	 * Gets the Anschluss (Ende, Links, Rechts, Spitze) of other node. Idea: We assume, the current node is a point and
	 * we want to estimate the Anschluss of the other node.
	 *
	 * @param other
	 *            the other
	 * @return the anschluss of other
	 * @throws Exception
	 */
	public String getAnschlussOfOther(final Node other) throws IllegalStateException, Exception {
		if (this.getConnectedNodes().size() != 3) {
			throw new IllegalStateException("Try to get Anschluss of Ende (Node ID: " + this.getId() + ")");
		}
		final Node nodeA = this.getConnectedNodes().get(0);
		final Node nodeB = this.getConnectedNodes().get(1);
		final Node nodeC = this.getConnectedNodes().get(2);

		Node spitze = null;
		Node links = null;
		Node rechts = null;

		if (nodeA.getX() > this.getX() && nodeB.getX() > this.getX() && nodeC.getX() < this.getX()
				|| nodeA.getY() > this.getY() && nodeB.getY() > this.getY() && nodeC.getY() < this.getY()
				|| nodeA.getX() < this.getX() && nodeB.getX() < this.getX() && nodeC.getX() > this.getX()
				|| nodeA.getY() < this.getY() && nodeB.getY() < this.getY() && nodeC.getY() > this.getY()) {
			spitze = nodeC;
			links = this.getLinkerAnschluss(nodeA, nodeB);
			rechts = this.getRechterAnschluss(nodeA, nodeB);
		} else if (nodeA.getX() > this.getX() && nodeC.getX() > this.getX() && nodeB.getX() < this.getX()
				|| nodeA.getY() > this.getY() && nodeC.getY() > this.getY() && nodeB.getY() < this.getY()
				|| nodeA.getX() < this.getX() && nodeC.getX() < this.getX() && nodeB.getX() > this.getX()
				|| nodeA.getY() < this.getY() && nodeC.getY() < this.getY() && nodeB.getY() > this.getY()) {
			spitze = nodeB;
			links = this.getLinkerAnschluss(nodeA, nodeC);
			rechts = this.getRechterAnschluss(nodeA, nodeC);
		} else if (nodeC.getX() > this.getX() && nodeB.getX() > this.getX() && nodeA.getX() < this.getX()
				|| nodeC.getY() > this.getY() && nodeB.getY() > this.getY() && nodeA.getY() < this.getY()
				|| nodeC.getX() < this.getX() && nodeB.getX() < this.getX() && nodeA.getX() > this.getX()
				|| nodeC.getY() < this.getY() && nodeB.getY() < this.getY() && nodeA.getY() > this.getY()) {
			spitze = nodeA;
			links = this.getLinkerAnschluss(nodeB, nodeC);
			rechts = this.getRechterAnschluss(nodeB, nodeC);
		} else {
			throw new Exception("Some error occured");
		}

		if (other.equals(spitze)) {
			return "Spitze";
		} else if (other.equals(links)) {
			return "Links";
		} else if (other.equals(rechts)) {
			return "Rechts";
		}
		throw new Exception("Equals-Method failed");
	}

	private Node getLinkerAnschluss(final Node nodeI, final Node nodeJ) throws IOException {
		if (nodeI.getY() > this.getY() && nodeJ.getY() > this.getY()) {
			// Point more or less directed to north
			if (nodeI.getX() < nodeJ.getX()) {
				return nodeI;
			}
			return nodeJ;
		}
		if (nodeI.getY() < this.getY() && nodeJ.getY() < this.getY()) {
			// Point more or less directed to south
			if (nodeI.getX() < nodeJ.getX()) {
				return nodeJ;
			}
			return nodeI;
		}
		if (nodeI.getX() < this.getX() && nodeJ.getX() < this.getX()) {
			// Point more or less directed to west
			if (nodeI.getY() < nodeJ.getY()) {
				return nodeI;
			}
			return nodeJ;
		}
		if (nodeI.getX() > this.getX() && nodeJ.getX() > this.getX()) {
			// Point more or less directed to east
			if (nodeI.getY() < nodeJ.getY()) {
				return nodeJ;
			}
			return nodeI;
		}

		System.out.println("Automatic detection of the point orientation failed.");
		System.out.println("Point " + this.getId() + ": x(" + this.getX() + "), y(" + this.getY() + ")");
		System.out.println("Node1 " + nodeI.getId() + ": x(" + nodeI.getX() + "), y(" + nodeI.getY() + ")");
		System.out.println("Node2 " + nodeJ.getId() + ": x(" + nodeJ.getX() + "), y(" + nodeJ.getY() + ")");
		System.out.print("Which one should be left? (enter 1 or 2)");
		try (BufferedReader reader = new BufferedReader(new InputStreamReader(System.in))) {
			final int oneOrTwo = Integer.parseInt(reader.readLine());
			if (oneOrTwo == 1) {
				return nodeI;
			} else {
				return nodeJ;
			}
		} catch (final IOException e) {
			throw e;
		}
	}

	private Node getRechterAnschluss(final Node nodeI, final Node nodeJ) throws IOException {
		final Node linkerAnschluss = this.getLinkerAnschluss(nodeI, nodeJ);
		if (linkerAnschluss.equals(nodeI)) {
			return nodeJ;
		}
		return nodeI;
	}

	@Override
	public boolean equals(final Object obj) {
		if (this == obj) {
			return true;
		}
		if (obj == null) {
			return false;
		}
		if (this.getClass() != obj.getClass()) {
			return false;
		}
		final Node other = (Node) obj;
		if (this.id == null) {
			if (other.id != null) {
				return false;
			}
		} else if (!this.id.equals(other.id)) {
			return false;
		}
		return true;
	}

	@Override
	public String toString() {
		return this.getId();
	}

}
