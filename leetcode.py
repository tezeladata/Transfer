# Minimum element after replacement with digit sum
class Solution(object):
    def minElement(self, nums):
        return min([sum([int(x) for x in str(i)]) for i in nums])

# Find the k-th character in string game I
class Solution(object):
    def kthCharacter(self, k, word="a"):
        alp = "abcdefghijklmnopqrstuvwxyz"

        while len(word) < k:
            new = ""
            for i in word:
                ind = alp.index(i)
                new += alp[(ind+1)%26]
            word += new
        
        return word[k-1]

# Smallest divisible digit product I
class Solution(object):
    def smallestNumber(self, n, t):
        def prod(n):
            res = 1
            for i in str(n):
                res *= int(i)
            return res

        res = n
        while prod(res)%t!=0:
            res += 1
        return res

# XOR operation in array
class Solution(object):
    def xorOperation(self, n, start):
        res = []

        for i in range(n):
            res.append(start+2*i)
        
        fin = 0
        for i in res:
            fin ^= i
        return fin

# Smallest number with all set bits
class Solution(object):
    def smallestNumber(self, n):
        while len(set(bin(n)[2:]))!=1:
            n += 1
        return n

# Count odd numbers in an interval range
class Solution(object):
    def countOdds(self, low, high):
        if high%2==0 and low%2==0:
            return (high-low)//2
        else:
            return (high-low)//2 + 1
    
# Number of good pairs
class Solution(object):
    def numIdenticalPairs(self, nums):
        res = []
        for i in range(len(nums)):
            for x in range(i+1, len(nums)):
                if nums[i]==nums[x] and i<x:
                    res.append([i, x])
        
        return len(res)