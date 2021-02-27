income = float(input('What is your weekly income? '))

tax_bracket = {
    'a':0.1,
    'b':0.15,
    'c':0.20,
    'd':0.30
    }

if income < 500:
    bracket = 'a'
elif  income < 1500:
    bracket = 'b'
elif  income < 2500:
    bracket = 'c'
else:
    bracket = 'd'

your_tax = tax_bracket[bracket]

tax = float(income * your_tax)

print('Your income is $%s ' % round(income, 2))
print('Your tax rate is %%%d ' % (your_tax * 100))
print('Your told tax paid is $%s ' % round(tax, 2))

    
