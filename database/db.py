# -*- coding: utf-8 -*-
import psycopg2
from psycopg2 import pool

from config_reader import NoveConfiguration


class Database:

    # def __repr__(self):
    # return 'DB(url=%s)' % self._host

    def __init__(self):
        configuration = NoveConfiguration()
        pass

    def session(self):
        configuration = NoveConfiguration()
        self._host = configuration.postgres_host
        self._user = configuration.postgres_user
        self._password = configuration.postgres_password
        self._port = configuration.postgres_port
        self._database = configuration.postgres_database


    def session(self):
        self._driver = psycopg2.connect(host='localhost', user='alejes', password='alejes', port='5432',
                                        database='proyectof')

        #self._driver = psycopg2.connect(host=self._host, user=self._user, password=self._password, port=self._port,
                                        #database=self._database)

        if self._driver:
            print("connection pool created successfully")
        #return self._driver.getconn()
        return self._driver