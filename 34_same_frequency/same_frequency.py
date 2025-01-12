def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    lst1 = list(str(num1))
    lst2 = list(str(num2))

    lst1.sort()
    lst2.sort()

    # print(lst1, lst2)
    if lst1 == lst2:
        return True
    else: 
        return False