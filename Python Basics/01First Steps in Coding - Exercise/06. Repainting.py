nylon = (int(input()) + 2) * 1.50
paint = int(input()) * 14.50 * 1.1
acetone = int(input()) * 5
bags = 0.4

hours = int(input())

sumMaterials = nylon + paint + acetone + bags
final = sumMaterials + sumMaterials * 0.3 * hours
print(final)
