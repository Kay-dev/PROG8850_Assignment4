import unittest
import mysql.connector

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.conn = mysql.connector.connect(
            user='root',
            password='admin8960392',
            host='localhost',
            database='subscriptions'
        )
        # disable auto commit
        self.conn.autocommit = False
        self.cursor = self.conn.cursor()
        # start a transaction
        self.cursor.execute("START TRANSACTION")

    def tearDown(self):
        self.conn.rollback()
        self.conn.close()

    def test_insert_employee(self):
        self.cursor.execute(
            "INSERT INTO subscribers (username, email) VALUES (%s, %s)",
            ('Jasleen Kaur', 'JasleenKaur@gmail.com')
        )

        self.cursor.execute("SELECT LAST_INSERT_ID()")
        inserted_id = self.cursor.fetchone()[0]
        self.cursor.execute("SELECT * FROM subscribers WHERE id = %s", (inserted_id,))
        result = self.cursor.fetchone()
        self.assertEqual(result[1], 'Jasleen Kaur')  # Check if the name matches

if __name__ == '__main__':
    unittest.main()