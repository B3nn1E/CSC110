def all_mappings (dictionary):
  new_list = []
  for key,values in dictionary.items():
    for value in values:
      new_list.append((key,value))
  return new_list