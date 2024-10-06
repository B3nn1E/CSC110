def sum_nums (integers,n):
  total = 0
  for list in integers: 
    for item in list:
      if item < n:
        total += item
  return total 
        