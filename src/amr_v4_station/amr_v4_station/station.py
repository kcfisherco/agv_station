#!/usr/bin/env python3
import time, os, pyodbc, rclpy, logging, sys
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

class stack_light:
    def __init__(self, station_publisher):
        self.station = station_publisher

    def light_controller(self):
            if (not production):
                self.change_color(GPIO.HIGH, GPIO.HIGH, GPIO.LOW)
                self.station.cart_status = False
                print("color: Yellow")

            elif (GPIO.input(pin_input[0]) and GPIO.input(pin_input[1])):
                self.change_color(GPIO.LOW, GPIO.LOW, GPIO.HIGH)
                self.station.cart_status = True
                print("color: Blue")

            elif (GPIO.input(pin_input[0]) ^ GPIO.input(pin_input[1])):
                self.change_color(GPIO.HIGH, GPIO.LOW, GPIO.LOW)
                self.station.cart_status = False
                print("color: Red")
                
            elif (docking and not GPIO.input(pin_input[0]) and not GPIO.input(pin_input[1])):
                self.flash_light(GPIO.HIGH, GPIO.LOW, GPIO.LOW)
                self.station.cart_status = False
                # Flashing Red

            elif (not GPIO.input(pin_input[0]) and not GPIO.input(pin_input[1])):
                self.change_color(GPIO.LOW, GPIO.HIGH, GPIO.LOW)
                self.station.cart_status = False
                print("color: Green")

            else:
                self.station.cart_status = False
                logging.warning("Hmm... there was an unexpected condition:")
                logging.warning(f"Production running? {production}")
                logging.warning(f"Input pin {pin_input[0]}: {GPIO.input(pin_input[0])}")
                logging.warning(f"Input pin {pin_input[1]}: {GPIO.input(pin_input[1])}")
                logging.warning(f"is robot docking? {docking}")

    def change_color(self, red_power, green_power, blue_power):
        GPIO.output(pin_output[0], red_power)
        GPIO.output(pin_output[1], green_power)
        GPIO.output(pin_output[2], blue_power)

    def flash_light(self, r, g, b):
        self.change_color(r, g, b)
        print("color: Red")
        time.sleep(2)
        self.change_color(GPIO.LOW, GPIO.LOW, GPIO.LOW)
        print("color: OFF")
        time.sleep(1.5)
            
def update_database(station_number, station_publisher):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=fisher-agc.database.windows.net;DATABASE=Fisher_AGC;UID=fisher_agc;PWD=tTp##L86?qM!4iG7')
    cursor = cnxn.cursor()
    try:
        update_station = cursor.execute("""
                                        update Station
                                        set cart_in_place = ?
                                        where station_name = ?
                                        """, station_publisher.cart_status, station_number)
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

# TEMPORARY
# NOTE: Virtual test with sensors
def simulate_sensors(p1_power, p2_power):
        GPIO.setup(pin_input, GPIO.OUT, initial=GPIO.LOW)
        GPIO.output(pin_input[0], p1_power)
        GPIO.output(pin_input[1], p2_power)
        GPIO.setup(pin_input, GPIO.IN)
        print("Sensor Pins:")
        print(f"pin {pin_input[0]}: {p1_power}")
        print(f"pin {pin_input[1]}: {p2_power}")

"""Global Settings"""
station_name = (os.getenv('STATION_ID','station-x')).split('-')[1]
print("Starting Program for station: %s" % station_name)
pin_input = [11, 13]      # 11 = Sensor 1, 13 = Sensor 2
pin_output = [40, 38, 37] # 40 = CH1/Red : Power, 38 = CH2/Green : Power, 37 = CH3/Blue : Power

def main():
    rclpy.init(args=None)

    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin_input, GPIO.IN)
        GPIO.setup(pin_output, GPIO.OUT, initial=GPIO.LOW)
        simulate_sensors(GPIO.LOW, GPIO.LOW) # TEMPORARY: Change test parameters here
        station_publisher = StationPublisher()
        light = stack_light(station_publisher)
        executor = MultiThreadedExecutor()
        executor.add_node(station_publisher)
        executor_try = Thread(target=executor.spin, daemon=True)
        executor_try.start()
        while rclpy.ok():
            if (station_name != None):
                read_database(station_name)
                light.light_controller()
                update_database(station_name, station_publisher)
            else:
                logging.info("The Hostname of Station is not set, aborting program and set STATION_ID = station-x in 'sudo gedit ~/.bashrc' GOODBYE !")
                time.sleep(5)
                sys.exit()

    except (KeyboardInterrupt,SystemError,SystemExit,rclpy.exceptions.ROSInterruptException):
        station_publisher.destroy_node()
        executor.shutdown()
        exit()

    finally:
        GPIO.cleanup()
        rclpy.shutdown()

if __name__ == '__main__':
    main()