""" 
Ben Phan
CSC110
Project -6
This program has 7 functions as part of running a game. I will only work on 4 functions in this project: load_game, load_objects, load_travel_table, and print_instructions.
"""

def load_game():
    """
This function load the game by iterates over a file in read mode. It returns a dictionary including an integer as a key and a list of values. 
Args: 
    None
Returns:
    A dictionary with the first item in the line as an integer key and the second items as a list value. 
  """
    game_file = open("game.txt", "r")
    game = {}
    for line in game_file:
      word = line.strip().split("\t")
       #first object is set to be an integer and the key
      key = int(word[0])
      #second objects are set to be the value
      value = word[1]
      #check if there is already a key in game
      if key in game:
      #add the value to the existed key
        game[key].append(value)
      #if the key is not in game
      else:
      #create a new pair of key and value
        game[key] = [value]
    game_file.close()
    return game

def load_objects():
    """
This function load the objects by iterates over a file in read mode. It returns a dictionary including a tupple key and a list of values. 
Args: 
    None
Returns:
    A dictionary with the first 2 itegers items and the third item in the line inside a tupple as a key and the fourth items onward as a list value. 
  """
    object_file = open("objects.txt", "r")
    objects = {}
    for line in object_file:
      word = line.strip().split("\t")
      #creating a tuple key using the first 3 items
      key = (int(word[0]),int(word[1]),word[2])
      #values are items 4 onward 
      objects[key]=word[3:]
    object_file.close()
    return objects

def load_travel_table():
    """
This function load the objects by iterates over a file in read mode. It returns a dictionary including a tupple key and a string value. 
Args: 
    None
Returns:
    A dictionary with the first 2 itegers items in the line inside a tupple as a key and the third item as a value. 
"""
    travel_file = open("travel_table.txt", "r")
    travel_table = {}
    for line in travel_file:
      word = line.strip().split("\t")
      # set key as a tuple with 2 integer as a first and second items in the line
      key = (int(word[0]),int(word[1]))
      #value is the third item
      value = word[2]
      travel_table[key]=value
    travel_file.close()
    return travel_table

def print_instructions():
    """
This function print the instruction. It takes no arguement and print out the content of the instruction file. 
Args: 
    None
Returns:
    Strings that represents the content of the file.
  """
    f = open("instructions.txt", "r")
    print (f.read())
    f.close()

def get_location(location, game, objects, player_objects):
    '''
    This function gets the next location from the game data.
    It doesn't return anything, it prints messages related to
    objects (if the user has them or not) and location information
    Args:
        location: integer
        game: dictionary with location and string information
        objects: dictionary of location, binary (0 or 1), and object name
        player_objects: list of strings
    Returns:
        None
    '''
    # for each string associated with that location in the game
    # dictionary, print that line
    for line in game[location]:
        print(line)

    # check if location has an object associated with it
    for key, value in objects.items():
        # if there's an object associated with this location
        # and the possible action is to take it (0)
        # and user hasn't taken it yet, print message associate with
        # object
        if key[0] == location and key[1] == 0 and key[2] not in player_objects:
            print(value[0])

        # if there's an object associated with this location
        # and we need to check if the user has it (1)
        if key[0] == location and key[1] == 1:
            if key[2] in player_objects:
                # user has the object
                print(value[1])
            else:
                # user does not have the object
                print(value[0])


def go_to_location(location, travel_table, objects, player_objects, answer):
    '''
    This function checks for the user's input (their answer), the objects
    that are available for the users to take, and the objects the user
    has in their object list
    Args:
        location: integer
        travel_table: dictionary with current location, possible to go
                      location and verb that takes user to to go location
        objects: dictionary of location, binary (0 or 1), and object name
        player_objects: list of strings
        answer: input from the user (string)
    Returns:
        next location (integer)
    '''
    # check if user wants to take an object
    if "take" in answer.lower():
        for key in objects:
            # check if there's an object to take
            if key[0] == location and key[1] == 0:
                # add object to user's object list
                player_objects.append(key[2])

    # check if the user needs to have an object to proceed
    for key in objects:
        # if there's a needed object for this location
        # but the user does not have it, return current location 
        # meaning the user doesn't go anywhere
        if key[0] == location and key[1] == 1 and key[2] not in player_objects:
            return location

    # no objects to take or needed to go anywhere
    # check where to go based on user's answer
    for x_y, verb in travel_table.items():
        if x_y[0] == location and verb in answer.upper():
            return x_y[1]


def play_game():
    '''
    This function is the main game playing function.
    It loads all text files for the game, and asks
    for the player's input
    '''
    # load game.txt
    game = load_game()
    # load objects.txt
    objects = load_objects()
    # load travel_table.txt
    travel_table = load_travel_table()
    # player starts with no objects
    player_objects = []
    # player starts at location 0
    location = 0
    # get info for location 0
    get_location(location, game, objects, player_objects)
    # ask if player wants instructions
    answer = input("> ")
    if "y" in answer.lower():
        print_instructions()
    # go to location 1 (start game for real)
    location += 1
    # this is just a demo with 11 locations
    while location < 12:
        # print info on current location
        get_location(location, game, objects, player_objects)
        # request player input
        answer = input("> ")
        # extra line break
        print()
        # player can exit at any time by inputting "exit"
        if "exit" not in answer.lower():
            # player doesn't want to exit
            # get next location based on player's input
            where_to_go = go_to_location(location, travel_table, objects, 
                                      player_objects, answer)
            # if a possible location was found
            if where_to_go:
                # change location
                location = where_to_go
        else: # user entered "exit"
            location = 12
    print("This is the end of this game demo.")