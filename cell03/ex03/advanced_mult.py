#!/usr/bin/env python3

num = 0
while num < 11:
    print(f"Table de {num}:", end=" ")
    count = 0
    while count < 11:
        print(num*count, end=" ")
        count+=1 
    print()
    num+=1