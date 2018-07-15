import pandas as pd


def selectionSort(vector):
    for a in range(len(vector)):
        minn = a
        for b in range(a, len(vector)):
            if vector[b] < vector[minn]:
                minn = b
        vector[a], vector[minn] = vector[minn], vector[a]
    return vector


def bubbleSort(vector):
    operations = 0
    for o in range(len(vector)):
        for a in range(1, len(vector)-o):
            operations += 1
            if vector[a] < vector[a-1]:
                vector[a], vector[a-1] = vector[a-1], vector[a]
    print(operations)
    return vector


print(bubbleSort([1,2,68,4,55,6,0]))


def merge2(left, right):
    result = []
    lf, rg = 0, 0
    while lf < len(left) and (rg < len(right)):
        if left[lf] < right[rg]:
            result.append(left[lf])
            lf += 1
        else:
            result.append(right[rg])
            rg += 1
    if lf < len(left):
        result.extend(left[lf:])
    elif rg < len(right):
        result.extend(right[rg:])
    return result


def merge1(vector):
    if len(vector) < 2:
        return vector[:]
    middle = len(vector) // 2
    left = merge1(vector[:middle])
    right = merge1(vector[middle:])
    return merge2(left,right)


print(
    merge1([99,51,33,55,12,1,0,99,-1,59,-51])
)


# ecom = pd.read_csv('./02-exercises/Ecommerce Purchases')
# print(ecom.head(5))
# print()
# # view top 5 email providers
# print(
#     ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5)
# )
# print()
# # number of purchases above 50$
# print(
#     ecom[ ecom['Purchase Price']>50. ]['Address'].count()
# )


def reverseWord(word, pos=0, reversed_word=''):
    if pos < len(word)-1:
        reversed_word = reverseWord(word, pos+1)
    return reversed_word+word[pos]


# print(reverseWord('patatine e pollo'))




