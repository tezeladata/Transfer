# Decompress run-length encoded list
class Solution(object):
    def decompressRLElist(self, nums):
        res = []

        for i in range(0, len(nums), 2):
            sub = nums[i:i+2]
            for x in range(sub[0]):
                res.append(sub[1])
        
        return res

# Rank transform of an array
class Solution(object):
    def arrayRankTransform(self, arr):
        rank = {num: i+1 for i, num in enumerate(sorted(set(arr)))}
        return [rank[num] for num in arr]

# The k weakest rows in a matrix
class Solution(object):
    def kWeakestRows(self, mat, k):
        return [x[0] for x in sorted([[i, mat[i].count(1)] for i in range(len(mat))], key=lambda x: x[1])[:k]]

# Count negative numbers in a sorted matrix
class Solution(object):
    def countNegatives(self, grid):
        res = 0
        for i in grid:
            for x in i: 
                if x < 0: res += 1
        return res

# Sort the integers by the number of 1 bits
class Solution(object):
    def sortByBits(self, arr):
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))

# How many numbers are smaller than the current number
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        return [len([x for x in nums[:i]+nums[i+1:] if x<nums[i]]) for i in range(len(nums))]

# Lucky numbers in a matrix
class Solution(object):
    def luckyNumbers(self, matrix):
        row_min = [min(row) for row in matrix]
        col_max = [max(col) for col in zip(*matrix)]
        return [num for num in row_min if num in col_max]

# Create target array in the given order
class Solution(object):
    def createTargetArray(self, nums, index):
        res = []
        for i in range(len(nums)):
            res.insert(index[i], nums[i])
        return res

# Maximum product of two elements in an array
class Solution(object):
    def maxProduct(self, nums):
        return (sorted(nums)[-1]-1) * (sorted(nums)[-2]-1)

# Shuffle the array
class Solution(object):
    def shuffle(self, nums, n):
        part1, part2 = nums[:n], nums[n:]
        res = []

        for i in range(len(part1)):
            res.append(part1[i])
            res.append(part2[i])
        
        return res

# Running sum of 1d array
class Solution(object):
    def runningSum(self, nums):
        res = []

        for i in range(1, len(nums)+1):
            res.append(sum(nums[:i]))
        
        return res

# Count good triplets
class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        res = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c: res.append((arr[i], arr[j], arr[k]))
        return len(res)

# Sort array by increasing frequency
class Solution(object):
    def frequencySort(self, nums):
        freqs = sorted(list(set([nums.count(i) for i in set(nums)])))
        res = []

        for freq in freqs:
            res += sorted([x for x in nums if nums.count(x) == freq], reverse=True)
        return res

# Remove duplicates from sorted array
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        k=1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        
        return k

# Baseball game
class Solution(object):
    def calPoints(self, operations):
        scores = []
        for op in operations:
            if op.lstrip('-').isdigit():
                scores.append(int(op))
            elif op == "+":
                scores.append(scores[-1] + scores[-2])
            elif op == "D":
                scores.append(2 * scores[-1])
            elif op == "C":
                scores.pop()
        return sum(scores)

# Number of lines to write string
class Solution(object):
    def numberOfLines(self, widths, s):
        all_lines = []
        cur_line, l_cur_line = "", 0

        get_line_w = lambda x: sum([widths[ord(i) - ord('a')] for i in x])

        for i in s:
            w = widths[ord(i) - ord('a')]
            if l_cur_line + w <= 100:
                cur_line += i
                l_cur_line += w
            else:
                all_lines.append(cur_line)
                cur_line = i
                l_cur_line = w
        all_lines.append(cur_line)

        return [len(all_lines), get_line_w(all_lines[-1])]

# Minimum absolute difference
class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        min_diff = float('inf')
        res = []

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            if diff < min_diff:
                min_diff = diff
                res = [[arr[i-1], arr[i]]]
            elif diff == min_diff:
                res.append([arr[i-1], arr[i]])

        return res

# Unique number of occurences
class Solution(object):
    def uniqueOccurrences(self, arr):
        occurs = [arr.count(i) for i in set(arr)]
        return len(occurs) == len(set(occurs))

# Find the highest altitude
class Solution(object):
    def largestAltitude(self, gain):
        altitude = 0
        highest = 0

        for g in gain:
            altitude += g
            highest = max(highest, altitude)

        return highest

# Find first palindromic string in the array
class Solution(object):
    def firstPalindrome(self, words):
        for i in words:
            if i == i[::-1]:
                return i
        return ""