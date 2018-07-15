import pandas as pd





ecom = sal = pd.read_csv('./02-exercises/Ecommerce Purchases')
print(ecom.head(5))
print()


print(
    ecom['CC Exp Date'].apply(lambda x: x[-2:]=='25').sum()
)








