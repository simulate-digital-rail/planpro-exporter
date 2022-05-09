package de.hpi.osm.planpro.generator;

import java.util.List;

public class Edge {
	private Node nodeA;
	private Node nodeB;
	private final String geoKanteUUID;
	private final String topKanteUUID;

	public Edge(final Node nodeA, final Node nodeB) {
		this.nodeA = nodeA;
		this.nodeB = nodeB;
		this.geoKanteUUID = Generator.getRandomUUID();
		this.topKanteUUID = Generator.getRandomUUID();
	}

	public Node getNodeA() {
		return this.nodeA;
	}

	public void setNodeA(final Node nodeA) {
		this.nodeA = nodeA;
	}

	public Node getNodeB() {
		return this.nodeB;
	}

	public void setNodeB(final Node nodeB) {
		this.nodeB = nodeB;
	}

	public boolean isNodeConnected(final Node node) {
		return this.getNodeA().equals(node) || this.getNodeB().equals(node);
	}

	public Node getOtherNode(final Node node) {
		if (this.getNodeA().equals(node)) {
			return this.getNodeB();
		}
		return this.getNodeA();
	}

	public String getGeoKanteUUID() {
		return this.geoKanteUUID;
	}

	public String getTopKanteUUID() {
		return this.topKanteUUID;
	}

	public List<String> getUUIDs() {
		return List.of(this.getGeoKanteUUID(), this.getTopKanteUUID());
	}

	public double getLength() {
		final double minX = Math.min(this.nodeA.getX(), this.nodeB.getX());
		final double maxX = Math.max(this.nodeA.getX(), this.nodeB.getX());
		final double minY = Math.min(this.nodeA.getY(), this.nodeB.getY());
		final double maxY = Math.max(this.nodeA.getY(), this.nodeB.getY());
		return Math.sqrt(Math.pow(maxX - minX, 2) + Math.pow(maxY - minY, 2));
	}
}
