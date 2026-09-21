#!/usr/bin/env python3

import sys

def downcase_it(text=None):
    return text.lower() if text is not None else "none"

if len(sys.argv) < 2:
    print("none")
else:
    print(*[downcase_it(i) for i in sys.argv[1:]], sep="\n")
