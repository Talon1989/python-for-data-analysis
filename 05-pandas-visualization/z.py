



dic = {'one': [1,5,3], 'two': [22,65,95]}

while True:
    try:
        text = input('enter key: ')
        int(text)
    except ValueError:
        break
    print('please a non digit string')


number = 88
try:
    dic[text].append(number)
except KeyError:
    dic[text] = []
    dic[text].append(number)





print(dic)










