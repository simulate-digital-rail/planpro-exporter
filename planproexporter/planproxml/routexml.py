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
             + f"{RouteXML.get_sections_xml(route)}" \
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
    def get_sections_xml(route):
        all_xml = ""
        edges_in_order = route.get_edges_in_order()
        for i in range(0, len(edges_in_order)):
            cur_edge = edges_in_order[i]
            distance_a = 0.0
            distance_b = cur_edge.get_length()
            if i == 0:
                # Start edge
                distance_a = route.start_signal.distance_edge
                if route.start_signal.effective_direction == "gegen":
                    distance_b = 0.0
            elif i == len(edges_in_order) - 1:
                # End edge
                if route.end_signal.effective_direction == "gegen":
                    distance_a = cur_edge.get_length()
                distance_b = route.end_signal.distance_edge
            all_xml = all_xml + RouteXML.get_section_xml(cur_edge, distance_a, distance_b)
        return all_xml

    @staticmethod
    def get_section_xml(edge, distance_a, distance_b):
        return f"              <Bereich_Objekt_Teilbereich>" + "\n" \
               + f"                <Begrenzung_A>" + "\n" \
               + f"                  <Wert>{distance_a:.3f}</Wert>" + "\n" \
               + f"                </Begrenzung_A>" + "\n" \
               + f"                <Begrenzung_B>" + "\n" \
               + f"                  <Wert>{distance_b:.3f}</Wert>" + "\n" \
               + f"                </Begrenzung_B>" + "\n" \
               + f"                <ID_TOP_Kante>" + "\n" \
               + f"                  <Wert>{edge.top_edge_uuid}</Wert>" + "\n" \
               + f"                </ID_TOP_Kante>" + "\n" \
               + f"              </Bereich_Objekt_Teilbereich>" + "\n"
