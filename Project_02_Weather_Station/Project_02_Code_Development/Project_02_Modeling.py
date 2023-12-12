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

print("got my data")

# get the time
time_in_min = [x*5 for x in range(len(sensors_data["s1t"]))]
origin = datetime.datetime(2023, 12, 2, 14, 0)
time = []
for t in time_in_min:
    time.append(origin + datetime.timedelta(minutes=t))

print("got time")

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
    # plt.fill_between(time, min_temp, max_temp, alpha= 0.2, label="min/max")
    plt.ylabel("Temperature (C)")   
    plt.xlabel("Time")
    plt.title("Temperature and Humidity in the room")
    plt.subplot(2, 1, 2)
    # plt.errorbar(time, mean_hum, yerr=std_hum, fmt='o', ecolor='green', capsize=3)
    plt.plot(time, mean_hum, label="avg")
    plt.ylabel("Humidity (%)")
    plt.xlabel("Time")

    plt.xlim(time[0], time[-1])
    plt.gcf().autofmt_xdate()
    plt.show()
# plot_avg_temp_hum()

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

# plot_avg_temp_with_error()

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

# visulise_tempreture()

def get_data_from_date(yr, month, day, records):
    """
    because in 2.12. the weather was 7 degrees in a day and 1 degree in a night
    we use data from 20.11 where the weather was 8 degree in a day and 2 degree in a night
    wich is by far the most similar to the 2.12. data from our options from 17.11. to 21.11. and 7.12. onwards
    """
    date = datetime.datetime(yr, month, day).date()
    data = []
    for r in records:
        d = r["datetime"]
        datetime_object = datetime.datetime.strptime(d, '%Y-%m-%dT%H:%M:%S.%f')
        if datetime_object.date() == date:

            data.append(r)
    return data

def plot_outdoor_temp(yr, month, day1, day2):
    """
    takes temp from two days form server ids 0, 2, 4
    plots their average and datetime on x axis
    """
    sen1 = get_server_sensor(0)
    sen2 = get_server_sensor(2)
    sen3 = get_server_sensor(4)
    print("got sensors")

    data1 = get_data_from_date(yr, month, day1, sen1)
    data1 += get_data_from_date(yr, month, day2, sen1)
    print("got data 1")
    data2 = get_data_from_date(yr, month, day1, sen2)
    data2 += get_data_from_date(yr, month, day2, sen2)
    print("got data 2")
    data3 = get_data_from_date(yr, month, day1, sen3)
    data3 += get_data_from_date(yr, month, day2, sen3)
    print("got data 3")

    temp = []
    time = []
    y1 = []
    y2 = []
    y3 = []

    for a, b, c in zip(data1, data2, data3):
        y1.append(a["value"])
        y2.append(b["value"])
        y3.append(c["value"])
        temp.append(np.mean([y1, y2, y3]))
        time.append(datetime.datetime.strptime(a["datetime"], '%Y-%m-%dT%H:%M:%S.%f'))

    print(time[0], time[-1])

    # Plot the data using visulise_tempreture() function
    plt.style.use('ggplot')

    fig = plt.figure(figsize=(10, 5))
    grid = plt.GridSpec(3, 4, figure=fig)
    ax1 = fig.add_subplot(grid[0:3, 0:3])
    ax1.set_xlim(time[0], time[-1])
    plt.gcf().autofmt_xdate()
    plt.ylabel("Temperature (C)")
    plt.xlabel("Time")
    ax1.plot(time, temp, label="avg", color='blue')
    ax2 = fig.add_subplot(grid[0, 3])
    ax2.set_xlim(time[0], time[-1])
    ax2.xaxis.set_major_locator(plt.MaxNLocator(4))
    plt.gcf().autofmt_xdate()
    ax2.plot(time, y1, label="s1t", color='red')
    ax3 = fig.add_subplot(grid[1, 3])
    ax3.set_xlim(time[0], time[-1])
    ax3.xaxis.set_major_locator(plt.MaxNLocator(4))
    plt.gcf().autofmt_xdate()
    ax3.plot(time, y2, label="s2t", color='green')
    ax4 = fig.add_subplot(grid[2, 3])
    ax4.set_xlim(time[0], time[-1])
    ax4.xaxis.set_major_locator(plt.MaxNLocator(4))
    plt.gcf().autofmt_xdate()
    ax4.plot(time, y3, label="s3t", color='orange')
    plt.show()
           
# plot_outdoor_temp(2023, 11, 19, 20)
