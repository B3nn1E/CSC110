def combine (list_1, list_2):
  for index in range (len (list_2)):
    characters = list_2 [index]
    list_1.append (characters)


test_list = []
combine(test_list, []) 
print(test_list) # []

test_list = [1, 2, 3]
combine(test_list, [1, 1]) 
print(test_list) # [1, 2, 3, 1, 1]

test_list = [1, 2, 3, 1, 5]
combine(test_list, [])
print(test_list) # [1, 2, 3, 1, 5]

