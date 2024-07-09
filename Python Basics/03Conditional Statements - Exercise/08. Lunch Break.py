import math

name = input()
length = int(input())
breaking = int(input())

launch = breaking / 8
calmness = breaking / 4


after = breaking - launch - calmness


left = math.ceil(length - after)

if left <= 0:
    print(f'You have enough time to watch {name} and left with {abs(left)} minutes free time.')
else:
    print(f'You don\'t have enough time to watch {name}, you need {abs(left)} more minutes.')
