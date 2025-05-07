# Power of four
class Solution(object):
    def isPowerOfFour(self, n):
        if n < 0: return False
        if n==1 or n==4: return True

        for i in range(int(n**0.4)):
            if 4**i == float(n): return True
        return False

# Find all numbers dissapeared in array
class Solution(object):
    def findDisappearedNumbers(self, nums):
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

# Arranging coins
import math

class Solution(object):
    def arrangeCoins(self, n):
        return int((math.sqrt(1 + 8 * n) - 1) // 2)

# Repeated substring pattern
class Solution(object):
    def repeatedSubstringPattern(self, s):
        for i in range(1, len(s)//2+1):
            if s[:i]*(len(s) // len(s[:i])) == s: return True
        
        return False

# Hamming distance
class Solution(object):
    def hammingDistance(self, x, y):
        return bin(x ^ y).count('1')

# Number complement
class Solution(object):
    def findComplement(self, num):
        num1 = bin(num)[2:]
        res = ""

        for i in num1:
            if i == "0": res += "1"
            else: res += "0"
        
        return int(res, 2)

# License key formatting
class Solution(object):
    def licenseKeyFormatting(self, s, k):
        all_chars = "".join(s.split("-"))
        first_len = len(all_chars) - ((len(all_chars) // k) * k)

        if first_len == 0:
            res = ""

            for i in range(0, len(all_chars), k):
                res += all_chars[i:i+k]
                res += "-"
            
            return res[:-1].upper()
        else:
            part1 = all_chars[:first_len]
            rem = all_chars[first_len:]

            res = part1 + "-"

            for i in range(0, len(all_chars) - len(part1), k):
                res += rem[i:i+k]
                res += "-"
            
            return res[:-1].upper()

# Max consecutive ones
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        current = 0

        for num in nums:
            if num == 1:
                current += 1
                max_count = max(max_count, current)
            else:
                current = 0

        return max_count

# Construct the rectangle
class Solution(object):
    def constructRectangle(self, area):
        start = int(area ** 0.5)
        while area % start != 0:
            start -= 1
        return [area // start, start]

# Fibonacci number
class Solution(object):
    def fib(self, n):
        if n==0: return 0

        res = [0,1]
        while len(res) < n+1: res.append(res[-2]+res[-1])
        return res[-1]