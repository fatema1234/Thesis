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
        token_frequency[rows] = wordcount_stemmed("norske.txt", rows)
    print(token_frequency[sentance])

print(token_frequency)