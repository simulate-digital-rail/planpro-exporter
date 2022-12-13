class SignalXML(object):

    @staticmethod
    def get_control_memeber_xml(signal):
        return f"            <Stellelement>" + "\n" \
             + f"              <Identitaet>" + "\n" \
             + f"                <Wert>{signal.control_member_uuid}</Wert>" + "\n" \
             + f"              </Identitaet>" + "\n" \
             + f"              <Basis_Objekt_Allg>" + "\n" \
             + f"                <Datum_Regelwerk>" + "\n" \
             + f"                  <Wert>2012-02-24</Wert>" + "\n" \
             + f"                </Datum_Regelwerk>" + "\n" \
             + f"              </Basis_Objekt_Allg>" + "\n" \
             + f"              <Objektreferenzen/>" + "\n" \
             + f"              <ID_Energie>" + "\n" \
             + f"                <Wert>C35FDB88-889E-539E-A68B-6079265F70D9</Wert>" + "\n" \
             + f"              </ID_Energie>" + "\n" \
             + f"              <ID_Information>" + "\n" \
             + f"                <Wert>C35FDB88-889E-539E-A68B-6079265F70D9</Wert>" + "\n" \
             + f"              </ID_Information>" + "\n" \
             + f"            </Stellelement>" + "\n"

    @staticmethod
    def get_signal_xml(signal):
        trip_length = f"{(signal.trip.get_length()/1000):.3f}".replace(".", ",")

        return f"            <Signal>" + "\n" \
             + f"              <Identitaet>" + "\n" \
             + f"                <Wert>{signal.signal_uuid}</Wert>" + "\n" \
             + f"              </Identitaet>" + "\n" \
             + f"              <Basis_Objekt_Allg>" + "\n" \
             + f"                <Datum_Regelwerk>" + "\n" \
             + f"                  <Wert>2012-02-24</Wert>" + "\n" \
             + f"                </Datum_Regelwerk>" + "\n" \
             + f"              </Basis_Objekt_Allg>" + "\n" \
             + f"              <Objektreferenzen/>" + "\n" \
             + f"              <Punkt_Objekt_Strecke>" + "\n" \
             + f"                <ID_Strecke>" + "\n" \
             + f"                  <Wert>{signal.trip.trip_uuid}</Wert>" + "\n" \
             + f"                </ID_Strecke>" + "\n" \
             + f"                <Strecke_Km>" + "\n" \
             + f"                  <Wert>{trip_length}</Wert>" + "\n" \
             + f"                </Strecke_Km>" + "\n" \
             + f"              </Punkt_Objekt_Strecke>" + "\n" \
             + f"              <Punkt_Objekt_TOP_Kante>" + "\n" \
             + f"                <Abstand>" + "\n" \
             + f"                  <Wert>{signal.distance_edge:.3f}</Wert>" + "\n" \
             + f"                </Abstand>" + "\n" \
             + f"                <ID_TOP_Kante>" + "\n" \
             + f"                  <Wert>{signal.edge.top_edge_uuid}</Wert>" + "\n" \
             + f"                </ID_TOP_Kante>" + "\n" \
             + f"                <Wirkrichtung>" + "\n" \
             + f"                  <Wert>{signal.effective_direction}</Wert>" + "\n" \
             + f"                </Wirkrichtung>" + "\n" \
             + f"                <Seitlicher_Abstand>" + "\n" \
             + f"                  <Wert>{signal.get_side_distance():.3f}</Wert>" + "\n" \
             + f"                </Seitlicher_Abstand>" + "\n" \
             + f"              </Punkt_Objekt_TOP_Kante>" + "\n" \
             + f"              <Bezeichnung>" + "\n" \
             + f"                <Bezeichnung_Aussenanlage>" + "\n" \
             + f"                  <Wert>{signal.classification_number}{signal.element_name}</Wert>" + "\n" \
             + f"                </Bezeichnung_Aussenanlage>" + "\n" \
             + f"                <Bezeichnung_Lageplan_Kurz>" + "\n" \
             + f"                  <Wert>{signal.element_name}</Wert>" + "\n" \
             + f"                </Bezeichnung_Lageplan_Kurz>" + "\n" \
             + f"                <Bezeichnung_Lageplan_Lang>" + "\n" \
             + f"                  <Wert>{signal.classification_number}{signal.element_name}</Wert>" + "\n" \
             + f"                </Bezeichnung_Lageplan_Lang>" + "\n" \
             + f"                <Bezeichnung_Tabelle>" + "\n" \
             + f"                  <Wert>{signal.classification_number}{signal.element_name}</Wert>" + "\n" \
             + f"                </Bezeichnung_Tabelle>" + "\n" \
             + f"                <Kennzahl>" + "\n" \
             + f"                  <Wert>{signal.classification_number}</Wert>" + "\n" \
             + f"                </Kennzahl>" + "\n" \
             + f"                <Oertlicher_Elementname>" + "\n" \
             + f"                  <Wert>{signal.element_name}</Wert>" + "\n" \
             + f"                </Oertlicher_Elementname>" + "\n" \
             + f"              </Bezeichnung>" + "\n" \
             + f"              <Signal_Real>" + "\n" \
             + f"                <Signal_Befestigungsart>" + "\n" \
             + f"                  <Wert>Mast</Wert>" + "\n" \
             + f"                </Signal_Befestigungsart>" + "\n" \
             + f"                <Signal_Real_Aktiv>" + "\n" \
             + f"                  <ID_Stellelement>" + "\n" \
             + f"                    <Wert>{signal.control_member_uuid}</Wert>" + "\n" \
             + f"                  </ID_Stellelement>" + "\n" \
             + f"                  <Signal_Funktion>" + "\n" \
             + f"                    <Wert>{signal.function}</Wert>" + "\n" \
             + f"                  </Signal_Funktion>" + "\n" \
             + f"                </Signal_Real_Aktiv>" + "\n" \
             + f"                <Signal_Real_Aktiv_Schirm>" + "\n" \
             + f"                  <Dunkelschaltung>" + "\n" \
             + f"                    <Wert>false</Wert>" + "\n" \
             + f"                  </Dunkelschaltung>" + "\n" \
             + f"                  <Richtpunktentfernung>" + "\n" \
             + f"                    <Wert>150</Wert>" + "\n" \
             + f"                  </Richtpunktentfernung>" + "\n" \
             + f"                  <Signal_Art>" + "\n" \
             + f"                    <Wert>{signal.kind}</Wert>" + "\n" \
             + f"                  </Signal_Art>" + "\n" \
             + f"                  <Signalsystem>" + "\n" \
             + f"                    <Wert>Ks</Wert>" + "\n" \
             + f"                  </Signalsystem>" + "\n" \
             + f"                  <Streuscheibe_Art>" + "\n" \
             + f"                    <Wert>HG</Wert>" + "\n" \
             + f"                  </Streuscheibe_Art>" + "\n" \
             + f"                  <Streuscheibe_Betriebsstellung>" + "\n" \
             + f"                    <Wert>HG4</Wert>" + "\n" \
             + f"                  </Streuscheibe_Betriebsstellung>" + "\n" \
             + f"                </Signal_Real_Aktiv_Schirm>" + "\n" \
             + f"              </Signal_Real>" + "\n" \
             + f"            </Signal>" + "\n"
