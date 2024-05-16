#!/usr/bin/env python3

# Author: Vi Dat Luu
# Author ID: 123964512
# Date Created: 2024/01/25
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <countdown_value>")
    sys.exit(1)


timer = int(sys.argv[1])


while timer > 0:
    print(timer)
    timer -= 1


print("blast off!")


