#author: AILEEN GRACE D. RABASTO

#computing for the area of the side of the square
# square_length = float(input('What is the length of the side of the square? '))
# area = square_length ** 2
# print(f'The area of the square is : {area:.1f}')
# print()

# area of the rectangle
# rectangle_length = float(input('What is the length of the rectangle? '))
# rectangle_width = float(input('What is the width of the rectangle? '))
# area_rectangle = rectangle_length * rectangle_width
# print(f'The area of the rectangle is: {area_rectangle::.1f}')

# radius of the circle
# radius_circle = float(input('What is the radius of the circle? '))
# area_circle = 3.14 * (radius_circle ** 2)
# print(f'The area of the circle is: {area_circle:.1f}. ')  

import math
#stretch assignment #1
#pi = math.pi
# radius = float(input("Enter radius of the circle: "))
# area = pi * (radius ** 2)
# print(f'The area of the circle is: {area:.1f}. ')  

#stretch assignment #2
pi = math.pi
# value = float(input("Enter a value: "))
# area_square = value ** 2
# area_circle = pi * (value ** 2)
# volume_cube = value * value * value
# volume_sphere = (4 / 3 * pi) * (value ** 3)
# print(f' The area of the square is: {area_square:.2f}')
# print(f' The area of the circle is: {area_circle:.2f}')
# print(f' The volume of the cube is: {volume_cube:.2f}')
# print(f' The volume of the sphere is: {volume_sphere:.2f}')

#stretch assignment #3:  cm to m conversion 
# area of a square convert in cm^2
sq_value = float(input("Enter the length of a square (in cm): "))
area_square = sq_value ** 2
print(f'The area of the square is : {area_square} cm^2')
print(f'The area of the square is : {area_square / 10000} m^2')
print()

#area of a circle
circle_value = float(input("Enter the radius of a circle (in cm): "))
area_circle = pi * (circle_value ** 2)
print(f' The area of the circle is: {area_circle} cm^2')
print(f' The area of the circle is: {area_circle/ 10000} m^2')
print()

# Area pf a rectamgle
rectangle_length = float(input('Enter the length of the rectangle (in cm) '))
rectangle_width = float(input('Enter the width of the rectangle? (in cm) '))
area_rectangle = rectangle_length * rectangle_width
print(f'The area of the rectangle is: {area_rectangle} cm^2')
print(f'The area of the rectangle is: {area_rectangle / 10000} m^2')
print()


