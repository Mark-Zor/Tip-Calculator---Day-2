#Tip Calculator
print('Welcome to the tip calculator!')

bill = input('What was the total bill?\n$')

tip_percent = input('How much tip would you like to give? 10, 12, or 15?\n')

split = input('How many people to split the bill?\n')

tip = float(tip_percent) / 100 * float(bill)

total = (float(bill) + float(tip)) / int(split)

print(f'Each person should pay: ${round(total, 2)}')









