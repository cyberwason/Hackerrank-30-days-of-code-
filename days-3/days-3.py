#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
# chequeo si es par o impar primero
    if N % 2 != 0:
        print("Weird")
    else:
        # ahora reviso los rangos que pide el problema
        if N >= 2 and N <= 5:
            print("Not Weird")
        elif N >= 6 and N <= 20:
            print("Weird")
        else:
            print("Not Weird")