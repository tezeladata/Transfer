# Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for x in range(i+1, len(nums)):
                if nums[i] + nums[x] == target: return [i, x]

# Palindrome number
class Solution(object):
    def isPalindrome(self, x):
        return str(x)[::-1] == str(x)
    
# Longest common prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        min_len = min(len(s) for s in strs)
        res = ""

        for i in range(min_len):
            char = strs[0][i]
            if all(s[i] == char for s in strs):
                res += char
            else:
                break

        return res
    
# Find the index of the first occurence in a string
class Solution(object):
    def strStr(self, haystack, needle):
        if haystack == needle: return 0

        for i in range(0, len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle: return i
        return 0 if len(haystack) == len(needle) and len(haystack) == 1 else -1
    
# Length of the last word
class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.strip().split(" ")[-1])
    
# Plus one
class Solution(object):
    def plusOne(self, digits):
        return [int(i) for i in str(int("".join([str(i) for i in digits]))+1)]
    
# Add binary
class Solution(object):
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]
    
# Sqrt(x)
class Solution(object):
    def mySqrt(self, x):
        if x == 0: return 0

        res = [1]
        while (res[-1] * res[-1]) <= x: res.append(res[-1]+1)
        return res[-2] if len(res) >= 2 else res[-1]
    
# Pascal's triangle
class Solution(object):
    def generate(self, n):
        a = []

        for i in range(n):
            a.append([])
            a[i].append(1)
            for j in range(1, i):
                a[i].append(a[i-1][j-1] + a[i-1][j])
            if n != 0:
                a[i].append(1)
        
        a[0] = [1]
        return a

# Valid palindrome
class Solution(object):
    def isPalindrome(self, s):
        return "".join([i for i in s.lower() if i.isalnum()]) == "".join([i for i in s.lower() if i.isalnum()])[::-1]
    
# Single number
class Solution(object):
    def singleNumber(self, nums):
        return [i for i in nums if nums.count(i) == 1][0]
    
# Majority element
class Solution(object):
    def majorityElement(self, nums):
        return sorted([[i, nums.count(i)] for i in set(nums)], key=lambda x: x[1], reverse = True)[0][0]
    
# Valid parentheses
class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False
        return not stack
    
# Search insert position
class Solution(object):
    def searchInsert(self, nums, target):
        return nums.index(target) if target in nums else len([i for i in nums if i < target])
    
# Best time to buy and sell stock
class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
    
# Happy number
class Solution(object):
    def isHappy(self, n):
        def change(num): return sum([int(i)**2 for i in str(num)])

        for i in range(20):
            if n == 1: return True
            else:
                n = change(n)
        
        return False
    
# Isomorphic strings
class Solution(object):
    def isIsomorphic(self, s, t):
        mapping_s_t = {}
        mapping_t_s = {}

        for char_s, char_t in zip(s, t):
            if (char_s in mapping_s_t and mapping_s_t[char_s] != char_t) or \
               (char_t in mapping_t_s and mapping_t_s[char_t] != char_s):
                return False
            mapping_s_t[char_s] = char_t
            mapping_t_s[char_t] = char_s

        return True

# Contains duplicate
class Solution(object):
    def containsDuplicate(self, nums):
        return len(set(nums)) < len(nums)