#!/usr/bin/env python3
import time, rclpy, logging, sys
import Jetson.GPIO as GPIO

from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from threading import Thread

from std_msgs.msg import Bool

class StationPublisher(Node):
    def __init__(self, database):
        super().__init__("station")
        self.db = database
        self.publisher = self.create_publisher(Bool, f"/{self.db.station_id}/cart_ready", 10)
        self.timer = self.create_timer(1.0, self.callback)
        self.get_logger().info("Station Publisher has started")

    def callback(self):
        message = Bool()
        message.data = False
        if (self.light_color()):
            message.data = True
            self.publisher.publish(message)
        else:
            self.publisher.publish(message)

    def light_color(self):
        if (not self.db.production_running):
            GPIO.output(pin_output[1], GPIO.LOW)
            GPIO.output(pin_output[2], GPIO.LOW)
            GPIO.output(pin_output[0], GPIO.HIGH)
            self.get_logger().info("Publishing color red")
            return False
        elif (self.get_gpio_pin(pin_input[0]) and self.get_gpio_pin(pin_input[1])):
            GPIO.output(pin_output[0], GPIO.LOW)
            GPIO.output(pin_output[1], GPIO.LOW)
            GPIO.output(pin_output[2], GPIO.HIGH)
            self.get_logger().info("Publishing color Blue")
            return True
        elif (self.get_gpio_pin(pin_input[0]) ^ self.get_gpio_pin(pin_input[1])):
            self.get_logger().info("Publishing color flashing yellow")
            return False
        else:
            GPIO.output(pin_output[0], GPIO.LOW)
            GPIO.output(pin_output[2], GPIO.LOW)
            GPIO.output(pin_output[1], GPIO.HIGH)
            self.get_logger().info("Publishing color Green")
            return False

    def get_gpio_pin(self, pin):
        prev_value = None
        value = GPIO.input(pin)
        if value != None:
            if value == GPIO.HIGH:
                value_str = "HIGH"
            else:
                value_str = "LOW"
            return value

def update_database():
    pass

def read_database():
    class db:
        station_id = "station209B"
        production_running = True
    return db()

def simulate_sensors(pins):
        GPIO.setup(pins, GPIO.OUT, initial=GPIO.LOW)
        GPIO.output(pins[0], GPIO.HIGH)
        GPIO.output(pins[1], GPIO.LOW)
        GPIO.setup(pins, GPIO.IN)
        print("Outputting state: {} to pin: {}".format(GPIO.input(pins[0]), pins[0]))
        print("Outputting state: {} to pin: {}".format(GPIO.input(pins[1]), pins[1]))

"""Global Settings"""
pin_input = [11, 13]
pin_output = [29, 33, 40] # 29 = Red; 33 = Green; 40 = Blue

def main():

    rclpy.init(args=None)

    try:

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin_input, GPIO.IN)
        GPIO.setup(pin_output, GPIO.OUT, initial=GPIO.LOW)

        simulate_sensors(pin_input)

        station = StationPublisher(read_database())
        executor = MultiThreadedExecutor()
        executor.add_node(station)
        executor_try = Thread(target=executor.spin, daemon=True)
        executor_try.start()

        time.sleep(1000)

        # while rclpy.ok():
        #     
        #     sys.exit()

    except (KeyboardInterrupt,SystemError,SystemExit,rclpy.exceptions.ROSInterruptException):
        station.destroy_node()
        executor.shutdown()
        exit()

    finally:
        GPIO.cleanup()
        rclpy.shutdown()
        print("shutting down :)")

if __name__ == '__main__':
    main()