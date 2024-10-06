def stop_ascending (numbers):
  if numbers == []:
    return None
  for index in range (len (numbers)-1):
    if numbers [index+1]<numbers [index]:
      return index +1
  return len (numbers)
      
print( stop_ascending([]) ) # None
print( stop_ascending([1, 2, 3]) ) # 3
print( stop_ascending([1, 2, 3, 1, 5]) ) # 3
