# math expression format strings in decimal places
# cars = 3
# pip = 8
# totpip = pip / cars
#print(f'There are {totpip:.1f} people in each car. ')
#print(f'There are {totpip:.2f} people in each car. ')
#print(f'There are {totpip:.3f} people in each car. ')

#scientific notaion
distance = 9 * 1205 * 18
#for 3 digits
#print(f'The distance is : {distance:.3e} meters')
#for 6 digits
# print()
# print(f'The distance is : {distance:.6e} meters')

#thousands grouping
big_num = 123456789
# #without formattting
# print(f'The number is: {big_num}')

#print with "," formatting
# print(f'The number is: {big_num:,}')

# #print with "_" formatting
#print(f'The number is: {big_num:_}')

import math
# radius=5
# area = math.pi * (radius ** 2)
# print(f'The area is: {area}')

#ceiling formulas
# weight = 1.65
# lower = math.floor(weight)
# print(lower)
# print()
# higher = math.ceil(weight)
# print(higher)

#Convert Fahrenheit to Celsius
print()
fahrenheit=float(input('What is the tempereature in Fahrenheit? '))
# num = 32
# celsius = fahrenheit-num
# divcelcius = 5/9
# celsius2= celsius * divcelcius
celsius = (fahrenheit - 32) * 5 / 9
print(f'The temperature in Celsius is {celsius:.1f} degrees.')
#print(f'The temperature in Celsius is {celsius2:.1f} degrees.')

