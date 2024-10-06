def has_duplicate (list):
  test_list = []
  if list == []:
    return False 
  for i in range (len(list)):
    if list [i] in test_list:
      return True
    test_list.append(list [i])
  return False 