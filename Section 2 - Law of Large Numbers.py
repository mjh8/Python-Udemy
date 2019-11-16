# Section 2 - Law of Large Numbers

import numpy as np
from numpy.random import randn

randn(100) #Array with 100 random values

N = 10000
counter = 0
for i in randn(N):
    if i > -1 and i < 1:
        counter = counter + 1
counter/N      

# The higher you increase N (sample size), the closer you get to the expected value

# Proves Law of Large Numbers Works