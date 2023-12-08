import matplotlib.pyplot as plt
import numpy as np
from Project_02_Library import *
import datetime
from scipy.optimize import curve_fit

# Initialize the sensors
sensors_id = {"s1t": 40, "s2t": 41, "s3t": 42, "s1h": 43, "s2h": 44, "s3h": 45}

# Get the data from the server
sensors_data = {}
for s in sensors_id:
    sensors_data[s] = [float(x) for x in get_my_sensor(sensors_id[s])]

# get the time
time_in_min = [x*5 for x in range(len(sensors_data["s1t"]))]
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
    plt.ylabel("Temperature (C)")   
    plt.xlabel("Time")
    plt.title("Temperature and Humidity in the room")
    plt.subplot(2, 1, 2)
    plt.errorbar(time, mean_hum, yerr=std_hum, fmt='o', ecolor='green', capsize=3)
    plt.plot(time, mean_hum, label="avg")
    plt.ylabel("Humidity (%)")
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

    plt.xlim(time[0], time[-1])
    plt.gcf().autofmt_xdate()
    plt.show()

# New function to plot average temperature with error bars every 30 data points and minimum and maximum
def plot_avg_temp_with_error():
    plt.errorbar(time[::30], mean_temp[::30], yerr=std_temp[::30], fmt='o', ecolor='green', capsize=3)
    plt.fill_between(time, min_temp, max_temp, alpha=0.2, label="min/max")
    plt.plot(time, mean_temp, label="avg")
    plt.ylabel("Temperature (C)")
    plt.xlabel("Time")
    plt.title("Average Temperature with Error Bars")

    plt.xlim(time[0], time[-1])
    plt.gcf().autofmt_xdate()
    plt.show()

plot_avg_temp_with_error()

def qudratic_model(x, a, b, c):
    return a*x**2 + b*x + c

def sin_model(x, a, b, c, d):
    return a*np.sin(b*x + c) + d

def linear_model(x, a, b):
    return a*x + b

def polynomial_model(x, a, b, c, d, e):
    return a*x**4 + b*x**3 + c*x**2 + d*x + e

def logist_model(x, a, b, c, d):
    return a/(1 + np.exp(-c*(x - d))) + b

def plot_regression_model(model):
    # Fit the regression model
    popt, pcov = curve_fit(model, time_in_min, mean_temp)

    # Generate x values for the regression line
    x = np.linspace(time_in_min[0], time_in_min[-1], 1000)

    # Generate y values using the fitted parameters
    y = model(x, *popt)

    # Plot the average temperature data
    plt.plot(time_in_min, mean_temp, label="Average Temperature")

    # Plot the regression model
    plt.plot(x, y, label="Regression Model")

    plt.ylabel("Temperature (C)")
    plt.xlabel("Time)")
    plt.title("Regression Model for Average Temperature")
    plt.legend()

    plt.xlim(time_in_min[0], time_in_min[-1])

    plt.xticks(ticks=[time_in_min[x] for x in range(60, len(time_in_min), 60)], labels=[origin + datetime.timedelta(minutes=time_in_min[x]) for x in range(60, len(time_in_min), 60)])  # Display x-axis ticks in datetime format
    plt.gcf().autofmt_xdate()
    plt.show()

plot_regression_model(polynomial_model)


def visulise_tempreture():
    plt.style.use('ggplot')

    fig = plt.figure(figsize=(10, 5))
    grid = plt.GridSpec(3, 4, figure=fig)
    ax1 = fig.add_subplot(grid[0:3, 0:3])
    ax1.set_xlim(time[0], time[-1])
    plt.gcf().autofmt_xdate()
    plt.ylabel("Temperature (C)")
    plt.xlabel("Time")
    ax1.plot(time, mean_temp, label="avg", color='blue')
    ax2 = fig.add_subplot(grid[0, 3])
    ax2.set_xlim(time[0], time[-1])
    ax2.xaxis.set_major_locator(plt.MaxNLocator(4))
    plt.gcf().autofmt_xdate()
    ax2.plot(time, sensors_data["s1t"], label="s1t", color='red')
    ax3 = fig.add_subplot(grid[1, 3])
    ax3.set_xlim(time[0], time[-1])
    ax3.xaxis.set_major_locator(plt.MaxNLocator(4))
    plt.gcf().autofmt_xdate()
    ax3.plot(time, sensors_data["s2t"], label="s2t", color='green')
    ax4 = fig.add_subplot(grid[2, 3])
    ax4.set_xlim(time[0], time[-1])
    ax4.xaxis.set_major_locator(plt.MaxNLocator(4))
    plt.gcf().autofmt_xdate()
    ax4.plot(time, sensors_data["s3t"], label="s3t", color='orange')
    plt.show()

visulise_tempreture()


