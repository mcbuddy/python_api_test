# ../platform/spec/metastore_api_test.py
#!/bin/env python

import requests
import unittest
import MySQLdb, MySQLdb.cursors
import sys
import argparse

class ApiTest(unittest.TestCase):
    def setUp(self):
        self.url = url
        self.conn = MySQLdb.connect(host=db_host, db=db_name, user=db_user)
        self.cursor = MySQLdb.cursors.DictCursor(self.conn)

    def test_get_something(self):
        name = 'anything'
        # api get call
        resp = requests.get(self.url + '/get_something/' + name)
        data = resp.json()

        # db query
        self.cursor.execute("select * from something where name = '" + name + "';")
        query = self.cursor.fetchone()

        # Assertion
        self.assertEqual(query['id'], data['id'])
        self.assertEqual(query['name'], data['name'])

    def test_post_something(self):
        # api get call
        resp = requests.get(self.url + '/post_something/', data = {'name':'anything'}
        data = resp.json()

        # db query
        self.cursor.execute("select * from something where name = 'anything';")
        query = self.cursor.fetchone()

        # Assertion
        self.assertEqual(query['id'], data['id'])
        self.assertEqual(query['name'], data['name'])

    def tearDown(self):
        self.conn.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', default='qa')
    parser.add_argument('unittest_args', nargs='*')

    args = parser.parse_args()
    if args.input == 'qa':
        url = 'http://your-qa-server.com'
        db_host = 'your_db_server'
        db_name = 'db_name'
        db_user = 'db_user'
    elif args.input == 'uat':
        url = 'http://your-uat-server.com'
        db_host = 'your_db_server'
        db_name = 'db_name'
        db_user = 'db_user'
    else:
        raise ValueError('Wrong Environment selection, Please use qa or uat when using -i or --input=')

    sys.argv[1:] = args.unittest_args
    unittest.main()
