# Solarmotor

Mobilizing mirror cluster.

## Information

Use adafruit servokit to manage the servos through the external board.
Enable the I2C module for the rasberry pi.
Install the package and initialize with

```python
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
kit.servo[0].angle = 180
```

```text
https://pinout.xyz/ Full pinout for the rpi3
https://components101.com/sites/default/files/component_datasheet/SG90%20Servo%20Motor%20Datasheet.pdf Datasheet for the servomotor used
```

## Cables

From right to left

```
..............................
.        ----------       1x .
.                         2x .
.                         3x .
.                         xx .
.            ooooo        4x .
.            ooooo        xx .
.            ooooo        xx .
.                         xx .
.                         xx .
.                            .

1: white
2: purple
3: yellow
4: black
```
