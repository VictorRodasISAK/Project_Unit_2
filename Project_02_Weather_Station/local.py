#collects data from local arduino connected to 3 sensors and saves it to local file and to server

from proj2_lib import *
import time

def main():
    s1 = create_new_sensor("s1", "Temperature", "room")
    for _ in range(576):
        data = read_ardruino()
        save_localy(data)
        new_record(data, sensor_id=s1)
        time.sleep(300)
    