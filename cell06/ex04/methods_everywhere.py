#!/usr/bin/env python3

import sys

def slicez(text):
    text += "ZZZZZZZZ"
    return text[slice(8)]


if len(sys.argv) < 2:
    print("none")
else:
    print(*[slicez(i) for i in sys.argv[1:]], sep="\n")