# getting info from user and assigning it to user, telling them what their BMI means
# My solution to this problem sheet
#Author Saidhbh Foley
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))
bmi = weight/(height*height)

print ('Your bmi is', bmi)