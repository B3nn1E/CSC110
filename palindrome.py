def reverse_string (string):
  reverse = ""
  index = len (string) -1 
  while index >= 0:
    reverse = reverse + string [index]
    index =  index -1

  return reverse 

def remove_spaces (string):
  no_space= ""
  index = 0
  while index < len (string): 
    if string [index] == " ":
      no_space = no_space
    else:
      no_space = no_space + string [index]
    index += 1
  return no_space 

def is_palindrome (string): 
  reverse= reverse_string (string)
  remove= remove_spaces (reverse)
  new_world = remove
  if new_world == remove_spaces (string):
    return True
  else: 
    return False 
  
    

