package de.hpi.osm.planpro.generator;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.UUID;

public class Generator {
	private final ArrayList<Node> nodes;

	private final ArrayList<Edge> edges;

	private final ArrayList<Signal> signals;

	private final ArrayList<Route> routes;

	private final ArrayList<RunningTrack> runningTracks;

	private final ArrayList<String> geoKanten;
	private final ArrayList<String> topKanten;
	private final ArrayList<String> geoKnoten;
	private final ArrayList<String> geoPunkte;
	private final ArrayList<String> topKnoten;
	private final ArrayList<String> signale;
	private final ArrayList<String> stellelemente;
	private final ArrayList<String> strecken;
	private final ArrayList<String> fstrFahrwege;

	public Generator(final ArrayList<Node> nodes, final ArrayList<Edge> edges, final ArrayList<Signal> signals,
			final ArrayList<Route> routes, final ArrayList<RunningTrack> runningTracks) {
		this.nodes = nodes;
		this.edges = edges;
		this.signals = signals;
		this.routes = routes;
		this.runningTracks = runningTracks;
		this.geoKnoten = new ArrayList<>();
		this.geoPunkte = new ArrayList<>();
		this.topKnoten = new ArrayList<>();
		this.geoKanten = new ArrayList<>();
		this.topKanten = new ArrayList<>();
		this.signale = new ArrayList<>();
		this.stellelemente = new ArrayList<>();
		this.strecken = new ArrayList<>();
		this.fstrFahrwege = new ArrayList<>();
	}

	public void generate(final String filename) {
		try (BufferedWriter writer = new BufferedWriter(new FileWriter(filename + ".ppxml"))) {
			final ArrayList<String> uuids = new ArrayList<>();
			Boilerplate.generatePrefix(writer);

			final String aussenUUID = Boilerplate.generateAussenelementansteuerung(writer);
			uuids.add(aussenUUID);

			uuids.addAll(this.generateNodes(this.nodes));
			uuids.addAll(this.generateEdges(this.edges));
			uuids.addAll(this.generateSignals(this.signals));
			uuids.addAll(this.generateRoutes(this.routes));
			uuids.addAll(this.generateRunningTracks(this.runningTracks));

			// Order of elements in XML is relevant! (Probably alphabetical)
			this.writeArrayList(writer, this.fstrFahrwege);
			this.writeArrayList(writer, this.geoKanten);
			this.writeArrayList(writer, this.geoKnoten);
			this.writeArrayList(writer, this.geoPunkte);
			this.writeArrayList(writer, this.signale);
			this.writeArrayList(writer, this.stellelemente);
			this.writeArrayList(writer, this.strecken);
			this.writeArrayList(writer, this.topKanten);
			this.writeArrayList(writer, this.topKnoten);

			final String unterbringungUUID = Boilerplate.generateUnterbringung(writer);
			uuids.add(unterbringungUUID);

			Boilerplate.generateSuffix(writer, uuids);
		} catch (final IOException e) {
			e.printStackTrace();
		}
	}

	private ArrayList<String> generateNodes(final ArrayList<Node> nodes) {
		final ArrayList<String> uuids = new ArrayList<>();

		for (final Node node : nodes) {
			uuids.addAll(node.getUUIDs());

			this.geoKnoten.add(
					String.format(NodeTemplates.getGeoKnotenTempate(), node.getId(), node.getGeoKnotenUUID()) + "\n");
			this.geoPunkte.add(String.format(NodeTemplates.getGeoPunktTemplate(), node.getId(), node.getGeoPunktUUID(),
					node.getX(), node.getY(), node.getGeoKnotenUUID()) + "\n");
			this.topKnoten.add(String.format(NodeTemplates.getTopKnotenTempate(), node.getId(), node.getTopKnotenUUID(),
					node.getGeoKnotenUUID()) + "\n");
		}

		return uuids;
	}

	private ArrayList<String> generateEdges(final ArrayList<Edge> edges) {
		final ArrayList<String> uuids = new ArrayList<>();

		try {
			for (final Edge edge : edges) {
				final String anschlussA = edge.getNodeA().getConnectedNodes().size() == 1 ? "Ende"
						: edge.getNodeA().getAnschlussOfOther(edge.getNodeB());
				final String anschlussB = edge.getNodeB().getConnectedNodes().size() == 1 ? "Ende"
						: edge.getNodeB().getAnschlussOfOther(edge.getNodeA());

				final String topKante = String.format(EdgeTemplates.getTopKanteTemplate(), edge.getNodeA().getId(),
						edge.getNodeB().getId(), edge.getTopKanteUUID(), edge.getNodeA().getTopKnotenUUID(),
						edge.getNodeB().getTopKnotenUUID(), anschlussA, anschlussB, edge.getLength());
				final String geoKante = String.format(EdgeTemplates.getGeoKanteTemplate(), edge.getNodeA().getId(),
						edge.getNodeB().getId(), edge.getGeoKanteUUID(), edge.getLength(), edge.getTopKanteUUID(),
						edge.getNodeA().getGeoKnotenUUID(), edge.getNodeB().getGeoKnotenUUID());

				uuids.addAll(edge.getUUIDs());
				this.topKanten.add(topKante + "\n");
				this.geoKanten.add(geoKante + "\n");
			}
		} catch (final Exception e) {
			e.printStackTrace();
		}

		return uuids;
	}

