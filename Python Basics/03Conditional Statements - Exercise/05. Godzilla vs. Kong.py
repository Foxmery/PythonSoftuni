budget = float(input())
people = int(input())
priceFor1 = float(input())

left = budget * 0.90

if people > 150:
    priceFor1 = priceFor1 * 0.90

left = left - priceFor1 * people

if left >= 0:
    print('Action!')
    print(f'Wingard starts filming with {abs(left):.02f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {abs(left):.02f} leva more.')

