#!/usr/bin/env python3

import sys

print(*sys.argv[:0:-1], sep="\n") if len(sys.argv) >= 3 else print("none")
