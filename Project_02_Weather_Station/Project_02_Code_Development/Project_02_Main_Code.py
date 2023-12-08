#collects Project_02_CSV_Files from local arduino connected to 3 sensors and saves it to local file and to server
#Sensor3 Near the room heater
#Sensor2 Near the window
#Sensor1 Near the door
from Project_02_Library import *
import time



def do_measurement(s1t, s2t, s3t, s1h, s2h, s3h):
    d1, d2, d3 = read_ardruino()
    save_localy(data=d1, file_name="/Users/m19-056/PycharmProjects/pythonProject1/Project_Unit_2/Project_02_Weather_Station/Project_02_CSV_Files/Project_02_CSV_S1.csv")
    save_localy(data=d2, file_name="/Users/m19-056/PycharmProjects/pythonProject1/Project_Unit_2/Project_02_Weather_Station/Project_02_CSV_Files/Project_02_CSV_S2.csv")
    save_localy(data=d3, file_name="/Users/m19-056/PycharmProjects/pythonProject1/Project_Unit_2/Project_02_Weather_Station/Project_02_CSV_Files/Project_02_CSV_S3.csv")

    new_record(d1[1], sensor_id=s1t)
    new_record(d1[0], sensor_id=s1h)
    new_record(d2[1], sensor_id=s2t)
    new_record(d2[0], sensor_id=s2h)
    new_record(d3[1], sensor_id=s3t)
    new_record(d3[0], sensor_id=s3h)

def create_all_sensors():
    s1t = create_new_sensor("s1t", "Temperature", "room")
    s2t = create_new_sensor("s2t", "Temperature", "room")
    s3t = create_new_sensor("s3t", "Temperature", "room")
    s1h = create_new_sensor("s1h", "Humidity", "room")
    s2h = create_new_sensor("s2h", "Humidity", "room")
    s3h = create_new_sensor("s3h", "Humidity", "room")
    print(s1t, s2t, s3t, s1h, s2h, s3h)
    return s1t, s2t, s3t, s1h, s2h, s3h

def main():
    for _ in range(576):    
        do_measurement(40, 41, 42, 43, 44, 45)
        time.sleep(300)

do_measurement(40, 41, 42, 43, 44, 45)
