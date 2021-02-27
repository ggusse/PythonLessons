def reverse_concatenate (a, b, c):
    new_string = c[::-1] + b[::-1] + a[::-1]
    return new_string

string1 = input('Enter first string: ')

string2 = input('Enter second string: ')

string3 = input('Enter third string: ')

print(reverse_concatenate (string1, string2, string3))

