import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict= {row.letter:row.code for (index, row) in data.iterrows()}
print(nato_dict)
user_input=input("Enter a word to see its nato codes").upper()
list_of_codes=[]
for i in user_input:
    list_of_codes.append(nato_dict[i])
print(list_of_codes)
