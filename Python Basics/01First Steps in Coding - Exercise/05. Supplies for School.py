pencils = int(input()) * 5.80
markers = int(input()) * 7.20
liters = int(input()) * 1.20
percentage = int(input()) / 100

sum = (pencils + markers + liters) * (1 - percentage)

print(sum)
