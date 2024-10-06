def count_vowels (string):
  new_dict={"a":0,"e":0,"i":0,"o":0,"u":0,"A":0,"E":0,"I":0, "O":0,"U":0}
  for char in string:
    if char in "UEOAIueoai":
      new_dict[char]+=1
  return new_dict

