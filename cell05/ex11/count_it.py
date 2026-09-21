#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("none")
else:
    print(f"paremeters: {len(sys.argv)-1}")
    print(*[f"{i}: {len(i)}" for i in sys.argv[1:]], sep="\n")