import requests
import serial

def smoothing(x, smoothing_win = 5, overlap = 1):
    smooth_x = []
    t = []
    for i in range(0, len(x), int(smoothing_win*overlap)):
        smooth_x.append(sum(x[i:i+smoothing_win])/smoothing_win)
        t.append(i)
    return t, smooth_x

def login_to_server(ip = "192.168.6.153", user = {"username": "Jenda", "password": "stoikForPres"}):
    ans = requests.post(f"http://{ip}/login", json=user)
    #print(ans.json())
    cookie = ans.json()["access_token"]
    return {"Authorization": f"Bearer {cookie}"} 

def new_record(value, sensor_id = 12, ip = "192.168.6.153"):
    headers = login_to_server()
    record = {"sensor_id": 12, "value": 28}
    ans = requests.post(f"http://{ip}/reading/new", json=record, headers=headers)

def get_my_sensor(sensor_id = 12, ip = "192.168.6.153"):
    headers = login_to_server()
    sen = requests.get(f"http://{ip}/sensors", headers=headers)
    return sen.json()

def read_ardruino():
    ardruino = serial.Serial(port="COM6", baudrate=9600, timeout=0.1)
    data = ""
    while len(data) < 1:
        data = ardruino.readline()
    return data.decode("utf-8")

def save_localy(data, file_name = "data.csv"):
    with open(file_name, "r") as f:
        file = f.readlines()
    file.append(data)
    with open(file_name, "w") as f:
        f.writelines(file)

def get_school_sensor(id, ip = "192.168.6.153"):
    ans = requests.get(f"http://{ip}/readings")
    data = ans.json()

    sensors = data["readings"][0]
    sensor = []
    for s in sensors:
        if s["sensor_id"] == id:
            sensor.append(s["value"])
    return sensor
    
def create_new_sensor(name, type, location, ip = "192.168.6.153"):
    headers = login_to_server()
    sensor = {"name": name, "type": type, "location": location, "unit": "C"}
    ans = requests.post(f"http://{ip}/sensor/new", json=sensor, headers=headers)
    print(ans.json())
    json = ans.json()
    return json["id"]
    
