

def frange(x, y, jump):
  while x < y:
    yield x
    x += jump


def summation(low, high):
    counter = 0
    for i in frange(low, high, 0.5):
        counter += (0.1 * i ** 2) + 1
    return counter


def preciseRange(size, increment):
    """
    :param size: upper bound of range
    :param increment: steps for incrementation
    :return: yield incrementation by increment factor
    """
    for n in range(size*increment):
        yield n / increment


# print(summation(2,7))
for i in preciseRange(10,100):
    print(i)

