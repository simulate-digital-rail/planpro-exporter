package de.hpi.osm.planpro.generator;

public class RunningTrackTemplates {

	public static String getFstrFahrwegTemplate() {
		// @formatter:off
				return "              <Fstr_Fahrweg>"+"\n"
						+"                <Identitaet>"+"\n"
						+"                  <Wert>%s</Wert>"+"\n"
						+"                </Identitaet>"+"\n"
						+"                <Basis_Objekt_Allg>"+"\n"
						+"                  <Datum_Regelwerk>"+"\n"
						+"                    <Wert>2012-02-24</Wert>"+"\n"
						+"                  </Datum_Regelwerk>"+"\n"
						+"                </Basis_Objekt_Allg>"+"\n"
						+"                <Objektreferenzen/>"+"\n"
						+"%s"+"\n" // Teilbereiche
						+"                <Fstr_V_Hg>"+"\n"
						+"                  <Wert>%d</Wert>"+"\n"
						+"                </Fstr_V_Hg>"+"\n"
						+"                <ID_Start>"+"\n"
						+"                  <Wert>%s</Wert> <!-- %s -->"+"\n"
						+"                </ID_Start>"+"\n"
						+"                <ID_Ziel>"+"\n"
						+"                  <Wert>%s</Wert> <!-- %s -->"+"\n"
						+"                </ID_Ziel>"+"\n"
						+"              </Fstr_Fahrweg>"+"\n";
		// @formatter:on
	}

	public static String getTeilbereichTemplate() {
		// @formatter:off
				return "              <Bereich_Objekt_Teilbereich> <!-- %s to %s -->"+"\n"
						+"                <Begrenzung_A>"+"\n"
						+"                  <Wert>%.3f</Wert>"+"\n"
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
