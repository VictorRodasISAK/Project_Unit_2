# A Distributed Weather Station for ISAK
![Project_02_GIF.gif](Project_02_Images%2FProject_02_GIF.gif)


**Fig.1:** *Weather GIF* [^1]


[^1]: Giphy, McLovin. “Search All the Gifs &amp; Make Your Own Animated Gif.” GIPHY, 2013, giphy.com/trending-gifs. Accessed 30 Nov. 2023. 


# Criteria A: Planning


## Problem Definition


## Proposed Solution
Considering the client requirements an adequate solution includes a low cost sensing device for humidity and temperature 
and a custom data script that process and analysis the samples acquired. For a low cost sensing device an adequate 
alternative is the DHT11 sensor[^2] which is offered online for less than 5 USD and provides adequate precision and range
for the client requirements (Temperature Range: 0°C to 50°C, Humidity Range: 20% to 90%). Similar devices such as the 
DHT22, AHT20 or the AM2301B [^3] have higher specifications, however the DHT11 uses a simple serial communication (SPI) 
rather than more elaborated protocols such as the I2C used by the alternatives. For the range, precision and accuracy 
required in this application the DHT11 provides the best compromise. Connecting the DHT11 sensor to a computer requires 
a device that provides a Serial Port communication. A cheap and often used alternative for prototyping is the Arduino 
UNO microcontroller [^4]. "Arduino is an open-source electronics platform based on easy-to-use hardware and software"[^5]. 
In addition to the low cost of the Arduino (< 6USD), this device is programmable and expandable[^2]. Other alternatives 
include different versions of the original Arduino but their size and price make them a less adequate solution.

Considering the budgetary constraints of the client and the hardware requirements, the software tool that I proposed for 
this solution is Python. Python's open-source nature and platform independence contribute to the long-term viability of 
the system. The use of Python simplifies potential future enhancements or modifications, allowing for seamless scalability 
without the need for extensive redevelopment [^6][^7]. In comparison to the alternative C or C++, which share similar 
features, Python is a High level programming language (HL) with high abstraction [^8]. For example, memory management 
is automatic in Python whereas it is responsibility of the C/C++ developer to allocate and free up memory [^8], this 
could result in faster applications but also memory problems. In addition, a HLL language will allow me and future 
developers extend the solution or solve issues promptly.


[^2]: Industries, Adafruit. “DHT11 Basic Temperature-Humidity Sensor + Extras.” Adafruit Industries Blog RSS, https://www.adafruit.com/product/386. 


[^3]: Nelson, Carter. “Modern Replacements for DHT11 and dht22 Sensors.” Adafruit Learning System, https://learn.adafruit.com/modern-replacements-for-dht11-dht22-sensors/what-are-better-alternatives.  


[^4]:“How to Connect dht11 Sensor with Arduino Uno.” Arduino Project Hub, https://create.arduino.cc/projecthub/pibots555/how-to-connect-dht11-sensor-with-arduino-uno-f4d239.  


[^5]:Team, The Arduino. “What Is Arduino?: Arduino Documentation.” Arduino Documentation | Arduino Documentation, https://docs.arduino.cc/learn/starting-guide/whats-arduino.  


