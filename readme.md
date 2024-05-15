# Station - Fisher Dynamics AGV Team 
## Table of Contents
1. [Description](#Description)
2. []()
3. []()

# Project Overview
## Description
On the production floor at a robot station, we want to control the color of the station's stack light depending on certain conditions met and communicate with the robot, when to grab the cart. The condition of the light will depend on two sensors mounted onto the station. A Jetson Nano (I used Jetson Xavier for testing purposes) will be installed on each station as a computer, which will be grabbing from and sending data to the database, listening for the sensors, changing stack light colors, and sending messages to the robot.

## Functional requirements
- Get state of sensors
- Configure GPIO pins to read relays and power on/off relays 
    - Change flag colors based on conditions met
- Publish messages to robot when cart is in place
- Request and update database for the station it is at

## Non-functional requirements
- Ensure real time responsiveness
- Maintain efficient and clean code that follows a similar structure to overall project

## Software Preqrequisites
- Jetson GPIO library
- ROS2 Humble (Galactic if using Jetson Xavier)

## Hardware Prerequisites
- Jetson (Xavier or Nano) w/ 3-Ch relay expansion board mounted
- 2 Sensors

# Code Overview

### Nodes
- Sensor
- Relay

### Publishers
- Sensor

### Subscribers
- Relay

### Interfaces
Msg:
- Sensor

Srv:
- None

### Parameters
- none


## Stack Light Color Conditions
### Condition 1:
Conditions that must be met:
- Production is not running

Output: \
Flag Color = <span style="color: yellow;">Yellow</span>

<hr>

### Condition 2:
Conditions that must be met:
- Production is running
- No sensors are active

Output: \
Flag Color = <span style="color: green;">Green</span>

<hr>

### Condition 3:
Conditions that must be met:
- Production is running
- All sensors are active

Output: \
Flag Color = <span style="color: Blue;">Blue</span>

<hr>

### Condition 4:
Conditions that must be met:
- Production is not running
- RobotMoveCart is not active
- Cart is in place

Output: \
Flag Color = <span style="color: Red;">Flashing Red</span>

<hr>

## Stack Light Conditional Flow diagram
<img src="flowdiagram.drawio.svg" alt="Flow diagram of the overall project" style="width:750px;"/>

## Station Psudocode
```
class sensor node
    init
        create & send sensor publisher

    function send data ()
        receive sensor data from database
        publish sensor data

class relay node
    init
        subscribe

    function detect if sensor relay on or off()
        listen if sensor on
            algorithm to recieve gpio pin powered high 
        otherwise
            algorithm to recieve gpio pin powered low

    function green light(parameter: pin1, pin2)
        

function main
    try
        initialize gpio, nodes
    except
        spin nodes
    finally
        destroy/shutdown up everything

call main
```

## Contact & Author
Kidd Chang - kidd.chang@fisherco.com