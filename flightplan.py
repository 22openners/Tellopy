from djitellopy import tello


drone = tello.Tello()
drone.connect()
#1
drone.takeoff()
drone.move_up(101)
#2
drone.move_forward(153)
#3
drone.rotate_counter_clockwise(90)     #Points north
#4
drone.move_forward(183)
#5 Points East and Lowers drone
drone.rotate_clockwise(90) #Points East
drone.move_down(92)
#6
drone.move_forward(92)
#7
drone.rotate_clockwise(90) #points South
#8
drone.move_up(31) #goes up to 40 ft
drone.move_forward(92) #flys forward 30ft
#9
drone.rotate_counter_clockwise(90) #points east
drone.move_forward(183)  #forward 60 ft
drone.land()
