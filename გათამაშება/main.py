import random
import time

# For cool design
def generate_line(alphabet, size, i):
    first_half = '-'.join(alphabet[size-1:abs(i):-1])  # First half of the line
    second_half = '-'.join(alphabet[abs(i):size])     # Second half of the line
    return first_half + second_half                  # Combine both halves

def print_rangoli(size, name):
    alphabet = name.split(" ")[0]

    for i in range(size-1, -size, -1):
        line = generate_line(alphabet, size, i)
        center_length = size*4 - 3  # Length to center the line
        print(line.center(center_length, '-'))
    
    return " "


participants = [
    "Zuka Abashidze",
    "Data Diasamidze",
    "Nikoloz Tchitadze",
    "Sandro Zabakhidze",
    "Andria Alavidze",
    "Tsotne Gujabidze",
    "Vano Motiashvili",
    "Ilia Dzindzibadze",
    "Giorgi Gvritishvili",
    "Guram Vakhtangashvili",
    "Ucha Khuberishvili",
    "Giorgi Varazashvili",
    "Luka Lortqifanidze", 
    "Guram Papunashvili",
    "Luka Gurgenidze",
    "Atuka Xusikviadze",
    "Andria Svanize",
    "Erekle Kilasonia",
    "nikoloz kimeridze",
    "Berdia Bekauri"
]

def check_valid(arr):
    return [arr.count(i) == 1 for i in arr].count(True) == len(arr)
print("There are no duplicates\n" if check_valid(participants) == True else "There are duplicates\n")

def counter():
    start = 10
    for i in range(10):
        print(start)
        start -= 1
        time.sleep(1)
    
# Main logic
prize_sum, winners = len(participants) * 5, []
for _ in range(3):
    counter()
    win = random.choice(participants)
    message = f"\nWinner is: {win}!!!\n"
    
    print("-"*len(message))
    print(message)
    print(f"\n{print_rangoli(len(win.split(" ")[0]), win)}")
    print("-"*len(message))

    participants.remove(win)
    winners.append(win)
    time.sleep(5)

print(winners)


# End
print(f"\n\nPrizes:\n{winners[0]}: {prize_sum/2} Gel!!\n{winners[1]}: {prize_sum*.3} Gel!!\n{winners[2]}: {prize_sum*.2} Gel!!")
print_rangoli(len("The End"), "End")