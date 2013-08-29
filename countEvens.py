#!/usr/bin/env python3

# Declare global variables
n = 0

# Setup function
def setup():
    global n
    n = 100

def loop():
    global n
    n = n + 1
    if ((n % 2) == 0):
        print(n)

# Main
setup()
while (n <= 120):
    loop()
