def all_odd_or_even(list):
    """
    -------------------------------------------------------
    Use: For a function that takes a list as input and 
    evaluates various conditions to return True or False
    -------------------------------------------------------
    Parameters:
        list - a list of variable length with integers
    Returns:
        True, False
    -------------------------------------------------------
    """
    if all(item % 2 == 0 for item in list) and len(list) >= 1: #and type(args)==int:
        return True
    elif all(item % 2 == 1 for item in list) and len(list) >= 1: #and type(args)==int:
        return True
    else:
        return False
