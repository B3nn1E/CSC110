def isfloat(string):
  for char in string:
    if char not in "0123456789.":
      return False
  return True 
      
def read_csv (file_name):
  f = open(file_name,"r")
  new_dict ={}
  for line in f:
    words = line.strip().split(",")
    k = words [0]
    v = []
    for i in range (1,len(words)):
      if words[i].isnumeric():
        v.append(int(words[i]))
      elif isfloat(words[i]):
        v.append(float(words[i]))   
      else: 
        v.append (words[i])
    new_dict [k]= v
  f.close ()
  return new_dict