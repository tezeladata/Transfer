# count(string, value, start, end)
def count(*args):
    if not isinstance(list(args)[0], str) or not isinstance(list(args)[1], str): raise TypeError("Both main argument and to_find argument should be strings.")
    if not args or len(list(args)) not in [2, 3, 4]: raise TypeError(f"Count takes exactly two, three, or four arguments ({len(list(args))} given)")

    main, to_find = list(args)[0], list(args)[1]
    start_ind = list(args)[2] if len(list(args)) >= 3 else None
    end_ind = list(args)[3] if len(list(args)) == 4 else None

    res = 0

    if start_ind is not None: main = main[start_ind:]
    if end_ind is not None: main = main[:end_ind]

    for i in range(len(main) - len(to_find)+1):
        found = main[i:i+len(to_find)]
        if found == to_find: res += 1
    
    return res