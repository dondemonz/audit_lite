import psycopg2
from psycopg2.extras import DictCursor


class DbHelper:

    def __init__(self, host=None, dbname=None, user=None, password=None, records=None):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.records = records
        self.connection = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
        self.connection.autocommit = True

    def check_db_events(self, event_time):
        with self.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute("SELECT * FROM audit_events WHERE event_time >=%s and event_action = 24", (event_time,))
                self.records = cursor.fetchall()
                print("records", self.records)
        cursor.close()
        return conn

    def check_db_objects(self, event_id):
        with self.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute("SELECT * FROM audit_objects WHERE event_id = %s", (event_id,))
                self.records = cursor.fetchall()
                #print("records", self.records)
        cursor.close()
        return conn

    def check_db_intervals(self, event_id):
        with self.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute("SELECT * FROM audit_intervals WHERE event_id =%s", (event_id,))
                self.records = cursor.fetchall()
                #print("records", self.records)
        cursor.close()
        return conn


#cursor.execute('SELECT * FROM audit_events WHERE event_action=%s', (event_action,))
    #CONVERT_TZ(created_at, '+00:00', '+08:00')   between     "2018-01-24" and "2018-01-25"

    def clean_db(self):
        with self.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute('DELETE FROM audit_events')
                conn.commit()
        cursor.close()


    def close_connection(self):
        self.connection.close()
        print("close")




