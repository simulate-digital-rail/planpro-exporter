from yaramo.model import Edge, GeoNode
import math


class EdgeXML(object):

    @staticmethod
    def get_top_edge_xml(edge: Edge):
        connection_a = "Ende"
        if len(edge.node_a.connected_nodes) > 1:
            connection_a = edge.node_a.get_anschluss_of_other(edge.node_b).name
        connection_b = "Ende"
        if len(edge.node_b.connected_nodes) > 1:
            connection_b = edge.node_b.get_anschluss_of_other(edge.node_a).name
        return f"            <TOP_Kante> <!-- {edge.node_a.uuid} to {edge.node_b.uuid} -->\n" \
               + f"              <Identitaet>\n" \
               + f"                <Wert>{edge.uuid}</Wert>\n" \
               + f"              </Identitaet>\n" \
               + f"              <Basis_Objekt_Allg>\n" \
               + f"                <Datum_Regelwerk>\n" \
               + f"                  <Wert>2012-02-24</Wert>\n" \
               + f"                </Datum_Regelwerk>\n" \
               + f"              </Basis_Objekt_Allg>\n" \
               + f"              <Objektreferenzen/>\n" \
               + f"              <ID_TOP_Knoten_A>\n" \
               + f"                <Wert>{edge.node_a.uuid}</Wert> <!-- {edge.node_a.uuid} -->\n" \
               + f"              </ID_TOP_Knoten_A>\n" \
               + f"              <ID_TOP_Knoten_B>\n" \
               + f"                <Wert>{edge.node_b.uuid}</Wert> <!-- {edge.node_b.uuid} -->\n" \
               + f"              </ID_TOP_Knoten_B>\n" \
               + f"              <TOP_Kante_Allg>\n" \
               + f"                <TOP_Anschluss_A>\n" \
               + f"                  <Wert>{connection_a}</Wert>\n" \
               + f"                </TOP_Anschluss_A>\n" \
               + f"                <TOP_Anschluss_B>\n" \
               + f"                  <Wert>{connection_b}</Wert>\n" \
               + f"                </TOP_Anschluss_B>\n" \
               + f"                <TOP_Laenge>\n" \
               + f"                  <Wert>{edge.length:.3f}</Wert>\n" \
               + f"                </TOP_Laenge>\n" \
               + f"              </TOP_Kante_Allg>\n" \
               + f"            </TOP_Kante>\n"

    @staticmethod
    def get_geo_edge_xml(geo_node_a: GeoNode, geo_node_b: GeoNode, uuid, top_edge: Edge):
        length = geo_node_a.get_distance_to_other_geo_node(geo_node_b)

        return f"            <GEO_Kante> <!-- {top_edge.node_a.uuid} to {top_edge.node_b.uuid} -->\n" \
             + f"              <Identitaet>\n" \
             + f"                <Wert>{uuid}</Wert>\n" \
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
             + f"                  <Wert>{length:.5f}</Wert>\n" \
             + f"                </GEO_Laenge>\n" \
             + f"                <Plan_Quelle>\n" \
             + f"                  <Wert>Ivl</Wert>\n" \
             + f"                </Plan_Quelle>\n" \
             + f"              </GEO_Kante_Allg>\n" \
             + f"              <ID_GEO_Art>\n" \
             + f"                <Wert>{top_edge.uuid}</Wert>\n" \
             + f"              </ID_GEO_Art>\n" \
             + f"              <ID_GEO_Knoten_A>\n" \
             + f"                <Wert>{geo_node_a.uuid}</Wert>\n" \
             + f"              </ID_GEO_Knoten_A>\n" \
             + f"              <ID_GEO_Knoten_B>\n" \
             + f"                <Wert>{geo_node_b.uuid}</Wert>\n" \
             + f"              </ID_GEO_Knoten_B>\n" \
             + f"            </GEO_Kante>\n"
