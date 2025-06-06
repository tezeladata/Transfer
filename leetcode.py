# Goat latin
class Solution(object):
    def toGoatLatin(self, sentence):
        vowels = "aeiouAEIOU"
        res = []

        for i in range(len(sentence.split(" "))):
            word = sentence.split(" ")[i]

            if word[0] in vowels:
                word = word + "ma"
            else:
                word = word[1:]+word[0]+"ma"
            
            word += "a"*(i+1)
            res.append(word)
        
        return " ".join(res)

# Uncommon words from two sentences
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        s1, s2 = s1.split(" "), s2.split(" ")
        return [i for i in s1 if s1.count(i)==1 and i not in s2] + [i for i in s2 if s2.count(i)==1 and i not in s1]

# Reverse only letters
class Solution(object):
    def reverseOnlyLetters(self, s):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        start = ""
        letters = ""

        for i in s:
            if i.lower() not in alphabet:
                start += i
            else:
                start += " "
                letters += i
        
        letters = letters[::-1]
        res = ""

        for i in start:
            if i!=" ": res += i
            else:
                if letters:
                    res += letters[0]
                    letters = letters[1:]
        
        return res

# DI string match
class Solution(object):
    def diStringMatch(self, s):
        low, high = 0, len(s)
        perm = []
        
        for char in s:
            if char == 'I':
                perm.append(low)
                low += 1
            else: 
                perm.append(high)
                high -= 1
        
        perm.append(low)
        return perm

# Occurences after bigram
class Solution(object):
    def findOcurrences(self, text, first, second):
        text = text.split(" ")
        firsts = [i for i in range(len(text)) if text[i] == first]
        res = []

        for i in firsts:
            if i+2<=len(text) and text[i+1]==second:
                try: res.append(text[i+2])
                except: continue
        
        return res

# Defanging an IP address
class Solution(object):
    def defangIPaddr(self, address):
        return address.replace(".", "[.]")

# Split a string in balanced strings
class Solution(object):
    def balancedStringSplit(self, s):
        balance = 0
        count = 0
        
        for char in s:
            if char == 'R':
                balance += 1
            else:
                balance -= 1
                
            if balance == 0:
                count += 1
                
        return count