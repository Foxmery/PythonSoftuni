num1 = int(input())
num2 = int(input())
num3 = int(input())

sum = num1 + num2 + num3

seconds = sum % 60

minutes = int((sum - seconds) / 60)

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
