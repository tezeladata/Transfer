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

# Maximum subarray with equal products
class Solution(object):
    def maxLength(self, nums):
        def prod(arr):
            res = 1
            for i in arr:
                res*=i
            return res

        def gcd(x, y):
            while y:
                x, y = y, x%y
            return x

        def lcm(x, y):
            return abs(x*y) // gcd(x, y)
        
        def get_all_subarrays(arr):
            n = len(arr)
            return [arr[i:j+1] for i in range(n) for j in range(i, n)]
        
        all_subs = sorted(get_all_subarrays(nums), key=lambda x: len(x), reverse=True)
        for i in all_subs:
            arr_lcm = lcm(i[0], i[1])
            for x in i[2:]:
                arr_lcm = lcm(arr_lcm, x)
            
            arr_gcd = gcd(i[0], i[1])
            for z in i[2:]:
                arr_gcd = gcd(arr_gcd, z)
            
            if prod(i) == arr_lcm * arr_gcd: return len(i)

# Count partitions with even sum difference
class Solution(object):
    def countPartitions(self, nums):
        return len([i for i in range(1,len(nums)) if (sum(nums[:i]) - sum(nums[i:])) %2 == 0])

# Sum of all odd length subarrays
class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        def get_all_subarrays(arr):
            n = len(arr)
            return [arr[i:j+1] for i in range(n) for j in range(i, n)]
        
        return sum([sum(i) for i in get_all_subarrays(arr) if len(i)%2==1])

# Check if digits are equal in string after operations I
class Solution(object):
    def hasSameDigits(self, s):
        def change(st):
            res = ""
            for i in range(1, len(st)):
                res += str((int(st[i]) + int(st[i-1]))%10)
            return res
        
        while len(s)!=2:
            s = change(s)
        
        return len(set(s))==1

# Find closest person
class Solution(object):
    def findClosest(self, x, y, z):
        first = abs(x-z)
        second = abs(y-z)

        if first == second: return 0
        return 1 if first < second else 2

# Maximum product of two digits
class Solution(object):
    def maxProduct(self, n):
        return sorted([int(i) for i in str(n)])[-1] * sorted([int(i) for i in str(n)])[-2]

# Smallest index with digit sum equal to index
class Solution(object):
    def smallestIndex(self, nums):
        sum_digs = lambda x: sum([int(i) for i in str(x)])

        for i in range(len(nums)):
            if i == sum_digs(nums[i]): return i
        
        return -1

# Maximum number of balls in a box
class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        all_boxes = [[] for _ in range(int("9"*len(str(highLimit))))]
        dig_sum = lambda x: sum([int(i) for i in str(x)])

        for i in range(lowLimit, highLimit+1):
            sm = dig_sum(i)
            all_boxes[sm-1].append(1)
        
        all_boxes = [i for i in all_boxes if i!=[]]
        return sum(sorted(all_boxes, key=lambda x: sum(x))[-1])