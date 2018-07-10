import random

import numpy as np
import pandas as pd




nations = pd.Series(['Italy', 'Spain', 'Greece', 'Germany'])


def throwNeedles(numNeedles):
    inCircle = 0
    for _ in range(1, numNeedles+1, 1):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) ** 0.5 <= 1:  # x**2 + y**2 = hypotenuse**2, since radius is one, if it's more than 1 is outside of the circle
            inCircle += 1
    return (4 * inCircle) / numNeedles


print(throwNeedles(20000))

