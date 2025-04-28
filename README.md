# Line Following Robot

This project implements a basic autonomous line-following robot using a Raspberry Pi, DC motors, IR sensors, and GPIO-based control.  
The robot detects the black/white track using two infrared (IR) sensors and adjusts its motor movements to follow the path accurately.

---

## Features

- Automatic detection of line using IR sensors
- Moves forward, turns left, or turns right based on sensor input
- Stops when no line is detected
- Manual activation using a button press
- LED status indicator for activation

---

## Hardware Components

- Raspberry Pi (any version with GPIO support)
- 2 DC Motors (for left and right wheels)
- Motor Driver (L298N or similar)
- 2 IR Sensors (for line detection)
- 1 Push Button (to start/stop)
- 1 LED (for status indication)
- Breadboard, Jumper wires, Power supply

---

## Software and Libraries

- Python 3.x
- RPi.GPIO (GPIO library for Raspberry Pi)
- time (standard Python library)

---

## Circuit Diagram (Overview)

| Component | GPIO Pin |
|:--|:--|
| Motor 1 | 25 |
| Motor 2 | 18 |
| Motor 3 | 24 |
| Motor 4 | 12 |
| Enable 1 (PWM) | 6 |
| Enable 2 (PWM) | 19 |
| Button | 4 |
| LED | 17 |
| Right IR Sensor | 20 |
| Left IR Sensor | 16 |

- Motors are controlled using GPIO outputs.
- PWM signals are used to control motor speed.
- IR sensors provide binary inputs (0 for black, 1 for white).

---

## How It Works

1. **Initialization:**
   - Motors, button, LED, and sensors are initialized using GPIO setup.
   - PWM is enabled for motor speed control.

2. **Button Activation:**
   - Robot remains idle until the button is pressed.
   - Upon button press, the LED turns ON and robot becomes active.

3. **Movement Control:**
   - If both IR sensors detect black (`0-0`): **Move Forward**
   - If right sensor white, left sensor black (`1-0`): **Turn Right**
   - If right sensor black, left sensor white (`0-1`): **Turn Left**
   - If both sensors white (`1-1`): **Stop**

4. **Loop:**
   - The robot continuously reads IR sensor values and adjusts its motion in real-time.

---

## Code Overview

```python
import RPi.GPIO as GPIO
import time

# Motor, Button, and LED GPIO setup
# Sensor reading loop
# Move forward, turn left/right, stop based on sensor inputs
# PWM used for speed control

