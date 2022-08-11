class EdgeXML(object):

    @staticmethod
    def get_top_edge_xml(edge):
        connection_a = "Ende"
        if len(edge.node_a.connected_nodes) > 1:
            connection_a = edge.node_a.get_anschluss_of_other(edge.node_b)
        connection_b = "Ende"
        if len(edge.node_b.connected_nodes) > 1:
            connection_b = edge.node_b.get_anschluss_of_other(edge.node_a)
        return f"            <TOP_Kante> <!-- {edge.node_a.identifier} to {edge.node_b.identifier} -->\n" \
               + f"              <Identitaet>\n" \
               + f"                <Wert>{edge.top_edge_uuid}</Wert>\n" \
               + f"              </Identitaet>\n" \
               + f"              <Basis_Objekt_Allg>\n" \
               + f"                <Datum_Regelwerk>\n" \
               + f"                  <Wert>2012-02-24</Wert>\n" \
               + f"                </Datum_Regelwerk>\n" \
               + f"              </Basis_Objekt_Allg>\n" \
               + f"              <Objektreferenzen/>\n" \
               + f"              <ID_TOP_Knoten_A>\n" \
               + f"                <Wert>{edge.node_a.top_node_uuid}</Wert> <!-- {edge.node_a.identifier} -->\n" \
               + f"              </ID_TOP_Knoten_A>\n" \
               + f"              <ID_TOP_Knoten_B>\n" \
               + f"                <Wert>{edge.node_b.top_node_uuid}</Wert> <!-- {edge.node_b.identifier} -->\n" \
               + f"              </ID_TOP_Knoten_B>\n" \
               + f"              <TOP_Kante_Allg>\n" \
               + f"                <TOP_Anschluss_A>\n" \
               + f"                  <Wert>{connection_a}</Wert>\n" \
               + f"                </TOP_Anschluss_A>\n" \
               + f"                <TOP_Anschluss_B>\n" \
               + f"                  <Wert>{connection_b}</Wert>\n" \
               + f"                </TOP_Anschluss_B>\n" \
               + f"                <TOP_Laenge>\n" \
               + f"                  <Wert>{edge.get_length():.3f}</Wert>\n" \
               + f"                </TOP_Laenge>\n" \
               + f"              </TOP_Kante_Allg>\n" \
               + f"            </TOP_Kante>\n"

    @staticmethod
    def get_geo_edge_xml(edge):
        return f"            <GEO_Kante> <!-- {edge.node_a.identifier} to {edge.node_b.identifier} -->\n" \
             + f"              <Identitaet>\n" \
             + f"                <Wert>{edge.geo_edge_uuid}</Wert>\n" \
             + f"              </Identitaet>\n" \
             + f"              <Basis_Objekt_Allg>\n" \
             + f"                <Datum_Regelwerk>\n" \
             + f"                  <Wert>2012-02-24</Wert>\n" \
             + f"                </Datum_Regelwerk>\n" \
             + f"              </Basis_Objekt_Allg>\n" \
             + f"              <Objektreferenzen/>\n" \
             + f"              <GEO_Kante_Allg>\n" \
             + f"                <GEO_Form>\n" \
             + f"                  <Wert>Gerade</Wert>\n" \
             + f"                </GEO_Form>\n" \
             + f"                <GEO_Laenge>\n" \
             + f"                  <Wert>{edge.get_length():.5f}</Wert>\n" \
             + f"                </GEO_Laenge>\n" \
             + f"                <Plan_Quelle>\n" \
             + f"                  <Wert>Ivl</Wert>\n" \
             + f"                </Plan_Quelle>\n" \
             + f"              </GEO_Kante_Allg>\n" \
             + f"              <ID_GEO_Art>\n" \
             + f"                <Wert>{edge.top_edge_uuid}</Wert>\n" \
             + f"              </ID_GEO_Art>\n" \
             + f"              <ID_GEO_Knoten_A>\n" \
             + f"                <Wert>{edge.node_a.geo_node_uuid}</Wert> <!-- {edge.node_a.identifier} -->\n" \
             + f"              </ID_GEO_Knoten_A>\n" \
             + f"              <ID_GEO_Knoten_B>\n" \
             + f"                <Wert>{edge.node_b.geo_node_uuid}</Wert> <!-- {edge.node_b.identifier} -->\n" \
             + f"              </ID_GEO_Knoten_B>\n" \
             + f"            </GEO_Kante>\n"
