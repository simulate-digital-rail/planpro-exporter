package de.hpi.osm.planpro.generator;

public class EdgeTemplates {

	public static String getTopKanteTemplate() {
		//@formatter:off
		return "            <TOP_Kante> <!-- %s to %s -->\n"
				+ "              <Identitaet>\n"
				+ "                <Wert>%s</Wert>\n"
				+ "              </Identitaet>\n"
				+ "              <Basis_Objekt_Allg>\n"
				+ "                <Datum_Regelwerk>\n"
				+ "                  <Wert>2012-02-24</Wert>\n"
				+ "                </Datum_Regelwerk>\n"
				+ "              </Basis_Objekt_Allg>\n"
				+ "              <Objektreferenzen/>\n"
				+ "              <ID_TOP_Knoten_A>\n"
				+ "                <Wert>%s</Wert>\n"
				+ "              </ID_TOP_Knoten_A>\n"
				+ "              <ID_TOP_Knoten_B>\n"
				+ "                <Wert>%s</Wert>\n"
				+ "              </ID_TOP_Knoten_B>\n"
				+ "              <TOP_Kante_Allg>\n"
				+ "                <TOP_Anschluss_A>\n"
				+ "                  <Wert>%s</Wert>\n"
				+ "                </TOP_Anschluss_A>\n"
				+ "                <TOP_Anschluss_B>\n"
				+ "                  <Wert>%s</Wert>\n"
				+ "                </TOP_Anschluss_B>\n"
				+ "                <TOP_Laenge>\n"
				+ "                  <Wert>%.3f</Wert>\n"
				+ "                </TOP_Laenge>\n"
				+ "              </TOP_Kante_Allg>\n"
				+ "            </TOP_Kante>";
		//@formatter:on
	}

	public static String getGeoKanteTemplate() {
		//@formatter:off
		return "            <GEO_Kante> <!-- %s to %s -->\n"
				+ "              <Identitaet>\n"
				+ "                <Wert>%s</Wert>\n"
				+ "              </Identitaet>\n"
				+ "              <Basis_Objekt_Allg>\n"
				+ "                <Datum_Regelwerk>\n"
				+ "                  <Wert>2012-02-24</Wert>\n"
				+ "                </Datum_Regelwerk>\n"
				+ "              </Basis_Objekt_Allg>\n"
				+ "              <Objektreferenzen/>\n"
				+ "              <GEO_Kante_Allg>\n"
				+ "                <GEO_Form>\n"
				+ "                  <Wert>Gerade</Wert>\n"
				+ "                </GEO_Form>\n"
				+ "                <GEO_Laenge>\n"
				+ "                  <Wert>%.5f</Wert>\n"
				+ "                </GEO_Laenge>\n"
				+ "                <Plan_Quelle>\n"
				+ "                  <Wert>Ivl</Wert>\n"
				+ "                </Plan_Quelle>\n"
				+ "              </GEO_Kante_Allg>\n"
				+ "              <ID_GEO_Art>\n"
				+ "                <Wert>%s</Wert>\n"
				+ "              </ID_GEO_Art>\n"
				+ "              <ID_GEO_Knoten_A>\n"
				+ "                <Wert>%s</Wert>\n"
				+ "              </ID_GEO_Knoten_A>\n"
				+ "              <ID_GEO_Knoten_B>\n"
				+ "                <Wert>%s</Wert>\n"
				+ "              </ID_GEO_Knoten_B>\n"
				+ "            </GEO_Kante>";
		//@formatter:on
	}

}
