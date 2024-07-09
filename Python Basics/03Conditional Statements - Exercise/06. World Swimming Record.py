import math

recSeconds = float(input())
meters = float(input())
secondsPerMeter = float(input())


ivansTime = meters * secondsPerMeter
slowing = math.floor(meters / 15) * 12.5




ivansTime = ivansTime + slowing



left = recSeconds - ivansTime

if left <= 0:
    print(f'No, he failed! He was {abs(left):.02f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {abs(ivansTime):.02f} seconds.')
