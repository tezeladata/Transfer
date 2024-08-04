# Pirates!! Are the Cannons ready!??
def cannons_ready(gunners):
    for i in gunners.values():
        if i.lower() == "nay": return 'Shiver me timbers!'
    return "Fire!"

# Is your period late?
from datetime import *
def period_is_late(last,today,cycle_length):
    return last + timedelta(days = cycle_length) < today

# 8kyu interpreters: HQ9+
def HQ9(code):
    if code == "H":
        return "Hello World!"
    if code == "Q":
        return "Q"
    if code == "9":
        result = ""
        for n in range(99,2,-1):
            result += f"{n} bottles of beer on the wall, {n} bottles of beer.\nTake one down and pass it around, {n-1} bottles of beer on the wall.\n"
        result += "2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall."
        return result
    return None

# UEFA EURO 2016
def uefa_euro_2016(teams, scores):
    if scores[0] > scores[1]: return f"At match {teams[0]} - {teams[1]}, {teams[0]} won!"
    elif scores[1] > scores[0]: return f"At match {teams[0]} - {teams[1]}, {teams[1]} won!"
    return f"At match {teams[0]} - {teams[1]}, teams played draw."

# Classy Extentions
from preloaded import Animal

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."
    
# Barking mad
class Dog ():
    def __init__(self, breed):
        self.breed = breed
    
    def bark(self):
        return "Woof"
    

snoopy = Dog("Beagle")

snoopy.bark = lambda: "Woof"

scoobydoo = Dog("Great Dane")

# They say that only the name is long enough to attract attention. They also said that only a simple Kata will have someone to solve it. This is a sadly story #1: Are they opposite?
def is_opposite(s1,s2):
    return "".join([i.swapcase() for i in s1]) == s2 if s1 else False

# Is the date today
from datetime import datetime

def is_today(date: datetime) -> bool:
    return date.date() == datetime.today().date()

# Training JS #18: Methods of String object--concat() split() and its good friend join()
def split_and_merge(string, sp):
    return ' '.join(sp.join(word) for word in string.split())

# Ensure question
def ensure_question(s):
    if not s: return "?"
    return s+"?" if s[-1]!="?" else s

# pick a set of first elements
def first(*args):
    if len(args) == 2: 
        seq, n = args[0], args[1]
        
        if n==0: return []
        return seq[:n] if len(seq) > n else seq
    return [args[0][0]]

# For Twins: 2. Math operations
def ice_brick_volume(radius, bottle_length, rim_length):
    height = bottle_length - rim_length
    side = 2 * radius
    volume = side * side * height
    
    return volume/2

# Find the Slope
def find_slope(points):
    a, b, c, d = points
    
    if c - a == 0:
        return "undefined"
    
    slope = (d - b) // (c - a)
    return str(int(slope))

# Fix the Bugs (Syntax) - My First Kata
def my_first_kata(a,b):
    if type(a) != int or type(b) != int: return False
    else:
        return a % b + b % a
    
# NBA full 48 minutes average
def nba_extrap(ppg, mpg):
    return round(ppg * (48 / mpg), 1)

# easy logs
import math

def logs(x, a, b):
    return (math.log(a) + math.log(b))/math.log(x);

# Fuel Calculator: Total Cost
def fuel_price(litres, price_per_litre):
    return round(litres * (price_per_litre - min(25, (litres // 2) * 5) / 100), 2)

# Online RPG: player to qualifying stage?
def playerRankUp(pts):
     return "Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up." if pts >= 100 else False

# Points of Reflection
def symmetric_point(p, q):
    return [2 * q[0] - p[0], 2 * q[1] - p[1]]

# Freudian translator
def to_freud(sentence):
    return "" if not sentence or sentence == " " else " ".join(["gender" for _ in range(len(sentence.split(" ")))])

# Grasshopper - Terminal Game #1
class Hero(object):
    def __init__(*args):
        self = args[0]
        if (len(args))==2: self.name = args[1]
        else: self.name = "Hero"
        self.position = "00"
        self.health = 100
        self.damage = 5
        self.experience = 0

# Finish Guess the Number Game
# class Guesser:
#     def __init__(self, number, lives):
#         self.number = number
#         self.lives = lives

#     def guess(self,n):
#         if self.lives == 0:
#             raise Except('Omae wa mo shindeiru')
#         elif n  == self.number:
#             return True
#         self.lives -= 1
#         return False

# Merging sorted integer arrays (without duplicates)
def merge_arrays(first, second): 
    return list(sorted(list(set(first+second))))

# Return Two Highest Values in List
def two_highest(arg1):
    if len(arg1) >= 3: return [list(sorted(list(set(arg1))))[-1], list(sorted(list(set(arg1))))[-2]]
    return [max(arg1)] if arg1 else []
    