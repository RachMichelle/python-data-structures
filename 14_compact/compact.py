def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    # compact_list = []
    # for val in lst: 
    #     if val: 
    #         compact_list.append(val)
    # return compact_list

    return [val for val in lst if val]