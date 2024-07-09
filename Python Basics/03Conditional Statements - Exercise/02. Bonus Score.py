num = int(input())

bonus = 0

if num <= 100:
    bonus = 5

else:
    if num > 100:
        bonus = num * 0.20
    if num > 1000:
        bonus = num * 0.10

if num % 2 == 0:
    bonus = bonus +  1

if num % 10 == 5:
    bonus = bonus +  2

print(bonus)
print(bonus + num)
