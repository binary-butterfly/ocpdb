# encoding: utf-8

"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2021 binary butterfly GmbH

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

test_dataset = """
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <GetChargePointListResponse xmlns="http://ochp.eu/1.4">
         <result>
            <resultCode>
               <resultCode>ok</resultCode>
            </resultCode>
            <resultDescription>Data accepted and processed.</resultDescription>
         </result>
         <chargePointInfoArray>
            <evseId>DE1ESE001301</evseId>
            <locationId>DE1ESS0013</locationId>
            <timestamp>
               <DateTime>2020-05-06T08:03:02Z</DateTime>
            </timestamp>
            <locationName>erdgas schwaben Nersingen</locationName>
            <locationNameLang>DEU</locationNameLang>
            <images>
               <uri>https://www.ladestationsinformationssystem.de/lisy2-web/service/rest/public/images/21497699</uri>
               <thumbUri>https://www.ladestationsinformationssystem.de/lisy2-web/service/rest/public/images/thumbnail/21497699</thumbUri>
               <class>ownerLogo</class>
               <type>png</type>
            </images>
            <images>
               <uri>https://www.ladestationsinformationssystem.de/lisy2-web/service/rest/public/images/89</uri>
               <thumbUri>https://www.ladestationsinformationssystem.de/lisy2-web/service/rest/public/images/thumbnail/89</thumbUri>
               <class>networkLogo</class>
               <type>png</type>
            </images>
            <images>
               <uri>https://www.ladestationsinformationssystem.de/lisy2-web/service/rest/public/images/21497691</uri>
               <thumbUri>https://www.ladestationsinformationssystem.de/lisy2-web/service/rest/public/images/thumbnail/21497691</thumbUri>
               <class>operatorLogo</class>
               <type>png</type>
            </images>
            <relatedResource>
               <uri>https://direct.emobilitycloud.com/dp/station/de1es/de1ess0013</uri>
               <class>operatorPayment</class>
            </relatedResource>
            <chargePointAddress>
               <houseNumber>11</houseNumber>
               <address>Schulstrasse</address>
               <city>Nersingen</city>
               <zipCode>89278</zipCode>
               <country>DEU</country>
            </chargePointAddress>
            <chargePointLocation lat="48.427389" lon="10.122389"/>
            <timeZone>Europe/Berlin</timeZone>
            <openingTimes>
               <twentyfourseven>true</twentyfourseven>
               <closedCharging>false</closedCharging>
            </openingTimes>
            <status>
               <ChargePointStatusType>Operative</ChargePointStatusType>
            </status>
            <telephoneNumber>08219002459</telephoneNumber>
            <location>
               <GeneralLocationType>parking-lot</GeneralLocationType>
            </location>
            <parkingSpot>
               <parkingId>DP1PSP001301</parkingId>
               <restriction>
                  <RestrictionType>evonly</RestrictionType>
               </restriction>
               <restriction>
                  <RestrictionType>plugged</RestrictionType>
               </restriction>
            </parkingSpot>
            <authMethods>
               <AuthMethodType>OperatorAuth</AuthMethodType>
            </authMethods>
            <authMethods>
               <AuthMethodType>RfidMifareCls</AuthMethodType>
            </authMethods>
            <authMethods>
               <AuthMethodType>OchpDirectAuth</AuthMethodType>
            </authMethods>
            <authMethods>
               <AuthMethodType>RfidMifareDes</AuthMethodType>
            </authMethods>
            <connectors>
               <connectorStandard>
                  <ConnectorStandard>IEC_62196_T2</ConnectorStandard>
               </connectorStandard>
               <connectorFormat>
                  <ConnectorFormat>Socket</ConnectorFormat>
               </connectorFormat>
            </connectors>
            <connectors>
               <connectorStandard>
                  <ConnectorStandard>DOMESTIC_F</ConnectorStandard>
               </connectorStandard>
               <connectorFormat>
                  <ConnectorFormat>Socket</ConnectorFormat>
               </connectorFormat>
            </connectors>
            <chargePointType>AC</chargePointType>
            <ratings>
               <maximumPower>22.0</maximumPower>
            </ratings>
            <userInterfaceLang>DEU</userInterfaceLang>
         </chargePointInfoArray>
         <chargePointInfoArray>
            <evseId>DE1ESE000201</evseId>
            <locationId>DE1ESS0002</locationId>
            <timestamp>
               <DateTime>2020-05-04T06:30:42Z</DateTime>
            </timestamp>
            <locationName>erdgas schwaben Günzburg1</locationName>
            <locationNameLang>DEU</locationNameLang>
            <images>
               <uri>https://www.ladestationsinformationssystem.de/lisy2-web/service/rest/public/images/21497699</uri>
               <thumbUri>https://www.ladestationsinformationssystem.de/lisy2-web/service/rest/public/images/thumbnail/21497699</thumbUri>
               <class>ownerLogo</class>
               <type>png</type>
            </images>
            <images>
               <uri>https://www.ladestationsinformationssystem.de/lisy2-web/service/rest/public/images/21497691</uri>
               <thumbUri>https://www.ladestationsinformationssystem.de/lisy2-web/service/rest/public/images/thumbnail/21497691</thumbUri>
               <class>operatorLogo</class>
               <type>png</type>
            </images>
            <images>
               <uri>https://www.ladestationsinformationssystem.de/lisy2-web/service/rest/public/images/89</uri>
               <thumbUri>https://www.ladestationsinformationssystem.de/lisy2-web/service/rest/public/images/thumbnail/89</thumbUri>
               <class>networkLogo</class>
               <type>png</type>
            </images>
            <relatedResource>
               <uri>https://direct.emobilitycloud.com/dp/station/de1es/de1ess0002</uri>
               <class>operatorPayment</class>
            </relatedResource>
            <chargePointAddress>
               <houseNumber>3</houseNumber>
               <address>Geschwister-Scholl-Straße</address>
               <city>Günzburg</city>
               <zipCode>89312</zipCode>
               <country>DEU</country>
            </chargePointAddress>
            <chargePointLocation lat="48.446038" lon="10.283219"/>
            <timeZone>Europe/Berlin</timeZone>
            <openingTimes>
               <twentyfourseven>true</twentyfourseven>
               <closedCharging>false</closedCharging>
            </openingTimes>
            <status>
               <ChargePointStatusType>Operative</ChargePointStatusType>
            </status>
            <telephoneNumber>08219002459</telephoneNumber>
            <location>
               <GeneralLocationType>on-street</GeneralLocationType>
            </location>
            <parkingSpot>
               <parkingId>DP1PSP000201</parkingId>
               <restriction>
                  <RestrictionType>evonly</RestrictionType>
               </restriction>
               <restriction>
                  <RestrictionType>plugged</RestrictionType>
               </restriction>
            </parkingSpot>
            <authMethods>
               <AuthMethodType>OperatorAuth</AuthMethodType>
            </authMethods>
            <authMethods>
               <AuthMethodType>RfidMifareDes</AuthMethodType>
            </authMethods>
            <authMethods>
               <AuthMethodType>RfidMifareCls</AuthMethodType>
            </authMethods>
            <authMethods>
               <AuthMethodType>OchpDirectAuth</AuthMethodType>
            </authMethods>
            <connectors>
               <connectorStandard>
                  <ConnectorStandard>IEC_62196_T2</ConnectorStandard>
               </connectorStandard>
               <connectorFormat>
                  <ConnectorFormat>Socket</ConnectorFormat>
               </connectorFormat>
            </connectors>
            <connectors>
               <connectorStandard>
                  <ConnectorStandard>DOMESTIC_F</ConnectorStandard>
               </connectorStandard>
               <connectorFormat>
                  <ConnectorFormat>Socket</ConnectorFormat>
               </connectorFormat>
            </connectors>
            <chargePointType>AC</chargePointType>
            <ratings>
               <maximumPower>22.0</maximumPower>
            </ratings>
            <userInterfaceLang>DEU</userInterfaceLang>
         </chargePointInfoArray>
         <chargePointInfoArray>
            <evseId>DEAMPE07612</evseId>
            <locationId>DEAMPS0761</locationId>
            <timestamp>
                <DateTime>2021-04-25T09:50:15Z</DateTime>
                </timestamp>
            <locationName>fleur ami 1</locationName>
            <locationNameLang>DEU</locationNameLang>
            <images>
                <uri>https://www.ladestationsinformationssystem.de/lisy2-web/service/rest/public/images/23898794</uri>
                <thumbUri>https://www.ladestationsinformationssystem.de/lisy2-web/service/rest/public/images/thumbnail/23898794</thumbUri>
                <class>ownerLogo</class>
                <type>png</type>
            </images>
            <images>
                <uri>https://www.ladestationsinformationssystem.de/lisy2-web/service/rest/public/images/7261754</uri>
                <thumbUri>https://www.ladestationsinformationssystem.de/lisy2-web/service/rest/public/images/thumbnail/7261754</thumbUri>
                <class>networkLogo</class>
                <type>png</type>
            </images>
            <images>
                <uri>https://www.ladestationsinformationssystem.de/lisy2-web/service/rest/public/images/23898792</uri>
                <thumbUri>https://www.ladestationsinformationssystem.de/lisy2-web/service/rest/public/images/thumbnail/23898792</thumbUri>
                <class>operatorLogo</class>
                <type>png</type>
            </images>
            <chargePointAddress>
                <houseNumber>6</houseNumber>
                <address>Höhenhöfe</address>
                <city>Tönisvorst</city>
                <zipCode>47918</zipCode>
                <country>DEU</country>
            </chargePointAddress>
            <chargePointLocation lat="51.313641" lon="6.476685"/>
            <timeZone>Europe/Berlin</timeZone>
            <openingTimes>
                <regularHours weekday="2" periodBegin="08:00" periodEnd="20:00"/>
                <regularHours weekday="4" periodBegin="08:00" periodEnd="20:00"/>
                <regularHours weekday="6" periodBegin="10:00" periodEnd="16:00"/>
                <regularHours weekday="5" periodBegin="07:00" periodEnd="20:00"/>
                <regularHours weekday="3" periodBegin="08:00" periodEnd="20:00"/>
                <regularHours weekday="1" periodBegin="08:00" periodEnd="20:00"/>
                <closedCharging>false</closedCharging>
            </openingTimes>
            <status>
                <ChargePointStatusType>Operative</ChargePointStatusType>
            </status>
            <location>
                <GeneralLocationType>parking-lot</GeneralLocationType>
            </location>
            <parkingSpot>
                <parkingId>DPAMPP07612</parkingId>
            </parkingSpot>
            <authMethods>
                <AuthMethodType>RfidMifareCls</AuthMethodType>
            </authMethods>
            <authMethods>
                <AuthMethodType>OchpDirectAuth</AuthMethodType>
            </authMethods>
            <authMethods>
                <AuthMethodType>RfidMifareDes</AuthMethodType>
            </authMethods>
            <connectors>
                <connectorStandard>
                    <ConnectorStandard>IEC_62196_T2</ConnectorStandard>
                </connectorStandard>
                <connectorFormat>
                    <ConnectorFormat>Socket</ConnectorFormat>
                </connectorFormat>
            </connectors>
            <chargePointType>AC</chargePointType>
            <ratings>
                <maximumPower>22.0</maximumPower>
            </ratings>
            <userInterfaceLang>DEU</userInterfaceLang>
        </chargePointInfoArray>
      </GetChargePointListResponse>
   </soap:Body>
</soap:Envelope>
"""

