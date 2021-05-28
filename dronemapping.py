from djitellopy import Tello
import KeyPressModule as kp
import cv2
import numpy as np
import time
import math

############ PARAMETERS ############
fSpeed = 112  # Forward/Backward cm/sec
aSpeed = 26  # Angular Velocity, Degrees/sec
uSpeed = 26  # Up/Down cm/sec
interval = 0.25

dInterval = fSpeed * interval  # Distance Interval
aInterval = aSpeed * interval  # Angular Interval
hInterval = uSpeed * interval  # Height Interval
#########################################
x, y = 500, 500
a = 0
yaw = 0

kp.init()
tello = Tello()
# tello.connect()
# print(tello.get_battery())
# global img
# tello.streamon()

points = []

def getKeyboardInput():

    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    global x, y, yaw, a
    d = 0

    if kp.getKey("LEFT"):
        lr = -speed
        d = dInterval
        a = -180

    elif kp.getKey("RIGHT"):
        lr = speed
        d = -dInterval
        a = 180

    if kp.getKey("UP"):
        fb = speed
        d = dInterval
        a = 270

    elif kp.getKey("DOWN"):
        fb = -speed
        d = -dInterval
        a = -90

    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"): ud = -speed

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

    if kp.getKey("z"):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
        time.sleep(0.3)

    time.sleep(interval)
    a += yaw
    x += int(d*math.cos(math.radians(a)))
    y += int(d*math.sin(math.radians(a)))


    return [lr, fb, ud, yv, x, y]


def drawPoints(img, points):
    for point in points:
        cv2.circle(img, points, 10, (255, 0, 0), cv2.FILLED)


while True:

    vals = getKeyboardInput()

    tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    img = np.zeros((1000, 1000, 3), np.uint8)
    points.append((vals[4],vals[5]))
    points = (vals[4], vals[5])
    drawPoints(img, points)

    cv2.imshow("Output", img)
    cv2.waitKey(1)

# img = tello.get_frame_read().frame
# img = cv2.resize(img, (360, 240))
# cv2.imshow("image", img)
# cv2.waitKey(1)
