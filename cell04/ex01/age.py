#!/usr/bin/env python3

age = int(input('Please tell me your age: '))
print(f'You are currently {age} years old.')
print(*(f"In {n} years, you'll be {age+n} years old.15" for n in range(10,31,10)), sep="\n")