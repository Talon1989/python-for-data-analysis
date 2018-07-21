import random
import pylab as py


diceOutcomes = [1,2,3,4,5,6]


def rolls(num=1):
    finalOutcomes = []
    for _ in range(10000):
        outcomes = []
        for _ in range(num):
            outcomes.append(random.choice(diceOutcomes))
        finalOutcomes.append(sum(outcomes) / len(outcomes))
    return finalOutcomes


r1 = rolls()
r2 = rolls(10)


py.hist(r1, bins=12)
py.hist(r2, bins=12)
py.show()

