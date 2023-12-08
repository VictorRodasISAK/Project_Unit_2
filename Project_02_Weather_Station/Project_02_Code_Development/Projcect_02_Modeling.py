import matplotlib.pyplot as plt
import numpy as np
from Project_02_Library import *
import datetime

# Initialize the sensors
sensors_id = {"s1t": 40, "s2t": 41, "s3t": 42, "s1h": 43, "s2h": 44, "s3h": 45}

# Get the data from the server
sensors_data = {}
for s in sensors_id:
    sensors_data[s] = [float(x) for x in get_my_sensor(sensors_id[s])]
    sensors_data[s] = sensors_data[s][:576]

# get the time
time_in_min = [x*5 for x in range(len(sensors_data["s1t"]))]

# use datetime to get the time in hours from initial time
origin = datetime.datetime(2023, 12, 2, 14, 0)
time = []
for t in time_in_min:
    time.append(origin + datetime.timedelta(minutes=t))
    

# get mean values for temperature and humidity
mean_temp = []
for s in range(len(sensors_data["s1t"])):
    mean_temp.append(np.mean([sensors_data["s1t"][s], sensors_data["s2t"][s], sensors_data["s3t"][s]]))
mean_hum = []
for s in range(len(sensors_data["s1h"])):
    mean_hum.append(np.mean([sensors_data["s1h"][s], sensors_data["s2h"][s], sensors_data["s3h"][s]]))

# standad deviation, minimum, maximum, and median
std_temp = []
for s in range(len(sensors_data["s1t"])):
    std_temp.append(np.std([sensors_data["s1t"][s], sensors_data["s2t"][s], sensors_data["s3t"][s]]))
std_hum = []
for s in range(len(sensors_data["s1h"])):
    std_hum.append(np.std([sensors_data["s1h"][s], sensors_data["s2h"][s], sensors_data["s3h"][s]]))
min_temp = []
for s in range(len(sensors_data["s1t"])):
    min_temp.append(np.min([sensors_data["s1t"][s], sensors_data["s2t"][s], sensors_data["s3t"][s]]))
min_hum = []
for s in range(len(sensors_data["s1h"])):
    min_hum.append(np.min([sensors_data["s1h"][s], sensors_data["s2h"][s], sensors_data["s3h"][s]]))
max_temp = []
for s in range(len(sensors_data["s1t"])):
    max_temp.append(np.max([sensors_data["s1t"][s], sensors_data["s2t"][s], sensors_data["s3t"][s]]))
max_hum = []
for s in range(len(sensors_data["s1h"])):
    max_hum.append(np.max([sensors_data["s1h"][s], sensors_data["s2h"][s], sensors_data["s3h"][s]]))

# plot the data
def plot_avg_temp_hum():
    plt.subplot(2, 1, 1)
    # plt.errorbar(time, mean_temp, yerr=std_temp, fmt='o', ecolor='green', capsize=3)
    plt.plot(time, mean_temp, label="avg")
    plt.fill_between(time, min_temp, max_temp, alpha= 0.2, label="min/max")
    plt.ylabel("Temperature")   
    plt.xlabel("Time")
    plt.title("Temperature and Humidity in the room")
    plt.subplot(2, 1, 2)
    plt.errorbar(time, mean_hum, yerr=std_hum, fmt='o', ecolor='green', capsize=3)
    plt.plot(time, mean_hum, label="avg")
    plt.ylabel("Humidity")
    plt.xlabel("Time")

    plt.xlim(time[0], time[-1])
    plt.gcf().autofmt_xdate()
    plt.show()
plot_avg_temp_hum()

# plot humidity sensor data
def get_indoor_humidity_data():
    plt.subplot(3, 1, 1)
    t, s1smooth = smoothing(sensors_data["s1h"], 10)
    plt.plot(t, s1smooth, label="s1h")
    plt.subplot(3, 1, 2)
    t, s2smooth = smoothing(sensors_data["s2h"], 10)
    plt.plot(t, s2smooth, label="s2h")
    plt.subplot(3, 1, 3)
    t, s3smooth = smoothing(sensors_data["s3h"], 10)
    plt.plot(t, s3smooth, label="s3h")
    plt.ylabel("Humidity")
    plt.xlabel("Time")
    plt.show()



