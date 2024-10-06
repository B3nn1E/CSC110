def invert_dictionary(dictionary):
  new_dict ={}
  for k,v in dictionary.items():
    if v not in new_dict:
      new_dict[v]=[k]
    else:
      new_dict[v].append(k)
  return new_dict

