a = []
b = []
new_list = []
import sys

a = input('Enter first list (no more than 10 numbers) separated by spaces: ').split()
b = input('Enter second list of equal length separated by spaces: ').split()

a1 = [int(i) for i in a]
b1 = [int(i) for i in b]

if len(a1) > 10 or len(b1) > 10 or len(a1) != len(b1):
    print('Incorrect list range')
    sys.exit()
else:
    for char in a1:
        for num in b1:
            new_char = (char, num)
            new_list.append(new_char)

print('AxB =', new_list)
