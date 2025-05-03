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

# Climbing stairs
class Solution(object):
    def climbStairs(self, n):
        if n <= 2: return n

        first, second = 1, 2
        for _ in range(3, n+1):
            third = first + second
            first = second
            second = third
        
        return second

# Power of two
class Solution(object):
    def isPowerOfTwo(self, n):
        if n < 0: return False
        
        for i in range(int(n**0.5)+2):
            if 2**i == n: return True
        return False
    
# Valid anagram
class Solution(object):
    def isAnagram(self, s, t):
        def dictize(st): return sorted([[i, st.count(i)] for i in set(st)])

        return dictize(s) == dictize(t)
    
# Add digits
class Solution(object):
    def addDigits(self, num):
        def change(num): return sum([int(i) for i in str(num)])

        while len(str(num)) > 1: num = change(num)

        return num

# Ugly number
class Solution(object):
    def isUgly(self, n):
        if n <= 0:
            return False
        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p
        return n == 1
    
# Missing number
class Solution(object):
    def missingNumber(self, nums):
        res = [i for i in range(max(nums)) if i not in nums]

        if len(res) == 0: return max(nums)+1
        return res[0]

# Move zeroes
class Solution(object):
    def moveZeroes(self, nums):
        insert_pos = 0
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1
        for i in range(insert_pos, len(nums)):
            nums[i] = 0

# Power of three
class Solution(object):
    def isPowerOfThree(self, n):
        if n < 0: return False
        
        for i in range(int(n**0.3)+2):
            if 3**i == n: return True
        return False

# Counting bits
class Solution(object):
    def countBits(self, n):
        return [bin(i)[2:].count("1") for i in range(n+1)]

# Reverse string
class Solution(object):
    def reverseString(self, s):
        new_ls = s[::-1]

        for i in range(len(s)): s[i] = new_ls[i]

# Reverse vowels of string
class Solution(object):
    def reverseVowels(self, s):
        vows = "aeiouAEIOU"
        new_ls, all_vows = [], []

        for i in s:
            if i not in vows: new_ls.append(i)
            else: 
                new_ls.append("_")
                all_vows.append(i)
        
        all_vows = all_vows[::-1]

        for i in range(len(new_ls)):
            if new_ls[i] == "_":
                new_ls[i] = all_vows[0]
                all_vows = all_vows[1:]
        
        return "".join(new_ls)

# Intersection of two arrays
class Solution(object):
    def intersection(self, nums1, nums2):
        return [i for i in set(nums1) if i in nums2]

# Intersection of two arrays II
class Solution(object):
    def intersect(self, nums1, nums2):
        new_ls = [i for i in set(nums1) if i in nums2]
        res = [[x, min(nums1.count(x), nums2.count(x))] for x in new_ls]
        fin = []

        for i in res:
            for _ in range(i[1]):
                fin.append(i[0])

        return fin

# Valid perfect square
class Solution(object):
    def isPerfectSquare(self, num):
        return int(num**0.5)*int(num**0.5) == num

# First unique character in a string
class Solution(object):
    def firstUniqChar(self, s):
        count = {}
        
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        
        return -1

# Find the difference
class Solution(object):
    def findTheDifference(self, s, t):
        count = {}
        
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        for char in t:
            if char not in count or count[char] == 0:
                return char
            count[char] -= 1