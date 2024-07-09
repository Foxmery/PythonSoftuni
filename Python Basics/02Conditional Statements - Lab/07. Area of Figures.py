from math import pi

shape = input()
num1 = float(input())
area = 0

if shape == 'square':
    area = num1 * num1

elif shape == 'rectangle':
    num2 = float(input())
    area = num1 * num2
elif shape == 'circle':
    area = num1 * num1 * pi
elif shape == 'triangle':
    num2 = float(input())
    area = num1 * num2 /2
 
print(f'{area:.3f}')
