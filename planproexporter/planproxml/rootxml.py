import uuid
import datetime


class RootXML(object):

    ausgabe_fachdaten_uuid = str(uuid.uuid4())
    external_element_control_uuid = "C35FDB88-889E-539E-A68B-6079265F70D9"
    accommondation_uuid = "F4CE3AF8-13B1-4E12-BB4D-982BEA37466E"

    @staticmethod
    def get_prefix_xml():
        current_datetime = datetime.datetime.now()
        datetime_string = current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>" + "\n" \
             + f"<nsPlanPro:PlanPro_Schnittstelle xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:nsPlanPro=\"http://www.plan-pro.org/modell/PlanPro/1.9.0.2\" xmlns:nsSignalbegriffe_Ril_301=\"http://www.plan-pro.org/modell/Signalbegriffe_Ril_301/1.9.0\">" + "\n" \
             + f"  <Identitaet>" + "\n" \
             + f"    <Wert>{str(uuid.uuid4())}</Wert>" + "\n" \
             + f"  </Identitaet>" + "\n" \
             + f"  <PlanPro_Schnittstelle_Allg>" + "\n" \
             + f"    <Erzeugung_Zeitstempel>" + "\n" \
             + f"      <Wert>{datetime_string}</Wert>" + "\n" \
             + f"    </Erzeugung_Zeitstempel>" + "\n" \
             + f"    <Werkzeug_Name>" + "\n" \
             + f"      <Wert>Werkzeugkoffer</Wert>" + "\n" \
             + f"    </Werkzeug_Name>" + "\n" \
             + f"    <Werkzeug_Version>" + "\n" \
             + f"      <Wert>48.3.0</Wert>" + "\n" \
             + f"    </Werkzeug_Version>" + "\n" \
             + f"  </PlanPro_Schnittstelle_Allg>" + "\n" \
             + f"  <LST_Planung>" + "\n" \
             + f"    <Fachdaten>" + "\n" \
             + f"      <Ausgabe_Fachdaten>" + "\n" \
             + f"        <Identitaet>" + "\n" \
             + f"          <Wert>{RootXML.ausgabe_fachdaten_uuid}</Wert>" + "\n" \
             + f"        </Identitaet>" + "\n" \
             + f"        <LST_Zustand_Start>" + "\n" \
             + f"          <Identitaet>" + "\n" \
             + f"            <Wert>{str(uuid.uuid4())}</Wert>" + "\n" \
             + f"          </Identitaet>" + "\n" \
             + f"          <Container/>" + "\n" \
             + f"        </LST_Zustand_Start>" + "\n" \
             + f"        <LST_Zustand_Ziel>" + "\n" \
             + f"          <Identitaet>" + "\n" \
             + f"            <Wert>{str(uuid.uuid4())}</Wert>" + "\n" \
             + f"          </Identitaet>" + "\n" \
             + f"          <Container>" + "\n"

    @staticmethod
    def get_external_element_control_xml():
        return f"            <Aussenelementansteuerung>" + "\n" \
             + f"                 <Identitaet>" + "\n" \
             + f"                   <Wert>{RootXML.external_element_control_uuid}</Wert>" + "\n" \
             + f"                 </Identitaet>" + "\n" \
             + f"                 <Basis_Objekt_Allg>" + "\n" \
             + f"                   <Datum_Regelwerk>" + "\n" \
             + f"                     <Wert>2012-02-24</Wert>" + "\n" \
             + f"                   </Datum_Regelwerk>" + "\n" \
             + f"                 </Basis_Objekt_Allg>" + "\n" \
             + f"                 <Objektreferenzen/>" + "\n" \
             + f"                 <AEA_Allg>" + "\n" \
             + f"                   <Aussenelementansteuerung_Art>" + "\n" \
             + f"                     <Wert>ESTW_A</Wert>" + "\n" \
             + f"                   </Aussenelementansteuerung_Art>" + "\n" \
             + f"                 </AEA_Allg>" + "\n" \
             + f"                 <AEA_Energieversorgung>" + "\n" \
             + f"                   <Energieversorgung_Art_Ersatz>" + "\n" \
             + f"                     <Wert>Notstromaggregat_NEA_stationaer</Wert>" + "\n" \
             + f"                   </Energieversorgung_Art_Ersatz>" + "\n" \
             + f"                   <ID_Energie_Primaer>" + "\n" \
             + f"                     <Wert>{RootXML.external_element_control_uuid}</Wert>" + "\n" \
             + f"                   </ID_Energie_Primaer>" + "\n" \
             + f"                 </AEA_Energieversorgung>" + "\n" \
             + f"                 <Bezeichnung>" + "\n" \
             + f"                   <Bezeichnung_AEA>" + "\n" \
             + f"                     <Wert>Scheibenberg</Wert>" + "\n" \
             + f"                   </Bezeichnung_AEA>" + "\n" \
             + f"                 </Bezeichnung>" + "\n" \
             + f"                 <ID_Information_Primaer>" + "\n" \
             + f"                   <Wert>{RootXML.external_element_control_uuid}</Wert>" + "\n" \
             + f"                 </ID_Information_Primaer>" + "\n" \
             + f"                 <ID_Unterbringung>" + "\n" \
             + f"                   <Wert>{RootXML.accommondation_uuid}</Wert>" + "\n" \
             + f"                 </ID_Unterbringung>" + "\n" \
             + f"            </Aussenelementansteuerung>" + "\n"

    @staticmethod
    def get_accommodation_xml():
        return f"               <Unterbringung>" + "\n" \
             + f"                 <Identitaet>" + "\n" \
             + f"                   <Wert>{RootXML.accommondation_uuid}</Wert>" + "\n" \
             + f"                 </Identitaet>" + "\n" \
             + f"                 <Basis_Objekt_Allg>" + "\n" \
             + f"                   <Datum_Regelwerk>" + "\n" \
             + f"                     <Wert>2012-02-24</Wert>" + "\n" \
             + f"                   </Datum_Regelwerk>" + "\n" \
             + f"                 </Basis_Objekt_Allg>" + "\n" \
             + f"                 <Objektreferenzen/>" + "\n" \
             + f"                 <Unterbringung_Allg>" + "\n" \
             + f"                   <Unterbringung_Art>" + "\n" \
             + f"                     <Wert>Gebaeude</Wert>" + "\n" \
             + f"                   </Unterbringung_Art>" + "\n" \
             + f"                   <Unterbringung_Befestigung>" + "\n" \
             + f"                     <Wert>Fundament</Wert>" + "\n" \
             + f"                   </Unterbringung_Befestigung>" + "\n" \
             + f"                 </Unterbringung_Allg>" + "\n" \
             + f"                 <ID_GEO_Punkt>" + "\n" \
             + f"                   <Wert>11314F34-1A1C-4EBB-9AB2-133C5F2A9167</Wert> <!-- Does not exists -->" + "\n" \
             + f"                 </ID_GEO_Punkt>" + "\n" \
             + f"               </Unterbringung>" + "\n"

    @staticmethod
    def get_suffix(uuids):
        uuids_string = ""
        uuids.append(RootXML.external_element_control_uuid)
        uuids.append(RootXML.accommondation_uuid)

        for uuid in uuids:
            uuids_string = uuids_string + f"                         <ID_LST_Objekt_Planungsbereich>" + "\n"
            uuids_string = uuids_string + f"                            <Wert>{uuid}</Wert>" + "\n"
            uuids_string = uuids_string + f"                        </ID_LST_Objekt_Planungsbereich>" + "\n"

        return f"                  </Container>" + "\n" \
             + f"        </LST_Zustand_Ziel>" + "\n" \
             + f"        <Untergewerk_Art>" + "\n" \
             + f"          <Wert>sonstige</Wert>" + "\n" \
             + f"        </Untergewerk_Art>" + "\n" \
             + f"      </Ausgabe_Fachdaten>" + "\n" \
             + f"    </Fachdaten>" + "\n" \
             + f"    <Objektmanagement>" + "\n" \
             + f"        <LST_Planung_Projekt>" + "\n" \
             + f"              <Identitaet>" + "\n" \
             + f"                <Wert>F05DAC3B-4E33-43D3-9A03-6055566FC3B7</Wert>" + "\n" \
             + f"              </Identitaet>" + "\n" \
             + f"              <LST_Planung_Gruppe>" + "\n" \
             + f"                <Identitaet>" + "\n" \
             + f"                  <Wert>AFFE2101-3E72-4D64-88F1-FFE1A69396AA</Wert>" + "\n" \
             + f"                </Identitaet>" + "\n" \
             + f"                <Fuehrende_Oertlichkeit>" + "\n" \
             + f"                  <Wert>ABC</Wert>" + "\n" \
             + f"                </Fuehrende_Oertlichkeit>" + "\n" \
             + f"                <LST_Planung_Einzel>" + "\n" \
             + f"                  <Identitaet>" + "\n" \
             + f"                    <Wert>BE199B7D-A86C-4682-8E08-4B23DE2CF5A3</Wert>" + "\n" \
             + f"                  </Identitaet>" + "\n" \
             + f"                  <ID_Ausgabe_Fachdaten>" + "\n" \
             + f"                    <Wert>{RootXML.ausgabe_fachdaten_uuid}</Wert>" + "\n" \
             + f"                  </ID_Ausgabe_Fachdaten>" + "\n" \
             + f"                  <LST_Objekte_Planungsbereich>" + "\n" \
             + f"{uuids_string}" \
             + f"                  </LST_Objekte_Planungsbereich>" + "\n" \
             + f"                  <Planung_E_Allg>" + "\n" \
             + f"                    <Bauphase>" + "\n" \
             + f"                      <Wert>Neubau ESTW-A Scheibenberg</Wert>" + "\n" \
             + f"                    </Bauphase>" + "\n" \
             + f"                    <Bauzustand_Kurzbezeichnung>" + "\n" \
             + f"                      <Wert>Ibn-Zustand</Wert>" + "\n" \
             + f"                    </Bauzustand_Kurzbezeichnung>" + "\n" \
             + f"                    <Datum_Abschluss_Einzel>" + "\n" \
             + f"                      <Wert>2015-06-23</Wert>" + "\n" \
             + f"                    </Datum_Abschluss_Einzel>" + "\n" \
             + f"                    <Datum_Regelwerksstand>" + "\n" \
             + f"                      <Wert>2015-06-23</Wert>" + "\n" \
             + f"                    </Datum_Regelwerksstand>" + "\n" \
             + f"                    <Index_Ausgabe>" + "\n" \
             + f"                      <Wert>01</Wert>" + "\n" \
             + f"                    </Index_Ausgabe>" + "\n" \
             + f"                    <Informativ>" + "\n" \
             + f"                      <Wert>false</Wert>" + "\n" \
             + f"                    </Informativ>" + "\n" \
             + f"                    <Laufende_Nummer_Ausgabe>" + "\n" \
             + f"                      <Wert>04</Wert>" + "\n" \
             + f"                    </Laufende_Nummer_Ausgabe>" + "\n" \
             + f"                    <Planung_E_Art>" + "\n" \
             + f"                      <Wert>Bauzustand</Wert>" + "\n" \
             + f"                    </Planung_E_Art>" + "\n" \
             + f"                    <Planung_Phase>" + "\n" \
             + f"                      <Wert>PT_1</Wert>" + "\n" \
             + f"                    </Planung_Phase>" + "\n" \
             + f"                  </Planung_E_Allg>" + "\n" \
             + f"                  <Planung_E_Ausgabe_Besonders>" + "\n" \
             + f"                    <Referenz_Vergleich_Besonders>" + "\n" \
             + f"                      <Wert>12345-67890</Wert>" + "\n" \
             + f"                    </Referenz_Vergleich_Besonders>" + "\n" \
             + f"                    <Vergleich_Ausgabestand_Basis>" + "\n" \
             + f"                      <Wert>2019-07-31</Wert>" + "\n" \
             + f"                    </Vergleich_Ausgabestand_Basis>" + "\n" \
             + f"                    <Vergleichstyp_Besonders>" + "\n" \
             + f"                      <Wert>sonstige</Wert>" + "\n" \
             + f"                    </Vergleichstyp_Besonders>" + "\n" \
             + f"                  </Planung_E_Ausgabe_Besonders>" + "\n" \
             + f"                  <Planung_E_Handlung>" + "\n" \
             + f"                    <Planung_E_Erstellung>" + "\n" \
             + f"                      <Identitaet>" + "\n" \
             + f"                        <Wert>1A3E6734-9E68-40FC-8C3F-D231E98146FF</Wert>" + "\n" \
             + f"                      </Identitaet>" + "\n" \
             + f"                      <Anhang_Dokumentation>" + "\n" \
             + f"                          <Identitaet>" + "\n" \
             + f"                            <Wert>1A3E6734-9E68-40FC-8C3F-D23DE98246FF</Wert>" + "\n" \
             + f"                          </Identitaet>" + "\n" \
             + f"                          <Anhang_Allg>" + "\n" \
             + f"                            <Anhang_Art>" + "\n" \
             + f"                              <Wert>Erlaeuterungsbericht</Wert>" + "\n" \
             + f"                            </Anhang_Art>" + "\n" \
             + f"                            <Dateiname>" + "\n" \
             + f"                              <Wert>Erläuterungsbericht-Scheibenberg</Wert>" + "\n" \
             + f"                            </Dateiname>" + "\n" \
             + f"                            <Dateityp>" + "\n" \
             + f"                              <Wert>pdf</Wert>" + "\n" \
             + f"                            </Dateityp>" + "\n" \
             + f"                            <Daten>" + "\n" \
             + f"                                <Wert></Wert>" + "\n" \
             + f"                            </Daten>" + "\n" \
             + f"                          </Anhang_Allg>" + "\n" \
             + f"                        </Anhang_Dokumentation>" + "\n" \
             + f"                      <Datum>" + "\n" \
             + f"                        <Wert>2015-11-03</Wert>" + "\n" \
             + f"                      </Datum>" + "\n" \
             + f"                      <Handelnder>" + "\n" \
             + f"                        <Identitaet>" + "\n" \
             + f"                          <Wert>60024045-7D4E-4C59-98AC-088D437D4B7A</Wert>" + "\n" \
             + f"                        </Identitaet>" + "\n" \
             + f"                        <Akteur_Allg>" + "\n" \
             + f"                          <Name_Akteur>" + "\n" \
             + f"                            <Wert>Boockmeyer</Wert>" + "\n" \
             + f"                          </Name_Akteur>" + "\n" \
             + f"                          <Name_Akteur_10>" + "\n" \
             + f"                            <Wert>Boockmeyer</Wert>" + "\n" \
             + f"                          </Name_Akteur_10>" + "\n" \
             + f"                          <Name_Akteur_5>" + "\n" \
             + f"                            <Wert>Boock</Wert>" + "\n" \
             + f"                          </Name_Akteur_5>" + "\n" \
             + f"                        </Akteur_Allg>" + "\n" \
             + f"                        <Kontaktdaten>" + "\n" \
             + f"                          <Identitaet>" + "\n" \
             + f"                            <Wert>55555555-5555-5555-5555-555555555555</Wert>" + "\n" \
             + f"                          </Identitaet>" + "\n" \
             + f"                          <Name_Organisation>" + "\n" \
             + f"                            <Wert>HPI-OSM</Wert>" + "\n" \
             + f"                          </Name_Organisation>" + "\n" \
             + f"                        </Kontaktdaten>" + "\n" \
             + f"                      </Handelnder>" + "\n" \
             + f"                      <Ident_Rolle>" + "\n" \
             + f"                        <Wert>Planer</Wert>" + "\n" \
             + f"                      </Ident_Rolle>" + "\n" \
             + f"                    </Planung_E_Erstellung>" + "\n" \
             + f"                  </Planung_E_Handlung>" + "\n" \
             + f"                </LST_Planung_Einzel>" + "\n" \
             + f"                <Planung_G_Allg>" + "\n" \
             + f"                  <Datum_Abschluss_Gruppe>" + "\n" \
             + f"                    <Wert>2016-12-31</Wert>" + "\n" \
             + f"                  </Datum_Abschluss_Gruppe>" + "\n" \
             + f"                  <PlanPro_XSD_Version>" + "\n" \
             + f"                    <Wert>1.7.0.1</Wert>" + "\n" \
             + f"                  </PlanPro_XSD_Version>" + "\n" \
             + f"                  <Untergewerk_Art>" + "\n" \
             + f"                    <Wert>sonstige</Wert>" + "\n" \
             + f"                  </Untergewerk_Art>" + "\n" \
             + f"                  <Verantwortliche_Stelle_DB>" + "\n" \
             + f"                    <Wert>DB Netze</Wert>" + "\n" \
             + f"                  </Verantwortliche_Stelle_DB>" + "\n" \
             + f"                </Planung_G_Allg>" + "\n" \
             + f"                <Planung_G_Fuehrende_Strecke>" + "\n" \
             + f"                  <Strecke_Abschnitt>" + "\n" \
             + f"                    <Wert>Annaberg-Buchholz - Schwarzenberg</Wert>" + "\n" \
             + f"                  </Strecke_Abschnitt>" + "\n" \
             + f"                  <Strecke_Km>" + "\n" \
             + f"                    <Wert>120,000</Wert>" + "\n" \
             + f"                  </Strecke_Km>" + "\n" \
             + f"                  <Strecke_Nummer>" + "\n" \
             + f"                    <Wert>8980</Wert>" + "\n" \
             + f"                  </Strecke_Nummer>" + "\n" \
             + f"                </Planung_G_Fuehrende_Strecke>" + "\n" \
             + f"                <Planung_G_Schriftfeld>" + "\n" \
             + f"                  <Bauabschnitt>" + "\n" \
             + f"                    <Wert>Annaberg-Buchholz - Schwarzenberg</Wert>" + "\n" \
             + f"                  </Bauabschnitt>" + "\n" \
             + f"                  <Bezeichnung_Anlage>" + "\n" \
             + f"                    <Wert>ESTW-UZ N-Stadt</Wert>" + "\n" \
             + f"                  </Bezeichnung_Anlage>" + "\n" \
             + f"                  <Bezeichnung_Planung_Gruppe>" + "\n" \
             + f"                    <Wert>Neubau ESTW-A Scheibenberg</Wert>" + "\n" \
             + f"                  </Bezeichnung_Planung_Gruppe>" + "\n" \
             + f"                  <Bezeichnung_Unteranlage>" + "\n" \
             + f"                    <Wert>ESTW-A Scheibenberg</Wert>" + "\n" \
             + f"                  </Bezeichnung_Unteranlage>" + "\n" \
             + f"                  <Planungsbuero>" + "\n" \
             + f"                    <Identitaet>" + "\n" \
             + f"                      <Wert>55555555-5555-5555-5555-555555555555</Wert>" + "\n" \
             + f"                    </Identitaet>" + "\n" \
             + f"                    <Name_Organisation>" + "\n" \
             + f"                      <Wert>HPI-OSM</Wert>" + "\n" \
             + f"                    </Name_Organisation>" + "\n" \
             + f"                  </Planungsbuero>" + "\n" \
             + f"                </Planung_G_Schriftfeld>" + "\n" \
             + f"                <Polygone_Betrachtungsbereich>" + "\n" \
             + f"                  <Koordinatensystem_BB>" + "\n" \
             + f"                    <Wert>WGS84</Wert>" + "\n" \
             + f"                  </Koordinatensystem_BB>" + "\n" \
             + f"                  <Polygonzug_Betrachtungsbereich>" + "\n" \
             + f"                    <Wert>4541324.55 5647860.25 4533627.31 5629542.69 4530892.30 5615315.52 4530896.25 5615314.81 4535700.32 5625130.79 4541007.74 5647040.74</Wert>" + "\n" \
             + f"                  </Polygonzug_Betrachtungsbereich>" + "\n" \
             + f"                </Polygone_Betrachtungsbereich>" + "\n" \
             + f"                <Polygone_Planungsbereich>" + "\n" \
             + f"                  <Koordinatensystem_PB>" + "\n" \
             + f"                    <Wert>WGS84</Wert>" + "\n" \
             + f"                  </Koordinatensystem_PB>" + "\n" \
             + f"                  <Polygonzug_Planungsbereich>" + "\n" \
             + f"                    <Wert>4534953.69 5631722.21 4535060.27 5631655.77 4534117.81 5629091.17 4534190.47 5629031.56 4534190.47 5626410.63 4534541.42 5626126.37 4534451.48 5625924.01 4533883.87 5626227.30 4533883.87 5625744.61 4533648.18 5624927.37 4533444.84 5624987.20 4533963.42 5627558.05 4533627.31 5629542.69 4533935.67 5628728.88 4533950.34 5629188.21</Wert>" + "\n" \
             + f"                  </Polygonzug_Planungsbereich>" + "\n" \
             + f"                </Polygone_Planungsbereich>" + "\n" \
             + f"              </LST_Planung_Gruppe>" + "\n" \
             + f"              <Planung_P_Allg>" + "\n" \
             + f"                <Bezeichnung_Planung_Projekt>" + "\n" \
             + f"                  <Wert>Neubau ESTW Scheibenberg</Wert>" + "\n" \
             + f"                </Bezeichnung_Planung_Projekt>" + "\n" \
             + f"                <Datum_Abschluss_Projekt>" + "\n" \
             + f"                  <Wert>2017-12-31</Wert>" + "\n" \
             + f"                </Datum_Abschluss_Projekt>" + "\n" \
             + f"                <Projekt_Nummer>" + "\n" \
             + f"                  <Wert>1234ABCD5678EFGH</Wert>" + "\n" \
             + f"                </Projekt_Nummer>" + "\n" \
             + f"                <Projektleiter>" + "\n" \
             + f"                  <Identitaet>" + "\n" \
             + f"                    <Wert>3C590A15-5293-4AF6-A81D-1C4E82297602</Wert>" + "\n" \
             + f"                  </Identitaet>" + "\n" \
             + f"                  <Akteur_Allg>" + "\n" \
             + f"                    <Name_Akteur>" + "\n" \
             + f"                      <Wert>Boockmeyer</Wert>" + "\n" \
             + f"                    </Name_Akteur>" + "\n" \
             + f"                    <Name_Akteur_10>" + "\n" \
             + f"                      <Wert>Boockmeyer</Wert>" + "\n" \
             + f"                    </Name_Akteur_10>" + "\n" \
             + f"                    <Name_Akteur_5>" + "\n" \
             + f"                      <Wert>Boock</Wert>" + "\n" \
             + f"                    </Name_Akteur_5>" + "\n" \
             + f"                  </Akteur_Allg>" + "\n" \
             + f"                  <Kontaktdaten>" + "\n" \
             + f"                    <Identitaet>" + "\n" \
             + f"                      <Wert>55555555-5555-5555-5555-555555555555</Wert>" + "\n" \
             + f"                    </Identitaet>" + "\n" \
             + f"                    <Name_Organisation>" + "\n" \
             + f"                      <Wert>HPI-OSM</Wert>" + "\n" \
             + f"                    </Name_Organisation>" + "\n" \
             + f"                  </Kontaktdaten>" + "\n" \
             + f"                </Projektleiter>" + "\n" \
             + f"              </Planung_P_Allg>" + "\n" \
             + f"            </LST_Planung_Projekt>" + "\n" \
             + f"    </Objektmanagement>" + "\n" \
             + f"  </LST_Planung>" + "\n" \
             + f"</nsPlanPro:PlanPro_Schnittstelle>" + "\n"

    @staticmethod
    def get_root_uuids():
        return [RootXML.ausgabe_fachdaten_uuid, RootXML.accommondation_uuid, RootXML.external_element_control_uuid]
