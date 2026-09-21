#!/usr/bin/env python3

f_num = int(input("Enter the first number: "))
s_num = int(input("Enter the second number: "))
mult= f_num*s_num

print(f'{f_num} x {s_num} = {mult}')

if mult < 0 :
    print('This number is negative.')
elif mult == 0:
    print('This number is both positive and negative.')
else:
    print('This number is positive.')