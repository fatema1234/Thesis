import pandas as pd
import chapters
from word_count import wordcount

#read excel file

icd_10_excel = pd.read_excel(r'./ICD-10.xlsx', sheet_name='Alle gyldiga Koder')
n1 = pd.DataFrame(icd_10_excel).to_numpy()

Kode_frequency = {}

for row in n1:
 #sentence check:
    if(pd.isna(row[0]) == False):
         uten = wordcount("norske.txt", row[1], True)
         med = wordcount("norske.txt", row[2], True)

         Kode_frequency[row[0]] = {
            'chapter_name': chapters.getChapterName(str(row[0])),
            'med_text': row[1],
            'med': med,
            'uten_text': row[2],
            'uten': uten
         }
    print(Kode_frequency)
print(Kode_frequency)

