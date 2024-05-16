#!/usr/bin/env python3

# Author: Vi Dat Luu
# Author ID: 123964512
# Date Created: 2024/01/25
import sys

if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3


while timer > 0:
    print(timer)
    timer -= 1


print("blast off!")


