# -*- coding: utf-8 -*-
from database import Database

class Users:
    def __init__(self, users):

        self._id = users.get('id', False)
        self._name = users.get('name', False)
        self._password = users.get('password', False)
    
    @staticmethod
    def browse_user(id):
        browse_user_query = """ select * from users where id={id}""".format(id=id)
        db = Database()
        ps_connection = db.session()
        ps_cursor = ps_connection.cursor() 
        ps_cursor.execute(browse_user_query)
        user = ps_cursor.fetchone()
        ps_cursor.close()
        return user

    @staticmethod
    def browse_columns():
        browse_user_query = """ select * from users """
        db = Database()
        ps_connection = db.session()
        ps_cursor = ps_connection.cursor()
        ps_cursor.execute(browse_user_query)
        user = ps_cursor.fetchone()
        ps_cursor.close()
        return user

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name
    
    @property
    def password(self):
        return self._password

    @id.setter
    def id_user(self, id):
        self._id = id

    @name.setter
    def name(self, name):
        self._name = name
    
    @password.setter
    def password(self, password):
        self._password = password

    

        