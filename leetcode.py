# Three divisors
class Solution(object):
    def isThree(self, n):
        return len([i for i in range(1, n+1) if n%i==0]) == 3

# Find greatest common divisor of array
class Solution(object):
    def findGCD(self, nums):
        def gcd(x, y):
            while y:
                x, y = y, x%y
            return x
        return gcd(min(nums), max(nums))

# A number after double reversal
class Solution(object):
    def isSameAfterReversals(self, num):
        if num == 0: return True

        def rem(num):
            while str(num)[0] == "0":
                num = int(str(num)[1:])

        rev1 = int(str(num)[::-1])
        rem(rev1)

        rev2 = int(str(rev1)[::-1])
        rem(rev2)

        return rev2 == num

# Minimum sum of four digit number after splitting digits
class Solution(object):
    def minimumSum(self, num):
        digits = sorted([int(d) for d in str(num)])
        
        num1 = digits[0] * 10 + digits[2]
        num2 = digits[1] * 10 + digits[3]
        
        return num1 + num2

# Count integers with even digit sum
class Solution(object):
    def countEven(self, num):
        return len([i for i in range(2, num+1) if sum([int(x) for x in str(i)])%2==0])

# Add two integers
class Solution(object):
    def sum(self, num1, num2):
        return num1+num2

# Smallest even multiple
class Solution(object):
    def smallestEvenMultiple(self, n):
        return n if n%2 == 0 else n*2

# Number of common factors
class Solution(object):
    def commonFactors(self, a, b):
        return len([x for x in range(1, min(a, b)+1) if a % x == 0 and b % x == 0])

# Average value of even numbers that are divisible by three
class Solution(object):
    def averageValue(self, nums):
        spec = [i for i in nums if i%6==0]
        return sum(spec) // len(spec) if spec else 0

# Convert the temperature
class Solution(object):
    def convertTemperature(self, celsius):
        return [celsius + 273.15, celsius*1.80 + 32.00]

# Find the pivot integer
class Solution(object):
    def pivotInteger(self, n):
        for i in range(1, n+1):
            if sum(range(1, i+1)) == sum(range(i, n+1)): return i
        return -1

# Count the digits that divide a number
class Solution(object):
    def countDigits(self, num):
        return len([int(i) for i in str(num) if num%int(i)==0])

# Difference between element sum and digit sum of array
class Solution(object):
    def differenceOfSum(self, nums):
        dig_sum = lambda num: sum([int(i) for i in str(num)])
        return abs(sum(nums)-sum([dig_sum(i) for i in nums]))

# Alternating digit sum
class Solution(object):
    def alternateDigitSum(self, n):
        n = [int(i) for i in str(n)]
        return sum([n[i]*-1 if i%2==1 else n[i] for i in range(len(n))])

# Split with minimum sum
class Solution(object):
    def splitNum(self, num):
        digits = sorted(str(num)) 
        
        num1 = ""
        num2 = ""
        
        for i in range(len(digits)):
            if i % 2 == 0:
                num1 += digits[i]
            else:
                num2 += digits[i]
        
        return int(num1) + int(num2)

# K items with the maximum sum
class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        all_nums = sorted([1 for _ in range(numOnes)] + [0 for _ in range(numZeros)] + [-1 for _ in range(numNegOnes)])
        res = 0

        while k > 0:
            res += all_nums[-1]
            all_nums = all_nums[:-1]
            k -= 1
        
        return res

# Calculate delayed arrival time
class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        return arrivalTime + delayedTime if arrivalTime + delayedTime < 24 else (arrivalTime + delayedTime)%24

# Sum multiples
class Solution(object):
    def sumOfMultiples(self, n):
        return sum([i for i in range(1, n+1) if i%3==0 or i%5==0 or i%7==0])

# Find the maximum achievable number
class Solution(object):
    def theMaximumAchievableX(self, num, t):
        return num + 2*t

# Prime number of set bits in binary representation
class Solution(object):
    def countPrimeSetBits(self, left, right):
        def is_prime(num):
            if num <= 1: return False
            for i in range(2, int(num**0.5)+1):
                if num%i==0: return False
            return True
        
        res = 0
        for i in range(left, right+1):
            if is_prime(bin(i).count("1")): res += 1
        
        return res

# Check if the number is fascinating
class Solution(object):
    def isFascinating(self, n):
        new_num = str(n)+str(n*2)+str(n*3)
        return len(new_num) == len(set(new_num)) and "0" not in new_num

# Number of beautiful pairs
class Solution(object):
    def countBeautifulPairs(self, nums):
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        
        count = 0
        for i in range(len(nums)):
            first_digit = int(str(nums[i])[0])
            for j in range(i+1, len(nums)):
                last_digit = nums[j] % 10
                if gcd(first_digit, last_digit) == 1:
                    count += 1
        return count

# Maximum odd binary number
class Solution(object):
    def maximumOddBinaryNumber(self, s):
        if s.count("1") == 1: return "0"*s.count("0")+"1"
        else:
            return "1"*(s.count("1")-1)+"0"*s.count("0")+"1"

# Count symmetric strings
class Solution(object):
    def countSymmetricIntegers(self, low, high):
        res = 0

        for i in range(low, high + 1):
            s = str(i)
            if len(s) % 2 == 0:
                mid = len(s) // 2
                left_sum = sum(int(d) for d in s[:mid])
                right_sum = sum(int(d) for d in s[mid:])
                if left_sum == right_sum:
                    res += 1

        return res