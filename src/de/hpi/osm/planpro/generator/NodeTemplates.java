package de.hpi.osm.planpro.generator;

public class NodeTemplates {

	public static String getGeoPunktTemplate() {
		// @formatter:off
		return "            <GEO_Punkt> <!-- %s -->\n"
				+ "              <Identitaet>\n"
				+ "                <Wert>%s</Wert>\n"
				+ "              </Identitaet>\n"
				+ "              <Basis_Objekt_Allg>\n"
				+ "                <Datum_Regelwerk>\n"
				+ "                  <Wert>2012-02-24</Wert>\n"
				+ "                </Datum_Regelwerk>\n"
				+ "              </Basis_Objekt_Allg>\n"
				+ "              <Objektreferenzen/>\n"
				+ "              <GEO_Punkt_Allg>\n"
				+ "                <GK_X>\n"
				+ "                  <Wert>%.5f</Wert>\n"
				+ "                </GK_X>\n"
				+ "                <GK_Y>\n"
				+ "                  <Wert>%.5f</Wert>\n"
				+ "                </GK_Y>\n"
				+ "                <Plan_Quelle>\n"
				+ "                  <Wert>Ivl</Wert>\n"
				+ "                </Plan_Quelle>\n"
				+ "                <GEO_KoordinatenSystem_LSys>\n"
				+ "                  <Wert>EA0</Wert>\n"
				+ "                </GEO_KoordinatenSystem_LSys>\n"
				+ "              </GEO_Punkt_Allg>\n"
				+ "              <ID_GEO_Knoten>\n"
				+ "                <Wert>%s</Wert>\n"
				+ "              </ID_GEO_Knoten>\n"
				+ "            </GEO_Punkt>";
		// @formatter:on
	}

	public static String getGeoKnotenTempate() {
		// @formatter:off
		return "            <GEO_Knoten> <!-- %s -->\n"
				+ "              <Identitaet>\n"
				+ "                <Wert>%s</Wert>\n"
				+ "              </Identitaet>\n"
				+ "              <Basis_Objekt_Allg>\n"
				+ "                <Datum_Regelwerk>\n"
				+ "                  <Wert>2012-02-24</Wert>\n"
				+ "                </Datum_Regelwerk>\n"
				+ "              </Basis_Objekt_Allg>\n"
				+ "              <Objektreferenzen/>\n"
				+ "            </GEO_Knoten>";
		// @formatter:on
	}

	public static String getTopKnotenTempate() {
		// @formatter:off
		return "            <TOP_Knoten> <!-- %s -->\n"
				+ "              <Identitaet>\n"
				+ "                <Wert>%s</Wert>\n"
				+ "              </Identitaet>\n"
				+ "              <Basis_Objekt_Allg>\n"
				+ "                <Datum_Regelwerk>\n"
				+ "                  <Wert>2012-02-24</Wert>\n"
				+ "                </Datum_Regelwerk>\n"
				+ "              </Basis_Objekt_Allg>\n"
				+ "              <Objektreferenzen/>\n"
				+ "              <ID_GEO_Knoten>\n"
				+ "                <Wert>%s</Wert>\n"
				+ "              </ID_GEO_Knoten>\n"
				+ "            </TOP_Knoten>";
		// @formatter:on
	}

}
