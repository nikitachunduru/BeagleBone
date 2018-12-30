import sys
from thread import start_new

import mysql
from mysql.connector import Error

from recording_thread import RecordingThread
from scheduler_creator import loadSchedules

'''
Run me to start.

Edit the parameters.py file for things like database connection parameters.
'''

def main(argv):
    reloadSchedulesFromDatabase()

    return 0

def reloadSchedulesFromDatabase():
    # Load the schedules from the database
    schedules = loadSchedules()

    threads = []

    for parameters in schedules:
        recordingThread = RecordingThread(parameters)
        recordingThread.start()
        threads.append(recordingThread)

    for thread in threads:
        thread.join()

# Save the given recording to the database.
def saveRecording(rssiValues, recordingFilename, scheduleId):
    try:
        connection = mysql.connector.connect(host=DB_HOSTNAME,
                                             database=DB_NAME,
                                             user=DB_USER,
                                             password=DB_PASSWORD)
        if connection.is_connected():
            cursor = connection.cursor()

            # Insert the given rssi values and recording filename into the recordings table
            recordingFile = readFile(recordingFilename)
            cursor.execute(
                "INSERT INTO recordings (schedule, RSSI_file, recording) VALUES ({}, {}, {})".format(
                    scheduleId,
                    rssiValues,
                    recordingFile
                )
            )
        else:
            raise RuntimeError("Could not connect to database")
    except Error as e:
        print ("Error while connecting to MySQL", e)
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()


# Load the file into memory and return it.
def readFile(filename):
    with open(filename, 'rb') as f:
        photo = f.read()
    return photo


if __name__ == '__main__':
    # Pass any command line args to the main function and make the process exit with the return code returned from main()
    sys.exit(main(sys.argv))