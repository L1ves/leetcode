#def canConstruct(ransomNote, magazine):
  """
  Дано две строки ransomNote и magazine. Верните true, если ransomNote может быть построен с использованием букв из magazine, и false в противном случае.

  Каждая буква в magazine может использоваться только один раз в ransomNote.

  Args:
    ransomNote: Строка, которую нужно построить.
    magazine: Строка, из которой можно брать буквы.

  Returns:
    True, если ransomNote может быть построен из magazine, и false в противном случае.
  """
  # Создаём словарь для хранения частоты букв в magazine.
  #   magazineCount = {}
  #   for letter in magazine:
  #       if letter not in magazineCount:
  #           magazineCount[letter] = 0
  #       magazineCount[letter] += 1
  #   for letter in ransomNote:
  #       if letter not in magazine or magazineCount[letter] <= 0:
  #           return False
  #       magazineCount[letter] -= 1
  #   return True


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        st1, st2 = Counter(ransomNote), Counter(magazine)
        if st1 & st2 == st1:
            return True
        return False