[^6]:Tino. “Tino/PyFirmata: Python Interface for the Firmata (Http://Firmata.org/) Protocol. It Is Compliant with Firmata 2.1. Any Help with Updating to 2.2 Is Welcome. the Capability Query Is Implemented, but the Pin State Query Feature Not Yet.” GitHub, https://github.com/tino/pyFirmata. 


[^7]:Python Geeks. “Advantages of Python: Disadvantages of Python.” Python Geeks, 26 June 2021, https://pythongeeks.org/advantages-disadvantages-of-python/.


[^8]: Real Python. “Python vs C++: Selecting the Right Tool for the Job.” Real Python, Real Python, 19 June 2021, https://realpython.com/python-vs-cpp/#memory-management.


### Design Statement


## Success Criteria
1. The solution provides a visual representation of the Humidity and Temperature values inside a dormitory (Local) and outside the house (Remote) for a period of minimum 48 hours. 
2. ```[HL]``` The local variables will be measure using a set of 3 sensors around the dormitory.
3. The solution provides a mathematical modelling for the Humidity and Temperature levels for each Local and Remote locations. ```(SL: linear model)```, ```(HL: non-lineal model)```
4. The solution provides a comparative analysis for the Humidity and Temperature levels for each Local and Remote locations including mean, standad deviation, minimum, maximum, and median.
5. ```(SL)```The Local samples are stored in a csv file and ```(HL)``` posted to the remote server as a backup.
6. The solution provides a prediction for the subsequent 12 hours for both temperature and humidity.
7. The solution includes a poster summarizing the visual representations, model and analysis created. The poster includes a recommendation about healthy levels for Temperature and Humidity.

_TOK Connection: To what extent does ```the use of data science``` in climate research influence our understanding of environmental issues, and what knowledge questions arise regarding the ```reliability, interpretation, and ethical implications``` of data-driven approaches in addressing climate change_

1. How does our use of technology shape our understanding of the environment
2. What responsibilities do we have as technologists when it comes to handling personal data related to our living spaces?
3. What cultural and contextual factors might impact our interpretation of the results, especially when comparing our local readings with those from the campus? 

# Criteria B: Design


## System Diagram
![Project_02_System_Diagram.png](Project_02_Images%2FProject_02_System_Diagram.png)


**Fig.2** shows the system diagram for the proposed solution (**HL**). The indoor variables will be measured using an 
Arduino and three DHT11 sensors located inside a room. Three sensors are used to determine more precisely the physical 
values and include measurement uncertainty. The outdoor variables will be requested to the remote server using a GET 
request to the API of the server at ```192.168.6.153/readings```. The local values are stored in a CSV database locally 
and a backup copy will be store in the remote server using the **Weather API**. 


## Record Of Tasks
| Task No. | Planned Action                           | Planned Outcome                                                                              | Time estimate | Target completion date | Criteria |
|----------|------------------------------------------|----------------------------------------------------------------------------------------------|---------------|------------------------|----------|
| 1        | Take information from Dr. Ruben's GitHub | To have the proposed solution, success criteria and the system diagram                       | 15 min        | Nov 25                 | A, B     |
| 2        | Working on the problem definition        | To have a general view on what do we need to work on                                         | 10 min        | Nov 26                 | A        |
| 3        | Making a shared repository on GitHub     | To have all the information updated                                                          | 10 min        | Nov 27                 | B        |
| 4        | Working on the code for 1 sensor         | To make sure that the sensors are working in a good way                                      | 30 min        | Nov 28                 | C        |
| 5        | Working on the functions for the code    | To have every function in one python code, therefore the main code is going to be more clear | 3 hours       | Nov 29                 | C        |
| 6        | Working on the code for 3 sensors        | To make sure that we can get the data in a clear way                                         | 1 hour        | Nov 30                 | C        |
| 7        | Making the connections between sensors   | To have the idea of the connections that we need to make and get the results expected        | 45 min        | Nov 30                 | C        |

## Test Plan
| Test No. | Type of Test                                               | Procedure                                                                                                    | Expected Outcome                                                                   | Date   |
|----------|------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|--------|
| 1        | Testing the Arduino code for 1 sensor                      | Upload the code to the Arduino, then use PyCharm code to print the data that we are getting from the sensor  | Data presented in the format Humidity:XX.XX% Temperature:XX.XX°C                   | Nov 28 |
| 2        | Testing the Arduino code for 2 sensors                     | Upload the code to the Arduino, then use PyCharm code to print the data from the 2 sensors                   | Data presented in the format Humidity:XX.XX% Temperature:XX.XX°C in both sensors   | Nov 29 |
| 3        | Testing the Arduino code for 3 sensors                     | Upload the code to the Arduino, then use PyCharm code to print the data from the 3 sensors                   | Data presented in the format Humidity:XX.XX% Temperature:XX.XX°C in the 3 sensors  | Nov 30 |
| 4        | Running the PyCharm code to save the data in the CSV Files | Run the code in PyCharm and after getting the data, saving the values of the sensors separately in CSV files | Every CSV file with humidity in the first line, and temperature in the second line | Dec 01 |

# Criteria C: Development


## Existing Tools


## List Of Techniques Used


## Development


# Criteria D: Functionality
