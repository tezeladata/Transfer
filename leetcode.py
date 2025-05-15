# Longest substring without repeating characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len

# Longest palindromic substring
class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            for x in range(i+1, len(s)+1):
                n = s[i:x]
                if n == n[::-1] and len(n) > len(res): res = n
        
        return res
    
# Reverse integer
class Solution(object):
    def reverse(self, x):
        n = int(str(x)[::-1]) if x >= 0 else int("-" + (str(x)[1:])[::-1])
        return 0 if n < -2**31 or n > 2**31 - 1 else n

# Container with most water
class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        res = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            res = max(res, h * w)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res

# Letter combinations of a phone number
class Solution(object):
    def letterCombinations(self, digits):
        if digits == "": return []

        corres = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]
        res = []

        if len(digits) == 1: return corres[int(digits)-2]
        elif len(digits) == 2:
            first = corres[int(digits[0])-2]
            second = corres[int(digits[1])-2]
            for i in first:
                for x in second:
                    res.append(i+x)
            return res
        elif len(digits) == 3:
            first = corres[int(digits[0])-2]
            second = corres[int(digits[1])-2]
            third = corres[int(digits[2])-2]
            for i in first:
                for x in second:
                    for z in third:
                        res.append(i+x+z)
            return res
        elif len(digits) == 4:
            first = corres[int(digits[0])-2]
            second = corres[int(digits[1])-2]
            third = corres[int(digits[2])-2]
            fourth = corres[int(digits[3])-2]
            for i in first:
                for x in second:
                    for z in third:
                        for y in fourth:
                            res.append(i+x+z+y)
            return res

# Divide two integers
class Solution(object):
    def divide(self, dividend, divisor):
        if dividend == -2**31 and divisor == -1:  return 2**31 - 1

        neg = (dividend < 0) != (divisor < 0)

        dividend, divisor = abs(dividend), abs(divisor)
        result = 0

        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            result += multiple

        return -result if neg else result

# Search in rotated sorted array
class Solution(object):
    def search(self, nums, target):
        return nums.index(target) if target in nums else -1

# Find first and last position of element in sorted array
class Solution(object):
    def searchRange(self, nums, target):
        res = [i for i in range(len(nums)) if nums[i] == target]
        
        if res == []: return [-1, -1]
        elif len(res) == 1: return [res[0], res[0]]
        elif len(res) > 2: return [res[0], res[-1]]
        return res

# Count and say
class Solution(object):
    def countAndSay(self, n):
        def gen_rle(s):
            res = ""
            count = 1

            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    count += 1
                else:
                    res += "{}{}".format(count, s[i-1])
                    count = 1
            res += "{}{}".format(count, s[-1])
            return res

        res = "1"
        for _ in range(n-1): res = gen_rle(res)
        return res

# Multiply strings
class Solution(object):
    def multiply(self, num1, num2):
        return str(int(num1)*int(num2))

# Permutations
class Solution(object):
    def permute(self, nums):
        if len(nums) == 0:
            return [[]]

        perms = []
        for i in range(len(nums)):
            rest = nums[:i] + nums[i+1:] 
            for p in self.permute(rest): perms.append([nums[i]] + p)
        return perms

# Group anagrams
class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())

# Pow(x, n)
class Solution(object):
    def myPow(self, x, n):
        return x**n

# Merge intervals
class Solution(object):
    def merge(self, intervals):
        if not intervals: return []

        intervals.sort(key=lambda x: x[0])
        res = []
        last = intervals[0]

        for i in range(1, len(intervals)):
            if last[1] >= intervals[i][0]: 
                last = [last[0], max(last[1], intervals[i][1])]
            else:
                res.append(last)
                last = intervals[i]

        res.append(last) 
        return res