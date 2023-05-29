"""
Copyright (c) 2023, rtiop
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.

from random import random
from math import sqrt
from cs50 import get_int
"""

dentro = x = y = 0
n = get_int("Número de experimentos: ")

for n in range(n):
    x = random()
    y = random()
    if sqrt((x**2) + (y**2)) <= 1:
        dentro += 1
pi = (dentro / n) * 4
print(pi)
