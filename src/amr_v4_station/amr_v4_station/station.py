#!/usr/bin/env python3
import time, rclpy, logging, sys
import Jetson.GPIO as GPIO

from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from threading import Thread

class Sensor(Node):
    def __init__(self):
        super().__init__("sensor_status")
    #     self.publisher = self.create_publisher(bool, "sensor_status", 10)
    #     self.timer = self.create_timer(1.0, self.callback)

    # def callback(self):
    #     pass

class Relay(Node):
    def __init__(self):
        super().__init__("relay_status")
        #Temp
        self.pin_output = 7
        self.pin_input = [29, 33, 40]
        #Temp

        self.input_29 = GPIO.setup(29, GPIO.OUT, initial=GPIO.LOW)
        self.input_33 = GPIO.setup(33, GPIO.OUT, initial=GPIO.LOW)
        self.input_40 = GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW)
        #self.relay_subscriber = self.create_subscription(bool, "relay_status", self.display_relay_status(), 10)

    def display_relay_status(self, msg):
        self.logging().info(msg.data)

    def flag_relay_receiver(self, pin_number):
        prev_value = None
        value = GPIO.input(pin_number)
        if value != prev_value:
            if value == GPIO.HIGH:
                value_str = "HIGH"
            else:
                value_str = "LOW"
            print("Value read from pin {} : {}".format(pin_number,
                                                        value_str))
            prev_value = value

    def simulator(self):
        GPIO.output(self.pin_input[0], GPIO.HIGH)
        print("Outputting state: {} to pin: {}".format(GPIO.input(self.pin_input[0]), self.pin_input[0]))
        print("sleep 1000 seconds :D")
        time.sleep(1000)
        #print("Input Pin 29: ", GPIO.input(29))
        # GPIO.setup(29, GPIO.IN)
        # GPIO.setup(self.pin_input[0], GPIO.IN)
        # GPIO.wait_for_edge(self.pin_input[0], GPIO.RISING)
        # flag_relay_receiver()
        # GPIO.setup(29, GPIO.OUT)
        # GPIO.output(self.pin_input[0], GPIO.LOW)

"""Global Settings"""

def main():

    rclpy.init(args=None)
    GPIO.setwarnings("ignore")
    GPIO.setmode(GPIO.BOARD)

    try:

        sensor = Sensor()
        relay = Relay()
        executor = MultiThreadedExecutor()
        executor.add_node(sensor)
        executor.add_node(relay)
        logging.info("Initializing Station")
        executor_try = Thread(target=executor.spin,daemon=True)
        executor_try.start()

        while rclpy.ok():
            relay.simulator()
            sys.exit()

    except (KeyboardInterrupt,SystemError,SystemExit,rclpy.exceptions.ROSInterruptException):

        
        exit()

    finally:
        GPIO.cleanup()
        sensor.destroy_node()
        relay.destoy_node()
        rclpy.shutdown()
        print("shutting down :)")

if __name__ == '__main__':
    main()