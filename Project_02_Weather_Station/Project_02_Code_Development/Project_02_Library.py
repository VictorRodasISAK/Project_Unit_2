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

def new_record(value, sensor_id, ip = "192.168.6.153"):
    headers = login_to_server()
    record = {"sensor_id": sensor_id, "value": value}
    ans = requests.post(f"http://{ip}/reading/new", json=record, headers=headers)
    print(ans.json())

def get_my_sensors(ip = "192.168.6.153"):
    headers = login_to_server()
    sen = requests.get(f"http://{ip}/user/readings", headers=headers)
    return sen.json()

def read_ardruino():
    ardruino = serial.Serial(port="COM5", baudrate=9600, timeout=0.1)
    d1 = ""
    while len(d1) < 1:
        d1 = ardruino.readline()
    d2 = ""
    while len(d2) < 1:
        d2 = ardruino.readline()
    d3 = ""
    while len(d3) < 1:
        d3 = ardruino.readline()
    d1 = d1.decode("utf-8")
    d2 = d2.decode("utf-8")
    d3 = d3.decode("utf-8")

    d1 = d1.strip("\r\n").split(",")
    d2 = d2.strip("\r\n").split(",")
    d3 = d3.strip("\r\n").split(",")
    return d1, d2, d3

def save_localy(data, file_name = "Project_02_CSV_Files.csv"):
    with open(file_name, "r") as f:
        humidity = f.readline().strip("\n")
        temperature = f.readline().strip("\n")
    h, t = data
    humidity = humidity + "," + h
    temperature = temperature + "," + t
    with open(file_name, "w") as f:
        f.writelines(humidity)
        f.writelines("\n")
        f.writelines(temperature)

def get_server_sensor(id, ip = "192.168.6.153"):
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
    
def formate_data(data):
    return data.strip("\n").split(",")
    


# d1, d2, d3 = read_ardruino()
# print(d1)
# print(d2)
# print(d3)
# save_localy(Project_02_CSV_Files=d1, file_name="Project_02_CSV_Files/Project_02_CSV_S1.csv")
# save_localy(Project_02_CSV_Files=d2, file_name="Project_02_CSV_Files/Project_02_CSV_S2.csv")
# save_localy(Project_02_CSV_Files=d3, file_name="Project_02_CSV_Files/Project_02_CSV_S3.csv")ú

#new_record(d1[1], sensor_id=24)


new_record(28, sensor_id=24)
print(get_my_sensors())