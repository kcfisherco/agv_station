# Station - Fisher Dynamics AGV Team 
## Table of Contents
### Project Overview
1. [Description](#Description)
2. [Requirements](#Requirements)
3. [Prerequisites](#Prerequisites)

Code Overview
1. [ROS2 Components](#ROS2-Components)
2. [Stack Light Color Conditions](#Stack-Light-Color-Conditions)
3. [Stack Light Conditional Flow Diagram](#Stack-Light-Conditional-Flow-Diagram)
4. [Station Pseudocode](#Station-Pseudocode)

Credit
1. [Contact & Author](#Contact-&-Author)

# Project Overview
## Description
At a agv station, the color of the station's stack light will change depending on certain conditions met and communicate with the robot when to grab the cart when placed onto the sensors. A Jetson Nano (I used Jetson Xavier for my first build) will be installed on each station as a computer and what it'll compute are as follows in this documentation...

## Requirements
Functional requirements
- Listen for state of sensors
- Configure GPIO pins to read relays and power on/off relays 
    - Change flag colors through relays
- Publish messages to robot when cart is in place
- Request data and update database

Non-functional requirements
- Ensure real time responsiveness
- Maintain efficient and clean code that follows a similar structure to overall project

## Prerequisites
Software Preqrequisites
- ROS2 Humble (Galactic if using Jetson Xavier)
- Jetson GPIO library (https://github.com/NVIDIA/jetson-gpio)

Hardware Prerequisites
- Jetson (Xavier or Nano) w/ 3-Ch relay expansion board mounted
- 2 Sensors

# Code Overview
## ROS2 Components
Nodes
- Station (Publisher)

Parameters
- Station number
- Production running?
- Did robot clear cart?

## Stack Light Color Conditions
### Condition 1:
Conditions that must be met:
- Production is not running

Output: \
Flag Color = <span style="color: Yellow;">Yellow</span>

<hr>

### Condition 2:
Conditions that must be met:
- Production is running
- No sensors are active

Output: \
Flag Color = <span style="color: Green;">Green</span>

<hr>

### Condition 3:
Conditions that must be met:
- Production is running
- Only one sensor is active
- Robot is clear

Output: \
Flag Color = <span style="color: Yellow;">Flashing Yellow</span>

<hr>

### Condition 4:
Conditions that must be met:
- Production is running
- One or no sensors are active
- Robot is not clear

Output: \
Flag Color = <span style="color: Red;">Flashing Red</span>

<hr>

### Condition 5:
Conditions that must be met:
- Production is running
- All sensors are active

Output: \
Flag Color = <span style="color: Blue;">Blue</span>

## Stack Light Conditional Flow diagram
<img src="flowdiagram.drawio.svg" alt="Flow diagram of the overall project" style="width:750px;"/>

## Station Pseudocode
```

class stack light publisher node
    init self
        create node name
        create publisher
        call publisher function

    function grab cart()
        if light color is xyz
            send message to grab cart
        otherwise 
            pass

function set light color()
    if production is running
        power light yellow
    otherwise
        if lights are both on
            power light blue
        else if only one light is on
            power light yellow
        otherwise
            power light green

function power light(color)
    some gpio algorithms to power light...


function main
    try
        initialize gpio, nodes
    except
        spin nodes
    finally
        destroy/shutdown up everything

call main
```

# Credit
## Contact & Author
Kidd Chang - kidd.chang@fisherco.com