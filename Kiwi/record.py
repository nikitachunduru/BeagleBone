import subprocess
import re


def record(station, port, freq, mode, time):
    """Record takes a string station (web address), an integer port, an integer freq, a string mode, and a integer time
     in seconds, and returns the RSSI data of the recording being saved, as a list of floats.
    The recording is saved in the directory that the script is run on under the default file name,
     which has the format (YYYYMMDDTHHMMSSZ_station_mode).wav"""
    command = ["python", "kiwirecorder.py", "-k", str(30), "-s", str(station), "-p", str(port), "-f", str(freq), "-m", mode,
               "--tlimit="+str(time), "-d", "audioFiles"]
    data = subprocess.Popen(command, stdout=subprocess.PIPE)
    output = data.communicate()[0]
    d =  re.sub("\r  ", ",", re.sub("Block: [0-9a-f]*, RSSI:", "", output)).split(",")[1:-1]
    return [float(i) for i in d]
