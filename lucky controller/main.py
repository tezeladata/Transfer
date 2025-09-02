import random
import time

names = [
    "ანდრია ბერიკაშვილი (game dev)",
    "გიორგი მახარაშვილი",
    "ზუკა ტუღრიაშვილი",
    "ლუკა სუარიშვილი",
    "ლუკა ტატუაშვილი",
    "შიო ელიკაშვილი",
    "დაჩი ალანია",
    "ანდრია კობახიძე",
    "გიო აბუაშვილი"
]

lucky_controllers = []
def get_cont(ls):
    new_cont = random.choice(ls)
    ls.remove(new_cont)

    lucky_controllers.append(new_cont)

for _ in range(5):
    time.sleep(10)
    get_cont(names)
    print(f"\n{"-"*(len(lucky_controllers[-1])+16)}\n\nNew controller: {lucky_controllers[-1]}\n\n{"-"*(len(lucky_controllers[-1])+16)}\n")