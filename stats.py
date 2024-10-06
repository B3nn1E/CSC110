"""
Ben Phan
CSC 110
Project-3
This program calculates the mean, variance, standard deviation, and the range of the maxiumum and minum values of a list of numbers. 

"""

def mean (numbers):
  """
This function returns the mean of a list of numbers
Args:
  numbers: list of numbers
Returns:
  A float rounded at 2 decimal represents mean value of the numbers list. 
    """
  index = 0
  result = 0
  while index < len (numbers):
    result = result + numbers [index]
    index +=1 
  return round (result/len(numbers),2 )

def variance (numbers):
  """
This function returns the mean of a list of numbers
Args:
  numbers: list of numbers
Returns:
  A float rounded at 2 decimal represents mean value of the numbers list. 
"""
  average = mean (numbers)
  index = 0
  result = 0
  while index < len (numbers):
    result = result + ((numbers [index]-average))**2
    index += 1
  return round (result / (len(numbers)-1),2 )

def sd (numbers):
  """
This function returns the standard deviation of a list of numbers
Args:
  numbers: list of numbers
Returns:
  A float rounded at 2 decimal represents standard deviation value of the numbers list. 
"""
  first_cal=variance (numbers)
  result = (first_cal)**0.5
  return round (result,2)

def list_range (numbers):
  """
This function returns the differecnes between the largest and smallest numeric values of a list of numbers
Args:
  numbers: list of numbers
Returns:
  A numerical value represents difference between the largest and the smallest numeric values of the numbers list. 
"""
  index = len (numbers) -1 
  max = numbers [index]
  min = numbers [index]
  while index >= 0:
    if numbers [index-1] > max:
      max = numbers [index -1]
    if numbers [index -1] < min:
      min = numbers [index -1]
    index -=1
  return max-min

  
  
  