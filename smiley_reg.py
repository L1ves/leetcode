import re

def count_smileys(arr):
  """
  Counts the number of valid smiley faces in an array.

  Args:
    arr: A list of strings representing potential smiley faces.

  Returns:
    The number of valid smiley faces in the array.
  """
  regex = r"[:;][\-~]?[)D]"
  count = 0

  for smiley in arr:
    if re.fullmatch(regex, smiley):
      count += 1

  return count



from re import findall
def count_smileys(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))