import pandas as pd
from word_count import wordcount_stemmed


#read excel file

icd_10_excel = pd.read_excel(r'./ICD-10.xlsx', sheet_name='Alle gyldige koder')
n1 = pd.DataFrame(icd_10_excel).to_numpy()

token_frequency = {}

for row in n1:
    #sentence check
    if(pd.isna(row[0]) == False):
        rows = row[1]+ ' '+row[2]
        token_split = list(set(rows.split()))

        for token in token_split:
            print(token + " ---->")
            if token in token_frequency:
                print(token_frequency[token])
            else:
                token_frequency[token] = wordcount_stemmed("norske.txt", token)
                print(token_frequency[token])

print(token_frequency)