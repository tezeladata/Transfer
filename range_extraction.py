# Range Extraction - 4kyu
def solution(args):
    if not args:
        return []

    res = []
    start = args[0]
    end = args[0]

    for i in range(1, len(args)):
        if args[i] == end + 1: end = args[i]
        elif args[i] == end - 1: end = args[i]
        else:
            if start == end: res.append(str(start))
            elif end == start + 1: res.append(f"{start},{end}")
            else: res.append(f"{start}-{end}")
            start = end = args[i]

    if start == end: res.append(str(start))
    elif end == start + 1: res.append(f"{start},{end}")
    else: res.append(f"{start}-{end}")

    return ",".join(res)