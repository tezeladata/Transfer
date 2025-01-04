# endswith(string, ending string, start, end)
def endswith(*args):
    if not isinstance(list(args)[0], str) or not isinstance(list(args)[0], str): raise TypeError("First and second arguments should be string")
    if not args or len(list(args)) not in [1, 2, 3, 4]: raise TypeError(f"Endswith takes exactly one, two, three or four arguments ({len(list(args))} given)")

    main, ending_str = list(args)[0], list(args)[1]
    start_ind = list(args)[2] if len(list(args)) >= 3 else None
    end_ind = list(args)[3] if len(list(args)) == 4 else None

    if start_ind is not None: main = main[start_ind:]
    if end_ind is not None: main = main[:end_ind]

    return main[-1*len(ending_str):] == ending_str