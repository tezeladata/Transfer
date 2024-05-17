def stat(strg):
    if strg == "":
        return ''
    
    data_list = []
    for runner_time in strg.split(", "):
        times = convert_to_seconds([int(time) for time in runner_time.split("|")])
        data_list.append(times)
    data_list.sort()
    
    
    return f"Range: {stat_range(data_list)} Average: {stat_mean(data_list)} Median: {stat_median(data_list)}"


# Funcs for convertions
def convert_to_seconds(time):
    return time[0] * 3600 + time[1] * 60 + time[2]

def convert_to_hms(seconds):
    hours = int(seconds / 3600 // 1)
    minutes = int((seconds - hours * 3600) / 60 // 1)
    seconds = int(seconds - hours * 3600 - minutes * 60)
    
    return f"{hours:02d}|{minutes:02d}|{seconds:02d}"


# Funcs for range, mean, median
def stat_range(data):
    return convert_to_hms(data[-1] - data[0])

def stat_mean(data):
    return convert_to_hms(sum(data) / len(data))
    
def stat_median(data):
    data_length = len(data)
    middle = data_length // 2
    
    if data_length % 2 == 0:
        return convert_to_hms((data[middle - 1] + data[middle]) / 2)
    return convert_to_hms(data[middle])

print(stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"))