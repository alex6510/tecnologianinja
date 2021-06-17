# -*- coding: utf-8 -*-
import psycopg2
from psycopg2 import pool

from config_reader import NoveConfiguration

class Database:
    def session(self):
        return self._driver.get_conn()
    def __repr__(self):
        return 'DB(url=%s)' % self._host
    def __int__(self):
        configuration = NoveConfiguration()
        self._host = configuration.postgres_host
        self._user = configuration.postgres_user
        self._password = configuration.postgres_password
        self._port = configuration.postgres_port
        self._database = configuration.postgres_database
        self._driver = psycopg2.pool.SimpleConnectionPool(1, 20,
                        host = self._host,
                        user = self._user,
                        password = self._password,
                        port = self._port,
                        database = self._database)
        if self._driver:
            print("connection pool created successfully")