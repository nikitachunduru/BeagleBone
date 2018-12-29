"""
Demonstrates how to schedule a job to be run in a process pool on 3 second intervals.
"""
# from kiwirecorder import kiwirecorder
from datetime import datetime
from record import record

import logging
import os

from apscheduler.schedulers.blocking import BlockingScheduler

logger = logging.getLogger(__name__)
logging.basicConfig()

def information():
    record("hat2018.twrmon.net", 8075, 800, "am", 10)

if __name__ == '__main__':
    # intervals = input('how many seconds?')
    scheduler = BlockingScheduler(logger=logger)
    scheduler.add_job(information, 'interval', seconds=15)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass