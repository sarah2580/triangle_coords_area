'''
import os
os.chdir('/Users/schen2580/Desktop/Python')
import triangle_area
triangle_area.main()

import importlib
importlib.reload(triangle_area)
triangle_area.main()
'''

def triangle_area():
    first_x, first_y = [float(v) for v in input("Enter the coord of 1st point: ").split(',')]
    second_x, second_y = [float(v) for v in input("Enter the coord of 2nd point: ").split(',')]
    third_x, third_y = [float(v) for v in input("Enter the coord of 3nd point: ").split(',')]

    x_points = [(first_x, first_y), (second_x, second_y), (third_x, third_y)]

    point_list = [(first_x, first_y), (second_x, second_y), (third_x, third_y)]
    point_list = sorted(point_list, key=lambda point: point[0])
    min_x_point = point_list[0][0]
    min_yx_point = point_list[0][1]
    mid_x_point = point_list[1][0]
    mid_yx_point = point_list[1][1]
    max_x_point = point_list[2][0]
    max_yx_point = point_list[2][1]

    left_trap_area = (mid_x_point - min_x_point) * ((mid_yx_point + min_yx_point)/2)
    right_trap_area = (max_x_point - mid_x_point) * ((mid_yx_point + max_yx_point)/2)
    bottom_trap_area = (max_x_point - min_x_point) * ((min_yx_point + max_yx_point)/2)

    main_trap = left_trap_area + right_trap_area
    triangle_area = abs(main_trap - bottom_trap_area)

    print('the area of the triangle is {0}'.format(triangle_area))


def main():
    triangle_area()
    while True:
        should_loop = input('do you want to go again?  ')
        if should_loop == 'yes':
            triangle_area()
        elif should_loop == 'no':
            return
        else:
            print('its just yes or no')
            continue
