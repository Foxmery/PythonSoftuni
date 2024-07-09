deposit = float(input())
months = int(input())
yearsPercentage = float(input()) / 100
final = deposit + months * ((deposit * yearsPercentage)/12)
print(final)

