"""
   CISC-121 2023W

   Name:   Kylie Hubbard
   Student Number: 20294570
   Email:  21kah10@queensu.ca
   Date: 2023-02-01

   I confirm that this assignment solution is my own work and conforms to
   Queen's standards of Academic Integrity
"""

friend_dictionary = {}

def friends_to_dictionary():
    """
    -------------------------------------------------------
    Use: For a function that turns a text file into a
    dictionary.
    -------------------------------------------------------
    Parameters:
        None
    Returns:
        A new dictionary.
    -------------------------------------------------------
    """
    with open("friendship.txt") as file:
        for line in file:
            (key, value) = line.split()
            friend_dictionary[str(key)] = value
        return (friend_dictionary)
friends_to_dictionary()


def all_my_friends(friend):
    """
    -------------------------------------------------------
    Use: For a function that takes an element from a
    dictionary and displays the keys and values equivalent.
    -------------------------------------------------------
    Parameters:
        friend - Takes the input of a variable on the
        dictionary
    Returns:
        A new list of the keys/values equivalent.
    -------------------------------------------------------
    """
    friend_list = []
    for key, value in friend_dictionary.items():
        if friend == value:
            friend_list.append(key)
        if friend == key:
            friend_list.append(value)
    return friend_list

def friendship_degree(dictionary):
    """
    -------------------------------------------------------
    Use: For a function that displays the keys and their
    corresponding friends and amount of friends.
    -------------------------------------------------------
    Parameters:
        dictionary - Takes the input of a dictionary
    Returns:
        All the friends a variable has and the amount
    -------------------------------------------------------
    """
    for key, value in dictionary.items():
        name = key
        friendsOfName = all_my_friends(name)
        numfriends= len(friendsOfName)
        print(name, "has", numfriends, "friends:", friendsOfName)
friendship_degree(friend_dictionary)
