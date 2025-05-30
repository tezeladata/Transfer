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

# Divisible and non-divisible sums difference
class Solution(object):
    def differenceOfSums(self, n, m):
        return sum([i for i in range(1,n+1) if i%m!=0]) - sum([i for i in range(1,n+1) if i%m==0])

# Greatest common divisor of strings
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        if str1 + str2 != str2 + str1:
            return ""

        gcd_len = gcd(len(str1), len(str2))
        return str1[:gcd_len]

# Distribute candies among children I
class Solution(object):
    def distributeCandies(self, n, limit):
        res = []

        for i in range(limit+1):
            for x in range(limit+1):
                for z in range(limit+1):
                    new_ls = [i, x, z]
                    if sum(new_ls)==n and all(y<=limit for y in new_ls):
                        res.append(new_ls)
        
        return len(res)

# Find missing and repeated values
class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        all_nums = []
        for i in grid:
            for x in i: all_nums.append(x)
        
        f = [i for i in all_nums if all_nums.count(i)==2][0]
        s = [i for i in range(1, max(all_nums)+1) if i not in all_nums]
        return [f, s[0]] if s!=[] else [f, max(all_nums)+1]

# N-th tribonacci number
class Solution(object):
    def tribonacci(self, n):
        if n==0: return 0
        res = [0, 1, 1]
        while len(res)<n+1:
            res.append(sum(res[-3:]))
        return res[-1]

# Type of triangle
class Solution(object):
    def triangleType(self, nums):
        if nums[0]+nums[1] <= nums[2] or nums[1]+nums[2] <= nums[0] or nums[0]+nums[2] <= nums[1]: return "none"
        if all(i==nums[0] for i in nums): return "equilateral"
        if sorted(nums)[0]==sorted(nums)[1] or sorted(nums)[1]==sorted(nums)[2]: return "isosceles"
        if nums[0]!=nums[1] and nums[1]!=nums[2]: return "scalene"

# Number of days between two dates
from datetime import datetime

class Solution(object):
    def daysBetweenDates(self, date1, date2):
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")
        return abs((d1 - d2).days)

# Find the sum of encrypted integers
class Solution(object):
    def sumOfEncryptedInt(self, nums):
        def enc(n):
            return int(str(max([int(i) for i in str(n)]))*len(str(n)))

        res = 0
        for i in nums:
            res += enc(i)
        return res

# Harshad number
class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        return sum([int(i) for i in str(x)]) if x%sum([int(i) for i in str(x)])==0 else -1

# Check if it is a straight line
class Solution(object):
    def checkStraightLine(self, coordinates):
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        for i in range(2, len(coordinates)):
            xi, yi = coordinates[i]
            if (x1 - x0) * (yi - y0) != (y1 - y0) * (xi - x0):
                return False
        return True

# Subtract the product and sum of digits of an integer
class Solution(object):
    def subtractProductAndSum(self, n):
        prod = 1
        for i in range(len(str(n))):
            prod *= int(str(n)[i])

        return prod - sum([int(i) for i in str(n)])

# Find numbers with even number of digits
class Solution(object):
    def findNumbers(self, nums):
        return len([i for i in nums if len(str(i))%2==0])

# Find N unique integers sum up to zero
class Solution(object):
    def sumZero(self, n):
        if n%2==1:
            res = [0] 
        else:
            res = [-1, 1]

        while len(res)<n:
            res.append(max(res)+1)
            res.append(max(res)*-1)

        return res

# Find minimum operations to make all elements divisible by three
class Solution(object):
    def minimumOperations(self, nums):
        return len([i for i in nums if i%3!=0])

# Number of steps to reduce a number to zero
class Solution(object):
    def numberOfSteps(self, num):
        res = 0

        while num!=0:
            if num%2 == 0: num //= 2
            else: num -= 1

            res += 1
        
        return res

# Maximum 69 number
class Solution(object):
    def maximum69Number (self, num):
        if all(i=="9" for i in str(num)): return num

        ind = str(num).index("6")
        return int(str(num)[:ind] + "9" + str(num)[ind+1:])

# Find if digit game can be won
class Solution(object):
    def canAliceWin(self, nums):
        return sum([i for i in nums if len(str(i))==1]) > sum([i for i in nums if len(str(i))==2]) or sum([i for i in nums if len(str(i))==2]) > sum([i for i in nums if len(str(i))==1])

# Count largest group
class Solution(object):
    def countLargestGroup(self, n):
        dig_sum = lambda x: sum([int(i) for i in str(x)])

        all_groups = {}

        for i in range(1, n+1):
            dig = dig_sum(i)
            if dig in all_groups.keys():
                all_groups[dig] = all_groups[dig]+[i]
            else:
                all_groups[dig] = [i]
        
        max_sz = max(len(i) for i in all_groups.values())
        return len([i for i in all_groups.values() if len(i)==max_sz])

# Final array state after K multiplication operations I
class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        for i in range(k):
            ind = nums.index(min(nums))
            nums[ind] = nums[ind]*multiplier
        return nums

# Convert date to binary
class Solution(object):
    def convertDateToBinary(self, date):
        return "-".join([bin(int(i))[2:] for i in date.split("-")])

# Find the key of the numbers
class Solution(object):
    def generateKey(self, num1, num2, num3):
        all_nums = [num1, num2, num3]
        max_len = max(len(str(i)) for i in all_nums)

        for i in range(len(all_nums)):
            num_str = str(all_nums[i])
            if len(num_str) != max_len:
                padding = "0" * (max_len - len(num_str))
                all_nums[i] = padding + num_str
            else:
                all_nums[i] = num_str

        res = "".join(
            str(min(int(all_nums[0][i]), int(all_nums[1][i]), int(all_nums[2][i])))
            for i in range(max_len)
        )
        return int(res)