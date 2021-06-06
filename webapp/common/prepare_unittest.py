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

import pymysql
from urllib.parse import urlparse
from flask import current_app


def prepare_unittest():
    if current_app.config['MODE'] != 'DEVELOPMENT' or not current_app.config['DEBUG']:
        print('wrong mode')
        return

    url = urlparse(current_app.config['SQLALCHEMY_DATABASE_URI'])
    connection = pymysql.connect(
        host=url.hostname,
        user=url.username,
        password=url.password,
        db=url.path[1:],
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    with connection.cursor() as cursor:
        for line in truncate_dbs.split("\n"):
            if not line:
                continue
            cursor.execute(line)
    connection.commit()


truncate_dbs = '''
SET FOREIGN_KEY_CHECKS=0;
TRUNCATE `action`;
TRUNCATE `cashpoint`;
TRUNCATE `hardware`;
TRUNCATE `pricegroup`;
TRUNCATE `token`;
TRUNCATE `unit`;
SET FOREIGN_KEY_CHECKS=1;
'''
