#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    print("Good job!" if input("What was the paremeter?: ") == sys.argv[1] else "Nope, sorry...")
