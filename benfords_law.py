""" 
Ben Phan
CSC110
Project -5
This program has 5 functions to determine if a set of data conforms to the Benford's law or not. 
"""

def isfloat(string):
  """
  This function returns if a string represents a float. 
  Args: 
    string: an input string to the function. 
  Returns: 
    A bool that determine if the string represents a float. 
  """
  #iterate over each character in the string
  for char in string:
    #if the character does not repressent numerical value or a period
    if char not in "0123456789.":
      return False
  return True 
  
def csv_to_list (file_name):
  """
  This function returns if a list that contains strings which represents only integers or floats. 
  Args: 
    file_name: string for file_name. 
  Returns: 
    A list contains strings which only represent integers or floats. 
  """
  f = open (file_name, "r")
  new_list = []
  # iterate over line of file
  for line in f:
    #stripping the new line characters and split the line by a comma. 
    name = line.strip("\n").split(",")
    # iterate over index in name 
    for i in range (len(name)):
      # check if each string represent a numbe or a float 
      if name [i].isnumeric() or isfloat(name[i]):
        new_list.append(name[i])
  f. close()
  return new_list 

def count_start_digits (numbers):
  """
  This function counts the amount of numbers from 1 to 9 of the beginning of each character on a number list. 
  Args: 
    numbers: a list of string that represents integers or floats. 
  Returns: 
    A dictionary which contains the number counts of every beginning characters of an item on a number list (beside 0).  
  """
  new_dict = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
  # iterate over item in the list 
  for item in numbers:
    number = int(item[0])
    # do not include 0
    if number != 0:
      new_dict [number] +=1
  return new_dict 

def digit_percentages (count):
  """
  This function return the percentage of the amount of numbers from 1 to 9 of the beginning of each character on a number list. 
  Args: 
    count: a dictionary which contains the amount of numbers from 1 to 9 of the beginning character in a number list. 
  Returns: 
    A dictionary which contains the percentage of numbers from 1-9 of every beginning characters of an item on a number list (beside 0).  
  """
  newer_dict = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
  total = 0
  # iterate over  value in the dictionary
  for value in count.values():
    total += value
  # iterate over key and value in the dictionary
  for key, value in count.items():
    percentage = round ((value / total)*100,2)
    newer_dict [key] += percentage 
  return newer_dict 

def check_benfords_law (percentages):
  """
  This function return if an arguement follows Benfords' Law. 
  Args: 
    percentages: a dictionary which contains the percentage of numbers from 1-9 of every beginning characters of an item on the previous number list. 
  Returns: 
    A bool to determine if that dictionary follow's Benford's Law.   
  """
  test_dict = {1: 30, 2: 17, 3: 12, 4: 9, 5: 7, 6: 6, 7: 5, 8: 5, 9: 4}
  #iterate over key and value in the dictionary
  for k,v in percentages.items():
    # check if the value is in the elgible range. 
    if v < (test_dict[k] - 5) or v > (test_dict[k] + 10): 
      return False
  return True 
    
  
