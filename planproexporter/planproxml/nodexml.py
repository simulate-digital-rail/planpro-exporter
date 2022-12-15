from yaramo.model import GeoNode, Node

class NodeXML(object):

    @staticmethod
    def get_geo_point_xml(geonode: GeoNode, identifier: str):
        return f"            <GEO_Punkt> <!-- {identifier} -->\n" \
               + f"              <Identitaet>\n" \
               + f"                <Wert>{geonode.geo_point.uuid}</Wert>\n" \
               + f"              </Identitaet>\n" \
               + f"              <Basis_Objekt_Allg>\n" \
               + f"                <Datum_Regelwerk>\n" \
               + f"                  <Wert>2012-02-24</Wert>\n" \
               + f"                </Datum_Regelwerk>\n" \
               + f"              </Basis_Objekt_Allg>\n" \
               + f"              <Objektreferenzen/>\n" \
               + f"              <GEO_Punkt_Allg>\n" \
               + f"                <GK_X>\n" \
               + f"                  <Wert>{x:.5f}</Wert>\n" \
               + f"                </GK_X>\n" \
               + f"                <GK_Y>\n" \
               + f"                  <Wert>{y:.5f}</Wert>\n" \
               + f"                </GK_Y>\n" \
               + f"                <Plan_Quelle>\n" \
               + f"                  <Wert>Ivl</Wert>\n" \
               + f"                </Plan_Quelle>\n" \
               + f"                <GEO_KoordinatenSystem_LSys>\n" \
               + f"                  <Wert>EA0</Wert>\n" \
               + f"                </GEO_KoordinatenSystem_LSys>\n" \
               + f"              </GEO_Punkt_Allg>\n" \
               + f"              <ID_GEO_Knoten>\n" \
               + f"                <Wert>{geonode.uuid}</Wert>\n" \
               + f"              </ID_GEO_Knoten>\n" \
               + f"            </GEO_Punkt>\n"

    @staticmethod
    def get_geo_node_xml(geonode: GeoNode, identifier:str):
        return f"            <GEO_Knoten> <!-- {identifier} -->\n" \
               + f"              <Identitaet>\n" \
               + f"                <Wert>{geonode.uuid}</Wert>\n" \
               + f"              </Identitaet>\n" \
               + f"              <Basis_Objekt_Allg>\n" \
               + f"                <Datum_Regelwerk>\n" \
               + f"                  <Wert>2012-02-24</Wert>\n" \
               + f"                </Datum_Regelwerk>\n" \
               + f"              </Basis_Objekt_Allg>\n" \
               + f"              <Objektreferenzen/>\n" \
               + f"            </GEO_Knoten>\n"

    @staticmethod
    def get_top_node_xml(node: Node):
        return f"            <TOP_Knoten> <!-- {node} -->\n" \
               + f"              <Identitaet>\n" \
               + f"                <Wert>{node.uuid}</Wert>\n" \
               + f"              </Identitaet>\n" \
               + f"              <Basis_Objekt_Allg>\n" \
               + f"                <Datum_Regelwerk>\n" \
               + f"                  <Wert>2012-02-24</Wert>\n" \
               + f"                </Datum_Regelwerk>\n" \
               + f"              </Basis_Objekt_Allg>\n" \
               + f"              <Objektreferenzen/>\n" \
               + f"              <ID_GEO_Knoten>\n" \
               + f"                <Wert>{node.geo_node.uuid}</Wert>\n" \
               + f"              </ID_GEO_Knoten>\n" \
               + f"            </TOP_Knoten>\n"

