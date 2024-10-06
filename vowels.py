def count_vowels(string):
  index = 0
  vowels = 0
  while index < len (string): 
    if string [index] in "ueoaiUEOAI":
       vowels += 1
    index +=1 
  return vowels
