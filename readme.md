# Station Project
## Description
Using a jetson nano (Used xavier for testing purposes), we will change colors of the station flag based on the states of two sensors

## Contact
Kidd Chang - kidd.chang@fisherco.com

## Software Preqrequisites
- Jetson GPIO library
- ROS2

## Hardware Prerequisites
- Jetson (Xavier or Nano)
- 3-Ch relay expansion board
- Relays
- 2 Sensors

# Project Overview

## Functional requirements
- Read states of two sensors
- Configure GPIO pins to read relays and power on/off relays 
- Change flag colors based on sensors
- Change flag color to orange when production is stopped

## Non-functional requirements
- Ensure real time responsiveness
- Maintain efficient and clean code that follows a similar structure to overall project

## Nodes
- Sensor
- Relay

## Publishers
- Sensor

## Subscribers
- Relay

## Psudocode
```
class sensor node
    init
        publish

    detect if sensor relay on or off function()
        listen if sensor on
            algorithm to recieve gpio pin powered high 
        otherwise
            algorithm to recieve gpio pin powered low

class relay node
    init
        subscribe

    activate flag relay function(parameter: pin)
        algorithm to turn gpio pin high

```

## Conditional Flow diagram
![Flow diagram of the overall project](flowdiagram.drawio.svg)
