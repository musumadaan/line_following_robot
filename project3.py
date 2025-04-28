import RPi.GPIO as GPIO
import time
m1 = 25
m2 = 18
m3 = 24
m4 = 12
button = 4
led = 17
isActive = False
GPIO.setmode(GPIO.BCM)

motor1 = GPIO.setup(m1, GPIO.OUT)
motor2 = GPIO.setup(m2, GPIO.OUT)
motor3 = GPIO.setup(m3, GPIO.OUT)
motor4 = GPIO.setup(m4, GPIO.OUT)
GPIO.setwarnings(False)
GPIO.setup(led, GPIO.OUT)
enable1_pwm = GPIO.PWM(6, 1000)
enable2_pwm = GPIO.PWM(19, 1000)
enable1_pwm.start(100)
enable2_pwm.start(100)

right_ir = GPIO.setup(20, GPIO.IN)
left_ir = GPIO.setup(16, GPIO.IN)

enable1 = 6
enable2 = 7


def move_forward():
    GPIO.output(m1, 0)
    GPIO.output(m2, 100)
    GPIO.output(m3, 0)
    GPIO.output(m4, 100)
    
def turn_right():
    GPIO.output(m1, 0)
    GPIO.output(m2, 0)
    GPIO.output(m3, 100)
    GPIO.output(m4, 0)
    
def turn_left():
    GPIO.output(m1, 0)
    GPIO.output(m2, 100)
    GPIO.output(m3, 0)
    GPIO.output(m4, 0)
    
def stop():
    GPIO.output(m1, 0)
    GPIO.output(m2, 0)
    GPIO.output(m3, 0)
    GPIO.output(m4, 0)
    
    
while True:
    GPIO.output(led, False)
    input_state = GPIO.input(button)
    if input_state == False:
        isActive = True
        GPIO.output(led, True)
        time.sleep(1)
    if isActive == True:

        right_val = GPIO.input(20)
        left_val = GPIO.input(16)
        print(str(right_val)+"-"+str(left_val))
        if right_val == 0 and left_val == 0:
            move_foward()
            
        elif right_val == 1 and left_val == 0:
            turn_right()
        
        elif right_val == 0 and left_val == 1:
            turn_left()
            
        else:
            stop()

    