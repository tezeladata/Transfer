# მონაცემების შეტანა
starting_list = []

def sort_users(name, x, y):
    starting_list.append([name, x, y])

sort_users("abashidze", 65, 44)
sort_users("koxreidze", 42, 65)
sort_users("varadashvili", 56, 26)
sort_users("xucishvili", 60, 26)
sort_users("yifshidze", 38, 24)
sort_users("gio xaniashvili", 29, 70)
sort_users("svanidze", 77, 51)
sort_users("girgvliani", 56,41)
sort_users("akolashvili", 32,21)
sort_users("mardaleishvili", 34,30)
sort_users("gabriel xaniashvili", 31,100)
sort_users("maisuradze", 58,31)
sort_users("wawiashvili", 50, 64)
sort_users("dolidze", 78,42)
sort_users("burchuladze", 36, 16)
sort_users("asanashvili", 70, 41)
sort_users("samushia", 63, 40)
sort_users("basharuli", 43, 41)
sort_users("wibliashvili", 53, 21)
sort_users("gociridze", 50, 57)
sort_users("kobakhidze", 63, 37)
sort_users("jojua", 45, 30)
sort_users("dzukaevi", 49, 32)
sort_users("khuberishvili", 60, 30)
sort_users("wereteli", 69, 43)
sort_users("janezashvili", 38, 0)
sort_users("kobaxidze", 43, 84)
sort_users("goachad", 90, 40)
sort_users("nikoloz kobakhidze", 60, 33)
sort_users("akaki dolidze", 59, 13)
sort_users("bregvadze", 70, 0)
sort_users("gagoshidze", 46, 30)
sort_users("kotrikadze", 65, 32)
sort_users("izoria", 50, 10)
sort_users("dvali", 35, 0)
sort_users("nutsubidze", 55, 0)
sort_users("tezela", 68, 50)
sort_users("diasamidze", 65, 41)
sort_users("shubitidze", 65 ,18)
sort_users("motiasvhili", 93, 28)
sort_users("molodini", 60, 40)
sort_users("janeza", 95, 25)


# მახასიათებლის გამოთვლა
sorted_list = []
def sort_data(list):
    sorted_list.append([list[0], (list[2] * list[1] / 20)])

for i in range(len(starting_list)):
    sort_data(starting_list[i])


# სიის დასორტირება
sorted_list.sort(key=lambda x: x[1], reverse=True)


# dict-ის სახით დაბეჭვდა
user_dict = dict()

for list in sorted_list:
    user_dict[list[0]] = list[1]

print(user_dict)