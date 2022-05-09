package de.hpi.osm.planpro.generator;

import java.util.ArrayList;
import java.util.Random;

public class Route {
	private final String routeUUID;
	private final int nameRoute;
	private final ArrayList<Edge> edges;

	public Route(final ArrayList<Edge> edges) {
		this.routeUUID = Generator.getRandomUUID();

		final Random r = new Random();
		this.nameRoute = r.nextInt(9000) + 1000;

		this.edges = edges;
	}

	public String getRouteUUID() {
		return this.routeUUID;
	}

	public int getNameRoute() {
		return this.nameRoute;
	}

	public ArrayList<Edge> getEdges() {
		return this.edges;
	}

	public double getLength() {
		return this.edges.stream().map(edge -> edge.getLength()).reduce(0.0, Double::sum);
	}
}
