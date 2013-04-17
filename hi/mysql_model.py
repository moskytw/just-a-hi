#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
from mosql.result import Model

class DummyPool(object):

    def getconn(self):
        return MySQLdb.connect(user='root', db='mosky')

    def putconn(self, conn):
        conn.close()

class PostgreSQLModel(Model):
    pool = DummyPool()
    dump_sql = True

class Person(PostgreSQLModel):
    table_name = 'person'
    column_names = ('person_id', 'name')
    identify_by = ('person_id', )

class Detail(PostgreSQLModel):
    table_name = 'detail'
    column_names = ('detail_id', 'person_id', 'key', 'val')
    identify_by = ('detail_id', )
    group_by = ('person_id', 'key')

class PersonDetail(Detail):
    join_table_names = ('person', )
    column_names = ('person_id', 'detail_id', 'key', 'val', 'name')
    group_by = ('person_id', 'key', 'name')
