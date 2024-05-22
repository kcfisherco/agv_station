#!/usr/bin/env python3
import time, os, pyodbc, rclpy, logging, sys
from typing import Counter
import Jetson.GPIO as GPIO

from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from threading import Thread

from amr_v4_msgs_srvs.msg import Station

class StationPublisher(Node):
    def __init__(self):
        super().__init__("station")
        self.publisher = self.create_publisher(Station, f"/station_{station_name}/cart_ready", 10)
        self.timer = self.create_timer(1.0, self.callback)
        self.cart_status = False

    def callback(self):
        message = Station()
        if (self.cart_status == True):
            message.cart_in_place = True
        else:
            message.cart_in_place = False
        self.publisher.publish(message)

def update_database(station_number, station):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=fisher-agc.database.windows.net;DATABASE=Fisher_AGC;UID=fisher_agc;PWD=tTp##L86?qM!4iG7')
    cursor = cnxn.cursor()
    try:
        update_station = cursor.execute("""
                                        update Station
                                        set cart_in_place = ?
                                        where station_name = ?
                                        """, station.cart_status, station_number)
        cnxn.commit()
        cnxn.close()
        return
    except Exception as e:
        print("Error: ", e)
        cnxn.rollback()
        cnxn.close()
        return

def read_database(station_number):
    global production
    global docking
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=fisher-agc.database.windows.net;DATABASE=Fisher_AGC;UID=fisher_agc;PWD=tTp##L86?qM!4iG7')
    cursor = cnxn.cursor()

    production = cursor.execute("select production_enabled from Station where station_name=?", station_number).fetchval() 
    docking = cursor.execute("select docking_in_action from Station where station_name=?", station_number).fetchval()
    cnxn.close()
    return production, docking

def light_controller(station):
        if (not production):
            GPIO.output(pin_output[0], GPIO.HIGH)
            GPIO.output(pin_output[1], GPIO.HIGH)
            GPIO.output(pin_output[2], GPIO.LOW)
            print("Set light color yellow")
            station.cart_status = False
        elif (GPIO.input(pin_input[0]) and GPIO.input(pin_input[1])):
            GPIO.output(pin_output[0], GPIO.LOW)
            GPIO.output(pin_output[1], GPIO.LOW)
            GPIO.output(pin_output[2], GPIO.HIGH)
            print("Set light color Blue")
            station.cart_status = True
        elif (GPIO.input(pin_input[0]) ^ GPIO.input(pin_input[1])):
            prev_inputs = pin_input
            for _ in range(4):
                GPIO.output(pin_output[0], GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(pin_output[0], GPIO.LOW)
                time.sleep(0.5)
                if GPIO.input(pin_input[0]) != prev_inputs[0] or GPIO.input(pin_input[1]) != prev_inputs[1]:
                    break
            print("Set light color flashing red")
            station.cart_status = False
        else:
            GPIO.output(pin_output[0], GPIO.LOW)
            GPIO.output(pin_output[1], GPIO.HIGH)
            GPIO.output(pin_output[2], GPIO.LOW)
            print("Set light color Green")
            station.cart_status = False

# Temporary Function
# NOTE: At this point in time I'm unable to test with sensors
def simulate_sensors(input_pins, pin_one_power, pin_two_power):
        GPIO.setup(input_pins, GPIO.OUT, initial=GPIO.LOW)
        GPIO.output(input_pins[0], pin_one_power)
        GPIO.output(input_pins[1], pin_two_power)
        GPIO.setup(input_pins, GPIO.IN)

"""Global Settings"""
station_name = (os.getenv('STATION_ID','station-x')).split('-')[1]
print("Starting Program for station: %s" % station_name)
pin_input = [11, 13]      # 11 = Sensor 1, 13 = Sensor 2
pin_output = [40, 38, 37] # 40 = CH1/Red, 38 = CH2/Green, 37 = CH3/Blue

def main():
    rclpy.init(args=None)

    try:

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin_input, GPIO.IN)
        GPIO.setup(pin_output, GPIO.OUT, initial=GPIO.LOW)
        station = StationPublisher()
        executor = MultiThreadedExecutor()
        executor.add_node(station)
        executor_try = Thread(target=executor.spin, daemon=True)
        executor_try.start()
        while rclpy.ok():
            if (station_name != None):
                production, docking = read_database(station_name)
                simulate_sensors(pin_input, GPIO.LOW, GPIO.HIGH) # Change test parameters here
                light_controller(station)
                update_database(station_name, station)
            else:
                logging.info("The Hostname of Station is not set, aborting program and set STATION_ID = station-x in 'sudo gedit ~/.bashrc' GOODBYE !")
                time.sleep(5)
                sys.exit()

    except (KeyboardInterrupt,SystemError,SystemExit,rclpy.exceptions.ROSInterruptException):
        station.destroy_node()
        executor.shutdown()
        exit()
    finally:
        GPIO.cleanup()
        rclpy.shutdown()

if __name__ == '__main__':
    main()