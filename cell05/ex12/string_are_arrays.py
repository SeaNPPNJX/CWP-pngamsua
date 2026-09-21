#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    print(*["z" for i in sys.argv[1] if "z" in i], sep="")