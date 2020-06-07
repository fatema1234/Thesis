import re

from nltk.corpus import stopwords
from nltk.stem import porter
from nltk.stem.util import suffix_replace, prefix_replace

from nltk.stem.api import StemmerI


class _LanguageSpecificStemmer(StemmerI):
  """
  This helper subclass offers the possibility
  to invoke a specific stemmer directly.
  This is useful if you already know the language to be stemmed at runtime.

  Create an instance of the Snowball stemmer.

  :param ignore_stopwords: If set to True, stopwords are
                           not stemmed and returned unchanged.
                           Set to False by default.
  :type ignore_stopwords: bool
  """

  def __init__(self, ignore_stopwords=False):
    # The language is the name of the class, minus the final "Stemmer".
    language = type(self).__name__.lower()
    if language.endswith("stemmer"):
      language = language[:-7]

    self.stopwords = set()
    if ignore_stopwords:
      try:
        for word in stopwords.words(language):
          self.stopwords.add(word)
      except IOError:
        raise ValueError(
          "{!r} has no list of stopwords. Please set"
          " 'ignore_stopwords' to 'False'.".format(self)
        )

  def __repr__(self):
    """
    Print out the string representation of the respective class.

    """
    return "<{0}>".format(type(self).__name__)


class _ScandinavianStemmer(_LanguageSpecificStemmer):
  """
  This subclass encapsulates a method for defining the string region R1.
  It is used by the Danish, Norwegian, and Swedish stemmer.

  """

  def _r1_scandinavian(self, word, vowels):
    """
    Return the region R1 that is used by the Scandinavian stemmers.

    R1 is the region after the first non-vowel following a vowel,
    or is the null region at the end of the word if there is no
    such non-vowel. But then R1 is adjusted so that the region
    before it contains at least three letters.

    :param word: The word whose region R1 is determined.
    :type word: str or unicode
    :param vowels: The vowels of the respective language that are
                   used to determine the region R1.
    :type vowels: unicode
    :return: the region R1 for the respective word.
    :rtype: unicode
    :note: This helper method is invoked by the respective stem method of
           the subclasses DanishStemmer, NorwegianStemmer, and
           SwedishStemmer. It is not to be invoked directly!

    """
    r1 = ""
    for i in range(1, len(word)):
      if word[i] not in vowels and word[i - 1] in vowels:
        if 3 > len(word[: i + 1]) > 0:
          r1 = word[3:]
        elif len(word[: i + 1]) >= 3:
          r1 = word[i + 1:]
        else:
          return word
        break

    return r1


class NorwegianStemmer(_ScandinavianStemmer):
  """
  The Norwegian Snowball stemmer.

  :cvar __vowels: The Norwegian vowels.
  :type __vowels: unicode
  :cvar __s_ending: Letters that may directly appear before a word final 's'.
  :type __s_ending: unicode
  :cvar __step1_suffixes: Suffixes to be deleted in step 1 of the algorithm.
  :type __step1_suffixes: tuple
  :cvar __step2_suffixes: Suffixes to be deleted in step 2 of the algorithm.
  :type __step2_suffixes: tuple
  :cvar __step3_suffixes: Suffixes to be deleted in step 3 of the algorithm.
  :type __step3_suffixes: tuple
  :note: A detailed description of the Norwegian
         stemming algorithm can be found under
         http://snowball.tartarus.org/algorithms/norwegian/stemmer.html

  """

  __vowels = "aeiouy\xE6\xE5\xF8"
  __s_ending = "bcdfghjlmnoprtvyz"
  __step1_suffixes = (
    "hetenes",
    "hetene",
    "hetens",
    "heter",
    "heten",
    "endes",
    "ande",
    "ende",
    "edes",
    "enes",
    "erte",
    "ede",
    "ane",
    "ene",
    "ens",
    "ers",
    "ets",
    "het",
    "ast",
    "ert",
    "en",
    "ar",
    "er",
    "as",
    "es",
    "et",
    "a",
    "e",
    "s",
  )

  __step2_suffixes = ("dt", "vt")

  __step3_suffixes = (
    "hetslov",
    "eleg",
    "elig",
    "elov",
    "slov",
    "leg",
    "eig",
    "lig",
    "els",
    "lov",
    "ig",
  )


  def stem(self, word):
    """
    Stem a Norwegian word and return the stemmed form.

    :param word: The word that is stemmed.
    :type word: str or unicode
    :return: The stemmed form.
    :rtype: unicode

    """
    word = word.lower()

    if word in self.stopwords:
      return word

    r1 = self._r1_scandinavian(word, self.__vowels)

    # STEP 1
    for suffix in self.__step1_suffixes:
      if r1.endswith(suffix):
        if suffix in ("erte", "ert"):
          word = suffix_replace(word, suffix, "er")
          r1 = suffix_replace(r1, suffix, "er")

        elif suffix == "s":
          if word[-2] in self.__s_ending or (
            word[-2] == "k" and word[-3] not in self.__vowels
          ):
            word = word[:-1]
            r1 = r1[:-1]
        else:
          word = word[: -len(suffix)]
          r1 = r1[: -len(suffix)]
        break

    # STEP 2
    for suffix in self.__step2_suffixes:
      if r1.endswith(suffix):
        word = word[:-1]
        r1 = r1[:-1]
        break

    # STEP 3
    for suffix in self.__step3_suffixes:
      if r1.endswith(suffix):
        word = word[: -len(suffix)]
        break

    return word



