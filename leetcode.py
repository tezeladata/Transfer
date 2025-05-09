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

# Base 7
class Solution(object):
    def convertToBase7(self, num):
        if num >= -6 and num <= 6: return str(num)

        is_neg = num < 0
        num = num*-1 if is_neg else num

        res = [num % 7]
        num = num // 7

        while num // 7 != 0:
            res.append(num%7)
            num //= 7
        res.append(num%7)

        res = "".join(str(i) for i in res[::-1])
        return "-{}".format(res) if is_neg else res

# Perfect number
class Solution(object):
    def checkPerfectNumber(self, n):
        if n <= 0: return []
        divisors = [1]
        for div in range(1, int(n ** 0.5 + 1)):
            if n % div == 0: divisors.extend([n // div, div])
        if n in divisors: divisors = [i for i in divisors if i!=n]
        return sum(list(set(divisors))) == n

# Detect capital
class Solution(object):
    def detectCapitalUse(self, word):
        return word.isupper() or word.islower() or word == word.capitalize()

# Reverse string II
class Solution(object):
    def reverseStr(self, s, k):
        if k > len(s): return s[::-1]
        else:
            res = ""
            for i in range(0, len(s), k*2):
                res += s[i:i+k][::-1] + s[i+k:i+2*k]
            
            return res

# Array partition
class Solution(object):
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])

# Distribute candies
class Solution(object):
    def distributeCandies(self, candyType):
        all_types = len(set(candyType))
        max_eat = len(candyType) // 2

        return max_eat if max_eat == all_types or max_eat < all_types else all_types

# Longest harmonious subsequence
class Solution(object):
    def findLHS(self, nums):
        nums.sort()
        res = 0
        start = 0
        
        for i in range(len(nums)):
            while nums[i] - nums[start] > 1:
                start += 1
            if nums[i] - nums[start] == 1:
                res = max(res, i - start + 1)
        
        return res

# Minimum index sum of two lists
class Solution(object):
    def findRestaurant(self, list1, list2):
        all_pairs = []

        for i in range(len(list1)):
            for x in range(len(list2)):
                if list1[i] == list2[x]: 
                    all_pairs.append([list1[i], i+x])
        
        all_pairs.sort(key=lambda x: x[1])
        all_pairs = [i for i in all_pairs if i[1] == all_pairs[0][1]]
        return [i[0] for i in all_pairs]

# Maximum product of three numbers
class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])