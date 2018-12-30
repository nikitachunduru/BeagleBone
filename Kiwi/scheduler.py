"""
Demonstrates how to schedule a job to be run in a process pool on 3 second intervals.
"""
# from kiwirecorder import kiwirecorder
from datetime import datetime
from record import record as rssi_record

import logging
import os

from apscheduler.schedulers.background import BackgroundScheduler

logger = logging.getLogger(__name__)
logging.basicConfig()

class Scheduler:
    def __init__(self):
        # intervals = input('how many seconds?')
        logger.info("start")
        self.scheduler = BackgroundScheduler(logger=logger)
        # scheduler.add_job(information, 'interval', seconds=15)
        print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

        self.scheduler.start()

    def addJob(self, params):
        self.scheduler.add_job(self._record, 'date', run_date=params['time'], args=[params])
        
    def _record(self, params):
        rssi_record(params['station'], params['port'], params['freq'], params['mode'], params['duration'], params['schedule_id'])

    def stop(self):
        self.scheduler.shutdown()

if __name__ == '__main__':
    scheduler = Scheduler()

    from datetime import datetime, timedelta
    import time as t
    time = datetime.now() + timedelta(seconds=10)   

    scheduler.addJob({ "station": "hat2018.twrmon.net", "port": 8075, "freq": 800, "mode": "am", "time": time, "schedule_id": 31, "duration": 10})

    t.sleep(15)
    scheduler.stop()