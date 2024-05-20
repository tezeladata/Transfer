# Add Binary
class Solution(object):
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]
    
# Pascal's Triangle
class Solution(object):
    def generate(self, numRows):
        a = []
        for i in range(numRows):
            a.append([])
            a[i].append(1)
            for j in range(1, i):
                a[i].append(a[i-1][j-1] + a[i-1][j])
            if i > 0: 
                a[i].append(1)
        
        return a
    
# Majority Element
class Solution(object):
    def majorityElement(self, nums):
        for i in list(set(nums)):
            if nums.count(i) > len(nums) * 0.5:
                return i
            
# Happy Number
class Solution(object):
    def isHappy(self, n):
        def convert(value):
            return sum(int(i) ** 2 for i in str(value))

        already = set()

        while n != 1 and n not in already:
            already.add(n)
            n = convert(n)

        return n == 1
    
# Contains Duplicate
class Solution(object):
    def containsDuplicate(self, nums):
        return sorted(nums) != sorted(list(set(nums)))
    
# Contains Duplicate II
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        num_index = {}
        for i, num in enumerate(nums):
            if num in num_index and i - num_index[num] <= k:
                return True
            num_index[num] = i
        return False
    
# Power of Two
class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        
        while n%2 == 0:
            n //= 2
        
        return n == 1
    
# Valid Anagram
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(list(s)) == sorted(list(t))
    
# Add Digits
class Solution(object):
    def addDigits(self, num):
        def convert(val):
            return sum(int(i) for i in str(val))

        while len(str(num)) != 1:
            num = convert(num)

        return num

# Ugly Number
class Solution(object):
    def isUgly(self, num):
        if num <= 0:
            return False
        
        while num % 2 == 0:
            num //= 2
        while num % 3 == 0:
            num //= 3
        while num % 5 == 0:
            num //= 5
        
        return num == 1