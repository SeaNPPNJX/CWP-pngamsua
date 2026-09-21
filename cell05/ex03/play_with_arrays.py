#!/usr/bin/env python3

original_arr = [2, 8, 9, 48, 8, 22, -12 ,2]
new_arr = {i+2 for i in original_arr if i+2 > 5}

print(f'{original_arr}\n{new_arr}')