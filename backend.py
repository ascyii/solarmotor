from adafruit_servokit import ServoKit


class Motor:
    """Model a type of servo motor."""

    # Default vaules for every motor
    MAX_PULSE = 2500
    MIN_PULSE = 500
    COVERAGE = 180  # Total degree of freedom in degrees
    OFFSET = 0  # In degrees a constant to be added
    SCALE = 1  # Scaling

    # Used for ids
    count = 0

    def __init__(self, board, angle=0):
        self.board = board
        self.id = Motor.count
        Motor.count += 1

        self.angle = angle
        self.offset = Motor.OFFSET  # Fine grained controls over every motor
        self.coverage = Motor.COVERAGE
        self.scale = Motor.SCALE

        # Initialization
        self.set()

    # Update the motor position on hardware
    def set(self):
        self.board.kit.servo[self.id].angle = self.angle * self.scale + self.offset

    def safe_set_angle(angle=0, sleep=0.01, offset=1):
        kit.servo[NUM].angle = angle + offset
        time.sleep(sleep)
        kit.servo[NUM].angle = angle

    def set_angle(self, angle):
        self.angle = min(self.coverage, max(0, angle))  # Double check bad
        self.set()

    def __str__(self):
        return f"Motor {self.id} is set at {self.angle} degrees."

    def inc(self, inc):
        self.angle += inc
        self.angle = min(max(self.angle, 0), Motor.COVERAGE)  # Clip
        self.set()


class Board:
    MIN = 500
    MAX = 2500

    def __init__(self, channels=16, frequency=50):
        self.channels = channels
        self.frequency = frequency
        self.kit = ServoKit(channels=channels, frequency=frequency)

        for i in range(channels):
            self.kit.servo[i].set_pulse_width_range(Board.MIN, Board.MAX)
            self.kit.servo[i].actuation_range = 180
            self.kit.servo[i].angle = 0
