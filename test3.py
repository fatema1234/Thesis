import pandas as pd
import chapters
from word_count import wordcount
from word_count import wordcount_stemmed

from stemming import NorwegianStemmer
import pandas as pd

norwegianStemmer = NorwegianStemmer()

icd_10_excel = pd.read_excel(r'./ICD-10.xlsx', sheet_name='Alle gyldige koder')
n1 = pd.DataFrame(icd_10_excel).to_numpy()

for w in n1:
     lower = norwegianStemmer.stem(word.lower())
print(norwegianStemmer.stem(w))


