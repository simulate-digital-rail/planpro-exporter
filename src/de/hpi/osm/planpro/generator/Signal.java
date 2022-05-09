package de.hpi.osm.planpro.generator;

import java.util.HashSet;
import java.util.List;
import java.util.Random;

public class Signal {

	public static List<String> supportedFunctions = List.of("Einfahr_Signal", "Ausfahr_Signal", "andere");
	public static List<String> supportedKinds = List.of("Hauptsignal", "Mehrabschnittssignal", "Vorsignal",
			"Sperrsignal", "Hauptsperrsignal", "andere");

	private String signalUUID;
	private Route route;
	private Edge edge;
	private double distanceEdge;
	private String effectiveDirection;
	private String classificationNumber;
	private String elementName;
	private String controlMemberUUID;
	private String function;
	private String kind;

	public Signal(final Route route, final Edge edge, final double distanceEdge, final String effectiveDirection,
			final String function, final String kind) {
		this.signalUUID = Generator.getRandomUUID();
		this.route = route;
		this.edge = edge;
		this.distanceEdge = distanceEdge;
		this.effectiveDirection = effectiveDirection;
		this.classificationNumber = "60";
		this.elementName = this.getRandomElementName();
		this.controlMemberUUID = Generator.getRandomUUID();
		this.function = function;
		this.kind = kind;
	}

	public String getSignalUUID() {
		return this.signalUUID;
	}

	public void setSignalUUID(final String signalUUID) {
		this.signalUUID = signalUUID;
	}

	public Route getRoute() {
		return this.route;
	}

	public void setRoute(final Route route) {
		this.route = route;
	}

	public Edge getEdge() {
		return this.edge;
	}

	public void setEdge(final Edge edge) {
		this.edge = edge;
	}

	public Node getNodeBefore() {
		if (this.getEffectiveDirection().toLowerCase().equals("in")) {
			return this.getEdge().getNodeA();
		}
		return this.getEdge().getNodeB();
	}

	public Node getNodeAfter() {
		if (this.getEffectiveDirection().toLowerCase().equals("in")) {
			return this.getEdge().getNodeB();
		}
		return this.getEdge().getNodeA();
	}

	public double getDistanceEdge() {
		return this.distanceEdge;
	}

	public void setDistanceEdge(final double distanceEdge) {
		this.distanceEdge = distanceEdge;
	}

	public String getEffectiveDirection() {
		return this.effectiveDirection;
	}

	public void setEffectiveDirection(final String effectiveDirection) {
		this.effectiveDirection = effectiveDirection;
	}

	public double getSideDistance() {
		if (this.getEffectiveDirection().toLowerCase().equals("in")) {
			return 3.950;
		}
		return -3.950;
	}

	public String getClassificationNumber() {
		return this.classificationNumber;
	}

	public void setClassificationNumber(final String classificationNumber) {
		this.classificationNumber = classificationNumber;
	}

	public String getElementName() {
		return this.elementName;
	}

	public void setElementName(final String elementName) {
		this.elementName = elementName;
	}

	public String getControlMemberUUID() {
		return this.controlMemberUUID;
	}

	public void setControlMemberUUID(final String controlElementUUID) {
		this.controlMemberUUID = controlElementUUID;
	}

	public String getFunction() {
		return this.function;
	}

	public void setFunction(final String function) {
		this.function = function;
	}

	public String getKind() {
		return this.kind;
	}

	public void setKind(final String kind) {
		this.kind = kind;
	}

	public List<String> getUUIDs() {
		return List.of(this.signalUUID, this.controlMemberUUID);
	}

	private static HashSet<String> usedElementNames = new HashSet<>();

	private String getRandomElementName() {
		String elementName = this.getRandomChar() + this.getRandomChar();
		while (usedElementNames.contains(elementName)) {
			elementName = this.getRandomChar() + this.getRandomChar();
		}
		usedElementNames.add(elementName);
		return elementName;
	}

	private String getRandomChar() {
		final Random r = new Random();
		return "" + (char) (r.nextInt('Z' - 'A' + 1) + 'A');
	}
}
