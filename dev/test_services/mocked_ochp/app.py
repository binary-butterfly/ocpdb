"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2022 binary butterfly GmbH

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

from flask import Flask, jsonify, Response

app = Flask('mocked_ochp')


def xml_response(xml_data: bytes):
    return Response(
        xml_data,
        content_type='text/xml; charset=ISO-8859-1',
    )


@app.route('/service/ochp/v1.4', methods=['POST'])
def get_ochp():
    with open('./test_data.xml') as xml_file:
        xml_data = xml_file.read()
    return xml_response(xml_data=xml_data.encode('latin-1')), 200


@app.route('/live/ochp/v1.4', methods=['POST'])
def get_ochp_live():
    with open('./live_data.xml') as xml_file:
        xml_data = xml_file.read()
    return xml_response(xml_data=xml_data.encode('latin-1')), 200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

