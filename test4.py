from stemming import NorwegianStemmer
import pandas as pd



def wordcount(filename, listwords, fullsentececheck=False):
  try:
    file = open(filename, "r", encoding=",utf8")
    read = file.readlines()
    file.close()

    norwegianStemmer = NorwegianStemmer()

    if (fullsentececheck == False):
         listwords = listwords.split()
         for word in listwords:
          lower = word.lower()
          count = 0
          for sentance in read:
             line = sentance.split()
             for each in line:
               line2 = each.lower()
               line2 = line2.strip("%#&")
               if lower == line2:
                 count += 1
          print(lower,":", count)
    else:
       lower = norwegianStemmer.stem(listwords.lower())
       count = 0
       for sentance in read:
         line = sentance.lower()
         for each in line:
            line2 = norwegianStemmer.stem(each.lower())
            line2 = line2.strip("%#&")
            if lower == line2:
              count += 1
       print(lower, ";", count)

  except FileExistsError:
      print("The file is not there")

icd_10_excel = pd.read_excel(r'./ICD-10.xlsx', sheet_name='Alle gyldige koder')
n1 = pd.DataFrame(icd_10_excel).to_numpy()

for row in n1:
    if (pd.isna(row[0]) == False):
      print(str(row[0]) + '-->')
      wordcount("norske.txt", row[1], True)
      print('\n')
     # wordcount("norske.txt", row[2], True)
      #print('\n')










