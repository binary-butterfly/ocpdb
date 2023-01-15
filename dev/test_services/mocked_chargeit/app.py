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

import json

from flask import Flask, jsonify

app = Flask('mocked_chargeit')


@app.route('/ps/rest/feed')
def get_feed():
    with open('./full_data.json') as json_file:
        json_data = json.loads(json_file.read())
    return jsonify(json_data), 200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
