"""
In this task, you will help a farmer who wants to calculate the area of a rectangular field.

Inputs will be given as floats in the following order:

Length of the field (in meters)
Width of the field (in meters)
You must calculate the area in decares and print the result as a float with 2 digits after decimal point.

Hint: 1 square meters = 0.001 decares
Important: In order to let the system evaluate your code correctly you should not use any argument for the input function and comply with the output format

"""

length = float(input())
width = float(input())
area = length * width / 1000
print("{:.2f}".format(area))

