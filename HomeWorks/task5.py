#Description
#Write a python program that reads a number in inches, converts it to meters.
#Note: One inch is 0.0254 meter.
#Test Data
#INCH: 2000
#Expected Output :
#2000.0 inch is 50.8 meters


Inchs = float(input("Please enter inch to convert in meter") )
Meters = float(Inchs * 0.0254)
Meters = str(Meters)

print(Meters + " meters")