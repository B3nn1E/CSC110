def get_elements(dict,n):
  new_list = []
  for k,v in dict.items():
    if k[0].isupper() or k[-1].isupper() or v >= n:
      new_list.append(v)
  return new_list