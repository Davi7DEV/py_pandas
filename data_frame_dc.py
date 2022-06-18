import pandas as pd


data = input("data: ")
valor = input("valor: ")
produto = input("produto: ")
qtde = input("quantidade: ")

produtos = {'data': [data],
'valor': [valor],
'produto': [produto],
'qtde': [qtde],
}
prod_df = pd.DataFrame(produtos)
print(prod_df)