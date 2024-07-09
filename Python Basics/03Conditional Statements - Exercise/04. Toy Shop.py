priceWanted = float(input())

puzzle = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

sumPrice = puzzle * 2.60 + dolls * 3 + bears * 4.10 + minions * 8.20 + trucks * 2

sum = puzzle + dolls + bears + minions + trucks


if sum >= 50:
    sumPrice = sumPrice * 0.75


sumPrice = sumPrice * 0.90

left = priceWanted - sumPrice

if left <= 0:
    print(f'Yes!{abs(left): .02f} lv left.')
else:
    print(f'Not enough money!{abs(left): .02f} lv needed.')
