package de.hpi.osm.planpro.generator;

public class RouteTemplates {

	public static String getStreckeTemplate() {
		// @formatter:off
		return "            <Strecke>"+"\n"
				+"              <Identitaet>"+"\n"
				+"                <Wert>%s</Wert>"+"\n"
				+"              </Identitaet>"+"\n"
				+"              <Basis_Objekt_Allg>"+"\n"
				+"                <Datum_Regelwerk>"+"\n"
				+"                  <Wert>2012-02-24</Wert>"+"\n"
				+"                </Datum_Regelwerk>"+"\n"
				+"              </Basis_Objekt_Allg>"+"\n"
				+"              <Objektreferenzen/>"+"\n"
				+"%s" // Teilbereiche
				+"              <Bezeichnung>"+"\n"
				+"                <Bezeichnung_Strecke>"+"\n"
				+"                  <Wert>%d</Wert>"+"\n"
				+"                </Bezeichnung_Strecke>"+"\n"
				+"              </Bezeichnung>"+"\n"
				+"            </Strecke>"+"\n";
		// @formatter:on
	}

	public static String getTeilbereichTemplate() {
		// @formatter:off
				return "              <Bereich_Objekt_Teilbereich>"+"\n"
						+"                <Begrenzung_A>"+"\n"
						+"                  <Wert>0.000</Wert>"+"\n"
						+"                </Begrenzung_A>"+"\n"
						+"                <Begrenzung_B>"+"\n"
						+"                  <Wert>%.3f</Wert>"+"\n"
						+"                </Begrenzung_B>"+"\n"
						+"                <ID_TOP_Kante>"+"\n"
						+"                  <Wert>%s</Wert>"+"\n"
						+"                </ID_TOP_Kante>"+"\n"
						+"              </Bereich_Objekt_Teilbereich>"+"\n";
				// @formatter:on
	}
}
