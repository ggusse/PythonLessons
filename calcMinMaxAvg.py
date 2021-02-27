values = [
    0.0,
    0.0,
    0.0,
    0.0,
    0.0
    ]

int_value = [
    0.0,
    0.0,
    0.0,
    0.0,
    0.0
    ]

for value in range(5):
    values[value] = float(input('Input value %d:' % (value + 1)))

total = sum(values)
average = total / len(values)
maxv = max(values)
minv = min(values)

for value in range(5):
    int_value[value] = float(values[value] + (values[value] * 0.2))
    
print('\nTotal = %f' %total)
print('Average = %f' %average)
print('Maximum = %f' %maxv)
print('Minimum = %f' %minv)

for value in range(5):
    print('Value %d with %%20 interest is %f' % ((value + 1), int_value[value]))
