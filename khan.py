

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


def revWord(word, pos=0, rev=''):
    if pos < len(word)-1:
        rev = revWord(word, pos+1)
    return rev+word[pos]


print(revWord('banana'))


def binomialSquare(num, epsilon=0.001):
    guess = num/2
    low, high = 1, num
    while abs(guess**2 - num) > epsilon:
        if guess**2 < num:
            low = guess
        elif guess**2 >= num:
            high = guess
        guess = (high+low) / 2
        print(guess)
    return guess



print(binomialSquare(16))


# do selection sort, merge sort, binomial square


def selectionSort(li):
    for a in range(len(li)):
        lowest = a
        for b in range(a, len(li)):
            if li[b] < li[lowest]:
                lowest = b
        li[a], li[lowest] = li[lowest], li[a]
    return li


nums = [5,6,9,84,12,23,55,1,3,45,8,9,2]
# print(selectionSort(nums))


def merge1(li):
    if len(li) < 2:
        return li
    mid = len(li) // 2
    left = merge1(li[:mid])
    right = merge1(li[mid:])
    return merge2(left, right)


def merge2(left, right):
    merged = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged.append(left[l])
            l+=1
        else:
            merged.append(right[r])
            r+=1
    if l < len(left):
        merged.extend(left[l:len(left)])
    elif r < len(right):
        merged.extend(right[r:len(right)])
    return merged


print(merge1(nums))


def binomSquare(num, epsilon=0.0001):
    low, high = 0, num
    mid = (low + high) / 2
    while abs(num - mid**2) > epsilon:
        if mid**2 < num:
            low = mid
        else:
            high = mid
        mid = (low + high) / 2
    return mid


print(binomSquare(81))









































