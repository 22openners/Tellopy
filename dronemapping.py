### Insert here a brief explanation of what CODE SECTION 1 does ###
# Imports libraries for use in the project. The KPM is a module that we made in order to register the Key Presses.
# The djitellopy is an SDK(

from djitellopy import Tello
import KeyPressModule as kp
import cv2
import numpy as np
import time
import math

### END CODE SECTION 1 ###

# Insert here a brief explanation of what CODE SECTION 2 does ###
# Sets variables forward speed and angular speed and then turns them into distance and angular intervals`
#

############ PARAMETERS ############
fSpeed = 56  # Forward/Backward cm/sec
aSpeed = 26  # Angular Velocity, Degrees/sec
interval = 0.25

dInterval = fSpeed * interval  # Distance Interval
aInterval = aSpeed * interval  # Angular Interval
#########################################


### END CODE SECTION 2 ###

x, y = 500, 500
a = 0
yaw = 0

kp.init()
tello = Tello()
# tello.connect()
# print(tello.get_battery())

points = []


# global img
# tello.streamon()

### Insert here are brief explanation of what CODE SECTION 3 does ###
# Sets the base position, acceleration, and yaw variables.
# Initializes the Key Press Module as kp. And sets djitellopy to tello. Opens an empty list called points.
# Sets the function for getting the keyboard input through use of the Key Press Module as kp.

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    global x, y, yaw, a
    d = 0

    if kp.getKey("LEFT"):
        lr = -speed
        d = dInterval
        a = 180

    elif kp.getKey("RIGHT"):
        lr = speed
        d = -dInterval
        a = -180

    if kp.getKey("UP"):
        fb = speed
        d = dInterval
        a = 270

    elif kp.getKey("DOWN"):
        fb = -speed
        d = -dInterval
        a = -90

    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed

    if kp.getKey("a"):
        yv = -speed
        yaw += aInterval

    elif kp.getKey("d"):
        yv = speed
        yaw -= aInterval

    if kp.getKey("q"):
        tello.land()
        time.sleep(3)
    if kp.getKey("e"): tello.takeoff()

    ### END CODE SECTION 3 ###

    #   if kp.getKey("z"):
    #       cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
    #       time.sleep(0.3)

    time.sleep(interval)
    a += yaw
    x += int(d * math.cos(math.radians(a)))
    y += int(d * math.sin(math.radians(a)))

    return [lr, fb, ud, yv, x, y]


### Insert here a brief explanation of what CODE SECTION 4 does ###
# Does the math for the acceleration and the position and returns the values of the keyboard calls.
# Also sets the function for drawing points through the open-cv module and used the .circle command to set a red point.


def drawPoints(img, points):
    for point in points:
        cv2.circle(img, point, 5, (0, 0, 255), cv2.FILLED)


### END CODE SECTION 4 ###

### Insert here a brief explanation of what CODE SECTION 5 does ###
# Gets the keyboard input and sends it to the drone through the send_rc_control.
# Opens the img window and appends the points list to begin drawing points and shows the output of the map

while True:
    vals = getKeyboardInput()
    tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = np.zeros((1000, 1000, 3), np.uint8)
    points.append((vals[4], vals[5]))
    drawPoints(img, points)
    cv2.imshow("Output", img)
    cv2.waitKey(1)

### END CODE SECTION 5 ###


### Ignore the following code, it's related to the Surveillance program and not used in the MAPPING Program ###

# img = tello.get_frame_read().frame
# img = cv2.resize(img, (360, 240))
# cv2.imshow("image", img)
# cv2.waitKey(1)
