#!/usr/bin/env python3

import sys, re

if len(sys.argv) != 3:
    print("none")
else:
    matched = re.findall(sys.argv[1], sys.argv[2])
    print(len(matched) if matched else "none")