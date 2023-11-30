#collects data from local arduino connected to 3 sensors and saves it to local file and to server

from proj2_lib import *
import time

def main():
    s1t = create_new_sensor("s1", "Temperature", "room")
    s2t = create_new_sensor("s2", "Temperature", "room")
    s3t = create_new_sensor("s3", "Temperature", "room")
    s1h = create_new_sensor("s1", "Humidity", "room")
    s2h = create_new_sensor("s2", "Humidity", "room")
    s3h = create_new_sensor("s3", "Humidity", "room")
    for _ in range(576):
        d1, d2, d3 = read_ardruino()
        save_localy(d1, "s1.csv")
        save_localy(d2, "s2.csv")
        save_localy(d3, "s3.csv")

        new_record(d1[0], sensor_id=s1t)
        new_record(d1[1], sensor_id=s1h)
        new_record(d2[0], sensor_id=s2t)
        new_record(d2[1], sensor_id=s2h)
        new_record(d3[0], sensor_id=s3t)
        new_record(d3[1], sensor_id=s3h)

        time.sleep(300)

    