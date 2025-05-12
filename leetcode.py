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