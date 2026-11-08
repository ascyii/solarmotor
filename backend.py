from adafruit_servokit import ServoKit

# Constants
FREQ_MIN = 500
FREQ_MAX = 2500

CHANNELS = 16

print("Creating the backend driver")
kit = ServoKit(channels=CHANNELS, frequency=50)

print("Resetting every motor")
for i in range(CHANNELS):
    kit.servo[i].set_pulse_width_range(FREQ_MIN, FREQ_MAX)
    kit.servo[i].actuation_range = 180
    kit.servo[i].angle = 0