	private ArrayList<String> generateSignals(final ArrayList<Signal> signals) {
		final ArrayList<String> uuids = new ArrayList<>();

		for (final Signal signal : signals) {
			final String controlMember = String.format(SignalTemplates.getControllMemberTemplate(),
					signal.getControlMemberUUID());

			final String nameLong = signal.getClassificationNumber() + signal.getElementName();
			final String routeLength = String.format("%.3f", signal.getRoute().getLength() / 1000).replaceAll("\\.",
					",");
			final String signalCode = String.format(SignalTemplates.getSignalTemplate(), signal.getSignalUUID(),
					signal.getRoute().getRouteUUID(), routeLength, signal.getDistanceEdge(),
					signal.getEdge().getTopKanteUUID(), signal.getEffectiveDirection(), signal.getSideDistance(),
					nameLong, signal.getElementName(), nameLong, nameLong, signal.getClassificationNumber(),
					signal.getElementName(), signal.getControlMemberUUID(), signal.getFunction(), signal.getKind());

			uuids.addAll(signal.getUUIDs());
			this.stellelemente.add(controlMember);
			this.signale.add(signalCode);
		}

		return uuids;
	}

	private ArrayList<String> generateRoutes(final ArrayList<Route> routes) {
		final ArrayList<String> uuids = new ArrayList<>();

		for (final Route route : routes) {
			final ArrayList<String> parts = new ArrayList<>();
			for (final Edge edge : route.getEdges()) {
				final String part = String.format(RouteTemplates.getTeilbereichTemplate(), edge.getLength(),
						edge.getTopKanteUUID());
				parts.add(part);
			}

			final String strecke = String.format(RouteTemplates.getStreckeTemplate(), route.getRouteUUID(),
					String.join("", parts), route.getNameRoute());

			uuids.add(route.getRouteUUID());
			this.strecken.add(strecke);
		}

		return uuids;
	}

	private ArrayList<String> generateRunningTracks(final ArrayList<RunningTrack> runningTracks) {
		final ArrayList<String> uuids = new ArrayList<>();

		for (final RunningTrack track : runningTracks) {
			if (track.getEndSignal() == null) {
				continue;
			}

			final Edge startEdge = track.getStartSignal().getEdge();
			final Edge endEdge = track.getEndSignal().getEdge();
			final ArrayList<String> edgesCode = new ArrayList<>();
			// Start edge
			double startStartDistance = 0.0;
			double startEndDistance = 0.0;
			if (track.getStartSignal().getEffectiveDirection().equals("in")) {
				startStartDistance = track.getStartSignal().getDistanceEdge();
				startEndDistance = track.getStartSignal().getEdge().getLength();
			} else {
				startStartDistance = track.getStartSignal().getDistanceEdge();
				startEndDistance = 0.0;
			}
			edgesCode.add(String.format(RunningTrackTemplates.getTeilbereichTemplate(), startEdge.getNodeA(),
					startEdge.getNodeB(), startStartDistance, startEndDistance, startEdge.getTopKanteUUID()));

			// All other edges
			for (final Edge edge : track.getEdgesInOrder()) {
				if (!edge.equals(startEdge) && !edge.equals(endEdge)) {
					edgesCode.add(String.format(RunningTrackTemplates.getTeilbereichTemplate(), edge.getNodeA(),
							edge.getNodeB(), 0.0, edge.getLength(), edge.getTopKanteUUID()));
				}
			}

			// End edge
			double endStartDistance = 0.0;
			double endEndDistance = 0.0;
			if (track.getEndSignal().getEffectiveDirection().equals("in")) {
				endStartDistance = 0.0;
				endEndDistance = track.getEndSignal().getDistanceEdge();
			} else {
				endStartDistance = track.getEndSignal().getEdge().getLength();
				endEndDistance = track.getEndSignal().getDistanceEdge();
			}
			edgesCode.add(String.format(RunningTrackTemplates.getTeilbereichTemplate(), endEdge.getNodeA(),
					endEdge.getNodeB(), endStartDistance, endEndDistance, endEdge.getTopKanteUUID()));

			final String fahrweg = String.format(RunningTrackTemplates.getFstrFahrwegTemplate(),
					track.getRunningTrackUUID(), String.join("", edgesCode), track.getvHG(),
					track.getStartSignal().getSignalUUID(), track.getStartSignal().getElementName(),
					track.getEndSignal().getSignalUUID(), track.getEndSignal().getElementName());
			uuids.addAll(track.getUUIDs());
			this.fstrFahrwege.add(fahrweg);
		}

		return uuids;
	}

	private void writeArrayList(final BufferedWriter writer, final ArrayList<String> strings) throws IOException {
		for (final String s : strings) {
			writer.write(s);
		}
	}

	public static String getRandomUUID() {
		return UUID.randomUUID().toString().toUpperCase();
	}

}
