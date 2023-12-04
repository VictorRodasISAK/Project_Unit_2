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

# get the time
time_in_min = [x*5 for x in range(len(sensors_data["s1t"]))]
time = [x/60 for x in time_in_min]
# use datetime to get the time in hours from initial time

    

# get mean values for temperature and humidity
mean_temp = []
for s in range(len(sensors_data["s1t"])):
    mean_temp.append(np.mean([sensors_data["s1t"][s], sensors_data["s2t"][s], sensors_data["s3t"][s]]))
mean_hum = []
for s in range(len(sensors_data["s1h"])):
    mean_hum.append(np.mean([sensors_data["s1h"][s], sensors_data["s2h"][s], sensors_data["s3h"][s]]))

# standad deviation, minimum, maximum, and median
# std_temp = np.std(mean_temp)
# min_temp = np.min(mean_temp)
# max_temp = np.max(mean_temp)
# median_temp = np.median(mean_temp)
# std_hum = np.std(mean_hum)
# min_hum = np.min(mean_hum)
# max_hum = np.max(mean_hum)
# median_hum = np.median(mean_hum)

# plot the data
plt.subplot(2, 1, 1)
plt.plot(time, mean_temp)
plt.ylabel("Temperature")   
plt.xlabel("Time")
plt.title("Temperature and Humidity in the room")
plt.subplot(2, 1, 2)
plt.plot(time, mean_hum)
plt.ylabel("Humidity")
plt.xlabel("Time")
plt.show()

# plot humidity sensor data
plt.subplot(3, 1, 1)
plt.plot(time, sensors_data["s1h"], label="s1h")
plt.subplot(3, 1, 2)
plt.plot(time, sensors_data["s2h"], label="s2h")
plt.subplot(3, 1, 3)
plt.plot(time, sensors_data["s3h"], label="s3h")
plt.ylabel("Humidity")
plt.xlabel("Time")
plt.show()

