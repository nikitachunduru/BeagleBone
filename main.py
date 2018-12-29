import sys

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

    for parameters in schedules:
        print('TODO: create scheduler with params: {}'.format(parameters))

    print(schedules)


if __name__ == '__main__':
    # Pass any command line args to the main function and make the process exit with the return code returned from main()
    sys.exit(main(sys.argv))