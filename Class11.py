"""
Today's Topics
1) Create SQLight3 database
2)
3)
4)
"""
# ################################

import sqlite3
db = sqlite3.connect("class_11.db")
cur = db.cursor()

USERS = {
    'id': 'Interger Primary Key',
    'name': 'TEXT',
    'Phone': 'TEXT',
    'email': 'TEXT unique',
    'password': 'TEXT',

}

command = "Create table if not exists users("
command += ", ".join([
    "{} {}".format(key, value) for key, value in USERS.items()
])
command +=")"

cur.execute(command)
db.close()


class DatabaseORM(object):
    """
    Database ORM
    """

    def __init__(self):
        """initialize class object"""
        self.com = None
        self.cur = None
        self.data = None
        self.database_info = dict()
        self.methods = {
            'create_table': self.create_table,
            'insert_record':self.Insert_record}

    def main(self, **kwargs):
        """
        Main Method of class
        :return:
        """
        self.create_db_connection()
        self.create_cursor()

        self.data = kwargs.get('data')
        method = kwargs.get('method')

        if method not in self.methods:
            return {
                'status': False,
                'message': 'Method does not supported.'
            }

        self.methods.get(method)()
    def create_db_connection(self):
        """
        Create database connection
        :return:
        """
        self.com = sqlite3.connect("class_11.db")

    def create_cursor(self):
        """
        Create database cursor
        :return:
        """
        self.cur = self.com.cursor()
    def generate_create_table_command(self):
        """
        Generate Create table commnad based on self.data
        :return:
        """
        statement = "CREATE TABLE IF NOT EXISTS {} (".format (
            self.data.get('table_name')
        )

        statement +=", ".join([
            "{} {}".format(key, value)
            for key, value in self.data.get('table_structure').items()
        ])
        statement += ")"

        return statement

    def create_table(self):
        """
        Create table
        :returm:
        """
        command = self.generate_create_table_command()
        try:
            self.cur.execute(command)
            print("Table has been created. ")
        except Exception as err:
            print(F"Due to following error Table has not been created\n{err}")

    def generate_insert_statement(self):
        """
        Generate insert statement based on the provided data
        :return:
        """
        insert_data = self.data.get('insert_data')
        _field = ", ".join([
            field for field in self.data.get('insert_data').key()
        ])
        place_holder = ", ".join(['?' for value in insert_data.value()])

        return F"INSERT INTO {self.data.get('table_name')}({_field}) " \
            F"VALUES({place_holder})"

    def insert_record(self):
        """
        Insert record in specified record
        :return:
        """
        print('Insert Record')
        self.prepare_insert_statement()

    def __del__(self):
         """
         :return:
         """
         self.com.close()

DatabaseORM().main(**{
    'method': 'create_table',
    'data': {
        'table_name': 'user',
        'table_structure': {
            'id': 'Interger Primary Key',
            'name': 'TEXT',
            'Phone': 'TEXT',
            'email': 'TEXT unique',
            'password': 'TEXT',
        }
    }
})