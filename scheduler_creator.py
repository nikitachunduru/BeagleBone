import mysql.connector
from mysql.connector import Error

from parameters import *

def loadSchedules():
    try:
        connection = mysql.connector.connect(host=DB_HOSTNAME,
                                             database=DB_NAME,
                                             user=DB_USER,
                                             password=DB_PASSWORD)
        if connection.is_connected():
            cursor = connection.cursor()

            schedules = []

            # Create query to load the schedule records from the database and return a dictionary of the parameters
            # TODO: finish this
            cursor.execute("select * from test_table")

            for row in cursor.fetchall():
                # For each row in the result set create a dictionary of "parameters" for the scheduled job
                # TODO: finish this
                params = dict()
                params['timestamp'] = ''
                params['repeat'] = True
                params['frequency'] = 800
                params['filename'] = 'myFilename'
                schedules.append(params)

            return schedules
        else:
            raise RuntimeError("Could not connect to database")
    except Error as e:
        print ("Error while connecting to MySQL", e)
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()