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

# String matching in an array
class Solution(object):
    def stringMatching(self, words):
        res = []

        for i in range(len(words)):
            word = words[i]
            rem = words[:i] + words[i+1:]

            for x in rem:
                if word in x: res.append(word)
        
        return list(set(res))

# Maximum score after splitting a string
class Solution(object):
    def maxScore(self, s):
        res = -1

        for i in range(1, len(s)):
            new_score = s[:i].count("0") + s[i:].count("1")
            if new_score > res: res = new_score
        
        return res

# Destination city
class Solution(object):
    def destCity(self, paths):
        start_cities = set()

        for path in paths: start_cities.add(path[0])

        for path in paths:
            if path[1] not in start_cities:
                return path[1]

# Check if word occurs as a prefix of any word in a sentence
class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        res = [i for i in range(len(sentence.split(" "))) if sentence.split(" ")[i][:len(searchWord)]==searchWord]
        return res[0]+1 if res else -1

# Shuffle string
class Solution(object):
    def restoreString(self, s, indices):
        res = ["_" for _ in range(len(indices))]
        for i in range(len(indices)):
            res[indices[i]] = s[i]
        
        return "".join(res)

# Make the string great
class Solution(object):
    def makeGood(self, s):
        def is_good(st):
            for i in range(len(st)-1):
                if (st[i].islower() and st[i+1].isupper() and st[i].upper() == st[i+1]) or (st[i].isupper() and st[i+1].islower() and st[i].lower() == st[i+1]):
                    return st[:i]+st[i+2:]
            return True
        
        while is_good(s)!=True:
            s=is_good(s)
        
        return s

# Crawler log folder
class Solution(object):
    def minOperations(self, logs):
        depth = 0
        for i in logs:
            if i.split("/")[0] not in "..":
                depth += 1
            if i.split("/")[0] == ".." and depth != 0:
                depth -= 1
        
        return depth if depth >= 0 else 0

# Maximum nesting depth of parentheses
class Solution(object):
    def maxDepth(self, s):
        depths = []
        cur_depth = 0

        for i in s:
            if i == "(":
                cur_depth += 1
                depths.append(cur_depth)
            elif i == ")":
                cur_depth -= 1
                depths.append(cur_depth)
        
        return max(depths) if depths else 0

# Check if two strings are equivalent
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        return "".join(word1)=="".join(word2)