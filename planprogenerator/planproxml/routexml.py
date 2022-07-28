class RouteXML(object):

    @staticmethod
    def get_route_xml(route):
        if route.end_signal is None:
            return ""
        return f"              <Fstr_Fahrweg>" + "\n" \
             + f"                <Identitaet>" + "\n" \
             + f"                  <Wert>{route.route_uuid}</Wert>" + "\n" \
             + f"                </Identitaet>" + "\n" \
             + f"                <Basis_Objekt_Allg>" + "\n" \
             + f"                  <Datum_Regelwerk>" + "\n" \
             + f"                    <Wert>2012-02-24</Wert>" + "\n" \
             + f"                  </Datum_Regelwerk>" + "\n" \
             + f"                </Basis_Objekt_Allg>" + "\n" \
             + f"                <Objektreferenzen/>" + "\n" \
             + f"{RouteXML.get_sections_xml(route.edges)}" + "\n" \
             + f"                <Fstr_V_Hg>" + "\n" \
             + f"                  <Wert>{route.v_hg}</Wert>" + "\n" \
             + f"                </Fstr_V_Hg>" + "\n" \
             + f"                <ID_Start>" + "\n" \
             + f"                  <Wert>{route.start_signal.signal_uuid}</Wert> <!-- {route.start_signal.element_name} -->" + "\n" \
             + f"                </ID_Start>" + "\n" \
             + f"                <ID_Ziel>" + "\n" \
             + f"                  <Wert>{route.end_signal.signal_uuid}</Wert> <!-- {route.end_signal.element_name} -->" + "\n" \
             + f"                </ID_Ziel>" + "\n" \
             + f"              </Fstr_Fahrweg>" + "\n"

    @staticmethod
    def get_sections_xml(edges):
        # TODO: Logic for order
        all_xml = ""
        for edge in edges:
            all_xml = all_xml + RouteXML.get_section_xml(edge)
        return all_xml

    @staticmethod
    def get_section_xml(edge):
        # TODO: Not both get_length
        return f"              <Bereich_Objekt_Teilbereich>" + "\n" \
               + f"                <Begrenzung_A>" + "\n" \
               + f"                  <Wert>{edge.get_length():.3f}</Wert>" + "\n" \
               + f"                </Begrenzung_A>" + "\n" \
               + f"                <Begrenzung_B>" + "\n" \
               + f"                  <Wert>{edge.get_length():.3f}</Wert>" + "\n" \
               + f"                </Begrenzung_B>" + "\n" \
               + f"                <ID_TOP_Kante>" + "\n" \
               + f"                  <Wert>{edge.top_edge_uuid}</Wert>" + "\n" \
               + f"                </ID_TOP_Kante>" + "\n" \
               + f"              </Bereich_Objekt_Teilbereich>" + "\n"
