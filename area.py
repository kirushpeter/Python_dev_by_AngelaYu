

# program to calculate areas

# select the 2d shape.

# print the area and shape selected.

pi = 3.1425

shape = input('Enter the shape you want to calculate the area: ')

def rectangle():

    Length = float(input('Enter the value length: '))

    Width = float(input('Enter the value width: '))

    print(Length * Width)


def circle():

    radius = float(input('Enter the radius: '))

    print(pi*radius**2)



def triangle():

    base = float(input('Enter the base: '))

    height = float(input('Enter the value of height: '))


    print(1/2*base*height)


if shape == 'circle' or 'Circle':

    circle()

elif shape == 'rectangle' or 'Rectangle':

    rectangle()


elif shape == 'triangle' or 'Triangle':

    triangle()


else:

    print('That shape is not available')    

