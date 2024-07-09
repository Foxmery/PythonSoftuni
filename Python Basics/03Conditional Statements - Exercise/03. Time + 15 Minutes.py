inHours = int(input())
inMinutes = int(input())

sum = inHours * 60 + inMinutes
after = sum + 15

seconds = after % 60
minutes = int((after - seconds) / 60)

if minutes >= 24:
    minutes = 0

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
