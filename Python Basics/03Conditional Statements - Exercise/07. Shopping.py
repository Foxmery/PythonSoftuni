budget = float(input())
gpu = int(input())
cpu = int(input())
ram = int(input())

priceGpu = gpu * 250

priceCpu = priceGpu * 0.35 * cpu

priceRam = priceGpu * 0.10 * ram


sumPrice = priceCpu + priceRam + priceGpu

if gpu > cpu:
    sumPrice = sumPrice * 0.85

left = budget - sumPrice

if left >= 0:
    print(f'You have {abs(left):.02f} leva left!')
else:
    print(f'Not enough money! You need {abs(left):.02f} leva more!')
