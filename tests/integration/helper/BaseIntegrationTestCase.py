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


import os
import pymysql
from urllib.parse import urlparse
from flask import current_app
from webapp import launch
from webapp.extensions import db
from tests.helper import BaseTestCase


class BaseIntegrationTestCase(BaseTestCase):
    run_reset_database = True

    def setUp(self):
        super().setUp()
        launch().app_context().push()

        if current_app.config['MODE'] != 'DEVELOPMENT' or not current_app.config['DEBUG']:
            raise Exception('wrong mode')

        if self.run_reset_database:
            self.reset_database()

    def reset_database(self):
        url = urlparse(current_app.config['SQLALCHEMY_DATABASE_URI'])
        connection = pymysql.connect(
            host=url.hostname,
            user=url.username,
            password=url.password,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        with connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            with open(os.path.join(current_app.config['TESTS_DIR'], 'files', 'reset.sql')) as reset_sql_file:
                for line in reset_sql_file.readlines():
                    if not line or not line.strip() or line.startswith('--'):
                        continue
                    cursor.execute(line)
            connection.commit()
            cursor.execute("USE ocpdb")
            connection.commit()
            cache = ''
            with open(os.path.join(current_app.config['TESTS_DIR'], 'files', 'base.sql')) as base_sql_file:
                for line in base_sql_file.readlines():
                    if not line or not line.strip() or line.strip().startswith('--'):
                        continue
                    if line.strip()[-1] != ';':
                        cache += ' ' + line
                        continue
                    cursor.execute(cache + ' ' + line)
                    cache = ''
            cursor.execute("SET FOREIGN_KEY_CHECKS=1;")
            connection.commit()

    def tearDown(self):
        db.session.remove()
