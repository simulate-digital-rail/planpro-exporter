class TripXML(object):

    @staticmethod
    def get_trip_xml(trip):
        return f"            <Strecke>" + "\n" \
             + f"              <Identitaet>" + "\n" \
             + f"                <Wert>{trip.trip_uuid}</Wert>" + "\n" \
             + f"              </Identitaet>" + "\n" \
             + f"              <Basis_Objekt_Allg>" + "\n" \
             + f"                <Datum_Regelwerk>" + "\n" \
             + f"                  <Wert>2012-02-24</Wert>" + "\n" \
             + f"                </Datum_Regelwerk>" + "\n" \
             + f"              </Basis_Objekt_Allg>" + "\n" \
             + f"              <Objektreferenzen/>" + "\n" \
             + f"{TripXML.get_sections_xml(trip.edges)}" \
             + f"              <Bezeichnung>" + "\n" \
             + f"                <Bezeichnung_Strecke>" + "\n" \
             + f"                  <Wert>{trip.trip_name}</Wert>" + "\n" \
             + f"                </Bezeichnung_Strecke>" + "\n" \
             + f"              </Bezeichnung>" + "\n" \
             + f"            </Strecke>" + "\n"

    @staticmethod
    def get_sections_xml(edges):
        all_xml = ""
        for edge in edges:
            all_xml = all_xml + TripXML.get_section_xml(edge)
        return all_xml

    @staticmethod
    def get_section_xml(edge):
        return f"              <Bereich_Objekt_Teilbereich>" + "\n" \
             + f"                <Begrenzung_A>" + "\n" \
             + f"                  <Wert>0.000</Wert>" + "\n" \
             + f"                </Begrenzung_A>" + "\n" \
             + f"                <Begrenzung_B>" + "\n" \
             + f"                  <Wert>{edge.get_length():.3f}</Wert>" + "\n" \
             + f"                </Begrenzung_B>" + "\n" \
             + f"                <ID_TOP_Kante>" + "\n" \
             + f"                  <Wert>{edge.top_edge_uuid}</Wert>" + "\n" \
             + f"                </ID_TOP_Kante>" + "\n" \
             + f"              </Bereich_Objekt_Teilbereich>" + "\n"