#!/usr/bin/env python3

num = int(input('Enter a number: '))

print(*(f"{n} x {num} = {n*num}" for n in range(10)), sep='\n')