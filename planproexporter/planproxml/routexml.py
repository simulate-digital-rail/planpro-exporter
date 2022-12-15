from yaramo.model import Route, Edge, SignalDirection

class RouteXML(object):

    @staticmethod
    def get_route_xml(route: Route):
        if route.end_signal is None:
            return ""
        return f"              <Fstr_Fahrweg>" + "\n" \
             + f"                <Identitaet>" + "\n" \
             + f"                  <Wert>{route.uuid}</Wert>" + "\n" \
             + f"                </Identitaet>" + "\n" \
             + f"                <Basis_Objekt_Allg>" + "\n" \
             + f"                  <Datum_Regelwerk>" + "\n" \
             + f"                    <Wert>2012-02-24</Wert>" + "\n" \
             + f"                  </Datum_Regelwerk>" + "\n" \
             + f"                </Basis_Objekt_Allg>" + "\n" \
             + f"                <Objektreferenzen/>" + "\n" \
             + f"{RouteXML.get_sections_xml(route)}" \
             + f"                <Fstr_V_Hg>" + "\n" \
             + f"                  <Wert>{route.maximum_speed}</Wert>" + "\n" \
             + f"                </Fstr_V_Hg>" + "\n" \
             + f"                <ID_Start>" + "\n" \
             + f"                  <Wert>{route.start_signal.uuid}</Wert> <!-- {route.start_signal.name} -->" + "\n" \
             + f"                </ID_Start>" + "\n" \
             + f"                <ID_Ziel>" + "\n" \
             + f"                  <Wert>{route.end_signal.uuid}</Wert> <!-- {route.end_signal.name} -->" + "\n" \
             + f"                </ID_Ziel>" + "\n" \
             + f"              </Fstr_Fahrweg>" + "\n"

    @staticmethod
    def get_sections_xml(route: Route):
        all_xml = ""
        edges_in_order = route.get_edges_in_order()
        for i in range(0, len(edges_in_order)):
            cur_edge = edges_in_order[i]
            distance_a = 0.0
            distance_b = cur_edge.length
            if i == 0:
                # Start edge
                distance_a = route.start_signal.distance_previous_node
                if route.start_signal.direction == SignalDirection.GEGEN:
                    distance_b = 0.0
            elif i == len(edges_in_order) - 1:
                # End edge
                if route.end_signal.direction == SignalDirection.GEGEN:
                    distance_a = cur_edge.length
                distance_b = route.end_signal.distance_previous_node
            all_xml = all_xml + RouteXML.get_section_xml(cur_edge, distance_a, distance_b)
        return all_xml

    @staticmethod
    def get_section_xml(edge: Edge, distance_a: float, distance_b: float):
        return f"              <Bereich_Objekt_Teilbereich>" + "\n" \
               + f"                <Begrenzung_A>" + "\n" \
               + f"                  <Wert>{distance_a:.3f}</Wert>" + "\n" \
               + f"                </Begrenzung_A>" + "\n" \
               + f"                <Begrenzung_B>" + "\n" \
               + f"                  <Wert>{distance_b:.3f}</Wert>" + "\n" \
               + f"                </Begrenzung_B>" + "\n" \
               + f"                <ID_TOP_Kante>" + "\n" \
               + f"                  <Wert>{edge.uuid}</Wert>" + "\n" \
               + f"                </ID_TOP_Kante>" + "\n" \
               + f"              </Bereich_Objekt_Teilbereich>" + "\n"
