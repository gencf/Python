"""
A ball is thrown down from a height of 355 m. The ball starts to fall with its initial velocity of 4 m/s, according to the second law of Newton, by assuming that air resistance is negligible.

The equation below expresses the vertical displacement of the ball at time t:

y=v0×t+0.5×g×t2

where v0 is the initial velocity, g is the gravitational acceleration (9.81 ms−2), and t is elapsed time.

Note that the equation above gives the displacement of the ball in the air, it does not give the height above ground.

Write a program that finds the height of the ball at any time t, which will be given by the user as a float. Your program should print this height as a float with 2 digits after decimal point.

"""

time = float(input())
height = 355 - 4 * time - 4.905 * time**2
print("%.2f" % height)

