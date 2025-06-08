# Largest substring between two equal characters
class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        if len(s)==len(set(s)): return -1

        res = ""
        for i in range(len(s)):
            for x in range(i+1, len(s)+1):
                sub = s[i:x]
                if sub[0]==sub[-1] and len(sub[1:-1])>len(res): res = sub[1:-1]
        return len(res)

# Goal parser interpretation
class Solution(object):
    def interpret(self, command):
        return command.replace("()", "o").replace("(al)", "al")

# Count the number of consistent strings
class Solution(object):
    def countConsistentStrings(self, allowed, words):
        allowed_set = set(allowed)
        return sum(all(char in allowed_set for char in word) for word in words)

# Determine if string halves are alike
class Solution(object):
    def halvesAreAlike(self, s):
        return len([i for i in s[:len(s)//2] if i.lower() in "aeiou"]) == len([i for i in s[len(s)//2:] if i.lower() in "aeiou"])

# Minimum changes to make alternating binary string
class Solution(object):
    def minOperations(self, s):
        pattern1 = pattern2 = 0
        for i, c in enumerate(s):
            if c != str(i % 2):
                pattern1 += 1
            if c != str((i+1) % 2):
                pattern2 += 1
        return min(pattern1, pattern2)

# Longest nice substring
class Solution(object):
    def longestNiceSubstring(self, s):
        def is_nice(st):
            for i in st:
                if st.count(i.lower())==0 or st.count(i.upper())==0: return False
            return True
        
        res = ""
        for i in range(len(s)):
            for x in range(i+1, len(s)+1):
                sub = s[i:x]
                if is_nice(sub) and len(sub) > len(res): res = sub
        return res

# Merge strings alternately
class Solution(object):
    def mergeAlternately(self, word1, word2):
        if len(word1)>len(word2): word2 = word2 + ("_"*(len(word1)-len(word2)))
        elif len(word2)>len(word1): word1 = word1 + ("_"*(len(word2)-len(word1)))

        
        res = ""

        for i in range(len(word1)):
            res += word1[i]+word2[i]
        return res.replace("_", "")

# Determine color of chessboard square
class Solution(object):
    def squareIsWhite(self, coordinates):
        if coordinates[0] in "aceg" and coordinates[1] in "2468": return True
        elif coordinates[0] in "bdfh" and coordinates[1] in "1357": return True
        return False

# Truncate sentence
class Solution(object):
    def truncateSentence(self, s, k):
        return " ".join(s.split(" ")[:k])

# Check if the sentence is pangram
class Solution(object):
    def checkIfPangram(self, sentence):
        return "".join(list(sorted(set(sentence))))=="abcdefghijklmnopqrstuvwxyz"

# Replace all digits with characters
class Solution(object):
    def replaceDigits(self, s):
        alp = "abcdefghijklmnopqrstuvwxyz"
        res = ""
        for i in range(len(s)):
            if s[i] in alp:
                res += s[i]
            else:
                res += alp[alp.index(s[i-1])+int(s[i])]
        return res

# Sorting the sentence
class Solution(object):
    def sortSentence(self, s):
        res = ["_" for _ in range(len(s.split(" ")))]
        for word in s.split(" "):
            res[int(word[-1])-1]=word[:-1]
        return " ".join(res)