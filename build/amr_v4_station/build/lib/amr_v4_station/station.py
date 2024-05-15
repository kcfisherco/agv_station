#!/usr/bin/env python3
import time, rclpy, logging, sys
import Jetson.GPIO as GPIO

from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from threading import Thread
from amr_v4_msgs_srvs.msg import Sensor

class SensorPublisher(Node):
    def __init__(self):
        super().__init__("sensor")
        self.publisher = self.create_publisher(Sensor, "/sensor_status", 10)
        self.timer = self.create_timer(1.0, self.test_on())

    def test_on(self):
        message = Sensor()
        message = True
        self.publisher.publish(message)

class RelaySubscriber(Node):
    def __init__(self):
        super().__init__("relay")
    #     self.relay_subscriber = self.create_subscription(Sensor, "sensor_status", self.detect_status, 10)

    # def detect_status(self, message):
    #     self.get_logger().info(message)

    def receive_input(self, pin):
        prev_value = None
        value = GPIO.input(pin)
        if value != prev_value:
            if value == GPIO.HIGH:
                value_str = "HIGH"
            else:
                value_str = "LOW"
            print("Value read from pin {} : {}".format(pin,
                                                        value_str))
            prev_value = value

    def simulator(self, pin):
        GPIO.output(pin, GPIO.HIGH)
        print("Outputting state: {} to pin: {}".format(GPIO.input(pin), pin))
        # print("Input Pin 29: ", GPIO.input(29))
        # GPIO.setup(29, GPIO.IN)
        # GPIO.setup(pin, GPIO.IN)
        # GPIO.wait_for_edge(pin, GPIO.RISING)
        # flag_relay_receiver()
        # GPIO.setup(29, GPIO.OUT)
        # GPIO.output(pin, GPIO.LOW)

"""Global Settings"""
pin_input = 7
pin_output = [29, 33, 40]

def main():

    rclpy.init(args=None)

    try:

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin_input, GPIO.IN)
        GPIO.setup(pin_output, GPIO.OUT, initial=GPIO.LOW)
        sensor = SensorPublisher()
        # relay = RelaySubscriber()
        rclpy.spin(sensor)
        # rclpy.spin(relay)

        # while rclpy.ok():
        #     relay.simulator(pin_output[0])
        #     sys.exit()

    except (KeyboardInterrupt,SystemError,SystemExit,rclpy.exceptions.ROSInterruptException):
        sensor.destroy_node()
        # relay.destoy_node()
        exit()

    finally:
        GPIO.cleanup()
        rclpy.shutdown()
        print("shutting down :)")

if __name__ == '__main__':
    main()