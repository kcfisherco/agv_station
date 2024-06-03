# Station - Fisher Dynamics AGV Team 
## Table of Contents
### [Project Overview](#Project-Overview)
1. [Description](#Description)
2. [Features](#Features)

### [Getting Started](#Getting-Started)
1. [Prerequisites](#Prerequisites)
2. [Installation](#Installation)
3. [Configuration](#Configuration)

### [Architecture](#Architecture)
1. [ROS2 Components](#ROS2-Components)

### [Testing](#Testing)
2. [Stack Light Color Conditions](#Stack-Light-Color-Conditions)
3. [Stack Light Conditional Flow Diagram](#Stack-Light-Conditional-Flow-Diagram)

### [Deployment](#Deployment)

### [Troubleshoooting](#Troubleshoooting)

### [Contributing](#Contributing)

### [Why behind my coding choices](#Why-behind-my-coding-choices])

### [Licensing & Credit](#Licensing-&-Credit])
1. [Contact & Author](#Contact-&-Author)

# Project Overview
## Description
At a agv station, the color of the station's stack light will change depending on certain conditions met and communicate with the robot  to grab the cart when placed onto the sensors. A Jetson Nano (I used Jetson Xavier throughout my initial tests) will be installed on each station as a computer and what it'll compute are as follows in this documentation...

## Features
Functional requirements
- Listen for state of sensors
- Configure GPIO pins to power on/off relays 
    - Change stack light colors (depending on conditions met) through relays
- Publish 'is_cart_in_place' messages to robot
- Read data and update database

Non-functional requirements
- Ensure real time responsiveness
- Maintain efficient and clean code that follows a similar structure to overall project

# Getting Started
## Prerequisites
Software 
- Python 3.8+
- ROS2 Humble (or Galactic)
- Microsoft SQL Server (v.19.3)
- Ubuntu 22.04.4 (20.04.6 if using ROS2 Galactic)

Hardware 
- Jetson Nano [40-Pin Datasheet](https://jetsonhacks.com/nvidia-jetson-nano-j41-header-pinout/)
- 3-Ch relay expansion board [Documentation](https://www.waveshare.com/wiki/3-CH_Relay_for_Jetson_Nano)
- 2 Proximity Sensors

Libraries
- Nvidia GPIO

## Installation

1. Follow this documentation to download ROS2 humble [(Link)](https://docs.ros.org/en/humble/Installation.html)
2. Follow this documentation to download Nvidia GPIO library [(Link)](https://github.com/NVIDIA/jetson-gpio)
3. Download Microsoft SQL Server Management Studio (v.19.3) to access database  [(Link)](https://learn.microsoft.com/en-us/sql/ssms/release-notes-ssms?view=sql-server-ver16#193)

## Configuration

1. Set up ROS2 environment through terminal
```
source /opt/ros/<ROS-dist>/setup.bash
source ~/agv_station/install/setup.bash
```
2. Set up local environment station variable 

Open .bashrc with gedit text editor
```
gedit
```  

Add this line inside of the .bashrc, but replace < number > with the actual station number
```
export STATION_ID="station-<number>"
```

check if station environment variable exists
```
printenv | grep STATION
``` 

3. Build the ROS2 Files
```
USER:~/agv_station$ colcon build
```

4. Connect to database on linux side
```
sudo su

curl https://packages.microsoft.com/keys/microsoft.asc | sudo tee /etc/apt/trusted.gpg.d/microsoft.asc

curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list 

sudo apt-get update

sudo ACCEPT_EULA=Y apt-get install -y msodbcsql18

sudo ACCEPT_EULA=Y apt-get install -y mssql-tools18

echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrcsource ~/.bashrc
```

# Architecture
## Data Flow
Initialize global variables, gpio, nodes, and local environment station name ---> Start spinning main program ---> Get database ---> Listen for sensor states ---> Change light color accordingly ---> Send data to database if cart is in place ---> Repeat from {Start Spinning main program}

## ROS2 Components
Nodes
- Station (Publisher)

## Variable Conditions
### Stack Light:
#### input:
- is sensor on/off
#### Output:
- stack light color

<hr>

### Database:
#### Send data
- station name
- is cart in place
#### Receive data
- station name
- is production running
- is robot in motion?

<hr>

### Timer
- 2 seconds - Flashing lights

# Testing 
## Conditions:
**Note:** All bulleted conditions must be met in order to get outputs

### Condition 1:
#### Conditions:
- Production is not running

#### Output: 
- Stack Light Color = <span style="color: Yellow;">Yellow</span>
- Cart in place = <span style="color: Red;">False</span>

<hr>

### Condition 2:
#### Conditions:
- Production is running
- Sensors are not active

#### Output:
- Stack Light Color = <span style="color: Green;">Green</span>
- Cart in place = <span style="color: Red;">False</span>

<hr>

### Condition 3:
#### Conditions:
- Production is running
- Sensors are active

#### Output:
- Stack Light Color = <span style="color: Blue;">Blue</span>
- Cart in place = <span style="color: Green;">True</span>

<hr>

### Condition 4:
#### Conditions:
- Production is running
- Sensors are not active
- Robot is in motion

#### Output:
- Stack Light Color = <span style="color: Red;">Flashing Red</span> 
- Cart in place = <span style="color: Red;">False</span>

#### Test Case:
- What if robot moves cart while robot is in motion? 
- What if operator moves cart while robot is in motion? (most likely to happen)
    - **Known issue; We will keep watch**

<hr>

### Condition 5:
#### Conditions:
- Production is running
- Only one sensor works
- Robot is not in motion

#### Output:
- Stack Light color = <span style="color: Red;">Flashing Red</span>

Test Case:
- One sensor broke
- The operator didn't push the cart all the way back

## Stack Light Conditional Flow diagram
<img src="flowdiagram.svg" alt="Flow diagram of the overall project" style="width:600px;"/>

# Deployment

Run this line in the terminal to run the main station.py code (Make sure you sourced environment and did colcon build in [#Installion](#Installation))
```
ros2 run amr_v4_station station
```

# Troubleshooting
## Common Issues:
- What if operator moves cart while robot is in motion?

# Contributing
## Guidelines
- Submit a pull request if you'd like to make changes and we will review the changes
- Submit a ticket in the issues if there are any known issues or have feature requests [(Link)](https://github.com/kcfisherco/agv_station/issues) Provide detailed explaination about the issue or suggestion to help us understand and address it promptly

# Why behind my coding choices
## Flashing yellow 
I made stack light flashing yellow when only one sensor is active

### Problem statement:
This was because, what if one sensor was broken, but the other was working

### Solution
I made the stack light flashing yellow when it detects at least one of the sensors are active

# Licensing & Credit
## Licensing
Proprietary software of Fisher Dynamics
## Acknowledgements: Credit to contributors
- Kidd Chang - kidd.chang@fisherco.com
- Anirudh Nath - anirudh.nath@fisherco.com