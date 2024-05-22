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
- Publish messages to robot so that it knows when to pickup cart or not to
- Read data and update database

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

## Variable Conditions
### Station Code:
#### input:
- is sensor on/off
#### Output:
- Set flag color

<hr>

### Database:
#### Send data
- is cart in place
#### Receive data
- station name
- is production running
- is robot in motion?

<hr>

### Timer
- 5 seconds

## Code Conditions:
**Note:** All bulleted conditions must be met in order to get outputs

### Condition 1:
#### Conditions:
- Production is not running

#### Output: 
- Flag Color = <span style="color: Yellow;">Yellow</span>
- Cart in place = <span style="color: Red;">False</span>

<hr>

### Condition 2:
#### Conditions:
- Production is running
- Sensors are not active/Cart not in place

#### Output:
- Flag Color = <span style="color: Green;">Green</span>
- Cart in place = <span style="color: Red;">False</span>

<hr>

### Condition 3:
#### Conditions:
- Production is running
- Sensors are active/Cart in place

#### Output:
- Flag Color = <span style="color: Blue;">Blue</span>
- Cart in place = <span style="color: Green;">True</span> after 5 seconds

<hr>

### Condition 4:
#### Conditions:
- Production is running
- Robot is in motion
- Sensors are not active/Cart not in place

#### Output:
- Flag Color = <span style="color: Red;">Flashing Red</span> 
- Cart in place = <span style="color: Red;">False</span>

#### Test Case:
- What if robot moves cart while robot is in motion?
- What if operator moves cart while robot is in motion?
    - **Known issue; We will keep watch**

<hr>

### Condition 5:
#### Conditions:
- Production is running
- Only one sensor works

#### Output:
- Flag color = Red

Test Case:
- What if one sensor is broken

## Stack Light Conditional Flow diagram
<img src="flowdiagram.svg" alt="Flow diagram of the overall project" style="width:750px;"/>

## Station Pseudocode
```

class station publisher node
    init self
        create node name
        create publisher
        call publisher function

    function callback
        cart ready = false
        if light controller function returns blue
            publish cart ready true
        otherwise
            publish cart ready false

    function light controller()
        if production is running
            make color red
            return red
        if sensor 1 & 2 is active
            make color blue
            return blue
        if sensor 1 or 2 is active
            make color flashing yellow
            return yellow
        otherwise
            make color green
            return green

    function get pin status of sensors
        algorithm to get pins

function get database
    connect to database

function update databse

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
## Creator & Author
Kidd Chang - kidd.chang@fisherco.com