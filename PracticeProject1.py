#Convert Radian into Degrees
import math

rad = (float(input("Enter the angle in randian: ")))

deg = round(rad / (180*math.pi),7)

print (f"{rad}rad = {deg} degrees")