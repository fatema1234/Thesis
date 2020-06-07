from stemming import NorwegianStemmer

def wordcount(filename, listwords, fullsentececheck=False):
  try:
    file = open(filename, "r", encoding="utf8")
    read = file.readlines()
    file.close()

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
        return count
    else:
      lower = listwords.lower()
      count = 0
      for sentance in read:
        line2 = sentance.lower()
        line2 = line2.strip("%#&")
        if lower in line2:
          count += 1
      return count
  except FileExistsError:
    print("The file is not there")


def wordcount_stemmed(filename, word):
  try:
    file = open(filename, "r", encoding="utf8")
    read = file.readlines()
    file.close()

    norwegianStemmer = NorwegianStemmer()

    lower = norwegianStemmer.stem(word.lower())
    count = 0
    for sentance in read:
      line = sentance.lower()
      for each in line:
        line2 = norwegianStemmer.stem(each.lower())
        line2 = line2.strip("%#&")
        if lower == line2:
          count += 1
    return count
  except FileExistsError:
    print("The file is not there")

