#collects Project_02_CSV_Files from local arduino connected to 3 sensors and saves it to local file and to server

from Project_02_Library import *
import time

def do_measurement(s1t, s2t, s3t, s1h, s2h, s3h):
    d1, d2, d3 = read_ardruino()
    save_localy(data=d1, file_name="../Project_02_CSV_Files/Project_02_CSV_S1.csv")
    save_localy(data=d2, file_name="../Project_02_CSV_Files/Project_02_CSV_S2.csv")
    save_localy(data=d3, file_name="../Project_02_CSV_Files/Project_02_CSV_S3.csv")

    new_record(d1[1], sensor_id=s1t)
    new_record(d1[0], sensor_id=s1h)
    new_record(d2[1], sensor_id=s2t)
    new_record(d2[0], sensor_id=s2h)
    new_record(d3[1], sensor_id=s3t)
    new_record(d3[0], sensor_id=s3h)

def create_all_sensors():
    s1t = create_new_sensor("s1", "Temperature", "room")
    s2t = create_new_sensor("s2", "Temperature", "room")
    s3t = create_new_sensor("s3", "Temperature", "room")
    s1h = create_new_sensor("s1", "Humidity", "room")
    s2h = create_new_sensor("s2", "Humidity", "room")
    s3h = create_new_sensor("s3", "Humidity", "room")
    print(s1t, s2t, s3t, s1h, s2h, s3h)
    return s1t, s2t, s3t, s1h, s2h, s3h

def main():
    s1t, s2t, s3t, s1h, s2h, s3h = create_all_sensors()
    for _ in range(576):
        do_measurement(s1t, s2t, s3t, s1h, s2h, s3h)
        time.sleep(300)

    