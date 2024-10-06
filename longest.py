def longest_string(list):
  longest = ""
  if list == []:
    return None
  for d in list:
    if d == {}:
      return None
    for value in d.values():
      if len(value) > len(longest):
        longest = value
  return longest