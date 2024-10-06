def differences (set_1,set_2):
  common = set_1.intersection(set_2)
  difference = 0
  for v in set_1:
    if v not in common:
      difference += 1
  for v in set_2:
    if v not in common:
      difference +=1
  return difference

    