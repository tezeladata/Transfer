# Reshape the matrix
class Solution(object):
    def matrixReshape(self, mat, r, c):
        all_nums = []

        for ls in mat:
            for num in ls:
                all_nums.append(num)

        if len(all_nums) != r * c:
            return mat
        
        res = []
        for i in range(r):
            res.append(all_nums[:c])
            all_nums = all_nums[c:]
        
        return res

# Longest continuous increasing subsequence
class Solution(object):
    def findLengthOfLCIS(self, nums):
        arr = [nums[0]]
        all_arrs = []

        for i in nums:
            if i > arr[-1]: arr.append(i)
            else:
                all_arrs.append(arr)
                arr = [i]
        all_arrs.append(arr)
        
        all_arrs = sorted(all_arrs, key=lambda x: len(x))
        return len(all_arrs[-1])

# 1-bit and 2-bit characters
class Solution(object):
    def isOneBitCharacter(self, bits):
        i = 0
        n = len(bits)
        while i < n - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return i == n - 1

# Shortest distance to a character
class Solution(object):
    def shortestToChar(self, s, c):
        c_indices = [i for i in range(len(s)) if s[i] == c]
        res = []

        for i in range(len(s)):
            if i <= c_indices[0]: res.append(c_indices[0] - i)
            else:
                sm = [x for x in c_indices if x <= i]
                up = [x for x in c_indices if x > i]

                if len(sm) > 0:
                    sm_dist = i-sm[-1]
                    
                    if len(up) > 0:
                        up_dist = up[0]-i

                        res.append(min(sm_dist, up_dist))
                    else:
                        res.append(sm_dist)
                else:
                    res.append(up[0]-i)
        
        return res

# Flipping an image
class Solution(object):
    def flipAndInvertImage(self, image):
        flip = [i[::-1] for i in image]
        res = []

        for i in flip:
            new_i = []
            for x in i:
                if x==0: new_i.append(1)
                else: new_i.append(0)
            res.append(new_i)
        return res

# Transpose matrix
class Solution(object):
    def transpose(self, matrix):
        res = []
        for i in range(len(matrix[0])): 
            new_i = []
            for x in range(len(matrix)):  new_i.append(0)
            res.append(new_i)
        
        for i in range(len(matrix)):
            for x in range(len(matrix[0])):
                res[x][i] = matrix[i][x]
        
        return res

# Fair candy swap
class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        sum_a, sum_b = sum(aliceSizes), sum(bobSizes)
        diff = (sum_a-sum_b) // 2

        set_b = set(bobSizes)

        for a in aliceSizes:
            b = a - diff
            if b in set_b: return [a, b]

# Monotonic array
class Solution(object):
    def isMonotonic(self, nums):
        return nums==sorted(nums) or nums==sorted(nums, reverse=True)

# Sort array by parity
class Solution(object):
    def sortArrayByParity(self, nums):
        return [i for i in nums if i%2==0] + [i for i in nums if i%2==1]

# X of a kind in a deck of cards
class Solution(object):
    def hasGroupsSizeX(self, deck):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        count_dict = {}
        for card in deck:
            if card in count_dict:
                count_dict[card] += 1
            else:
                count_dict[card] = 1

        counts = count_dict.values()

        x = 0
        for c in counts:
            x = gcd(x, c)

        return x >= 2

# Sort array by parity II
class Solution(object):
    def sortArrayByParityII(self, nums):
        e, o = [i for i in nums if i%2==0], [i for i in nums if i%2==1]
        res = []

        for i in range(len(nums)):
            if i%2 == 0:
                res.append(e[0])
                e = e[1:]
            else:
                res.append(o[0])
                o = o[1:]
        
        return res

# Valid mountain array
class Solution(object):
    def validMountainArray(self, arr):
        n = len(arr)
        if n < 3:
            return False

        i = 0

        while i + 1 < n and arr[i] < arr[i + 1]: i += 1

        if i == 0 or i == n - 1: return False

        while i + 1 < n and arr[i] > arr[i + 1]: i += 1
        return i == n - 1

# Delete columns to make sorted
class Solution(object):
    def minDeletionSize(self, strs):
        count = 0
        for i in range(len(strs[0])):
            all_chars = []
            for word in strs: all_chars.append(word[i])
            if all_chars != sorted(all_chars): count += 1
        return count

# N-repeated element in size 2N array
class Solution(object):
    def repeatedNTimes(self, nums):
        return [i for i in set(nums) if nums.count(i)==len(nums)//2][0]

# Largest perimeter triangle
class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0

# Squares of a sorted array
class Solution(object):
    def sortedSquares(self, nums):
        return sorted([i**2 for i in nums])

# Add to array-form of integer
class Solution(object):
    def addToArrayForm(self, num, k):
        return [int(i) for i in str(int("".join([str(i) for i in num]))+k)]

# Available captures to a rook
class Solution(object):
    def numRookCaptures(self, board):
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rook_i, rook_j = i, j

        count = 0
        # Up
        for x in range(rook_i - 1, -1, -1):
            if board[x][rook_j] == 'B':
                break
            if board[x][rook_j] == 'p':
                count += 1
                break
        # Down
        for x in range(rook_i + 1, 8):
            if board[x][rook_j] == 'B':
                break
            if board[x][rook_j] == 'p':
                count += 1
                break
        # Left
        for y in range(rook_j - 1, -1, -1):
            if board[rook_i][y] == 'B':
                break
            if board[rook_i][y] == 'p':
                count += 1
                break
        # Right
        for y in range(rook_j + 1, 8):
            if board[rook_i][y] == 'B':
                break
            if board[rook_i][y] == 'p':
                count += 1
                break

        return count

# Find common characters
class Solution(object):
    def commonChars(self, words):
        res = []
        for c in set(words[0]):
            counts = [word.count(c) for word in words]
            if 0 not in counts:
                res.extend([c] * min(counts))
        return res

# Matrix cells in distance order
class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        res = []
        for r in range(rows):
            for c in range(cols): res.append([[r, c], abs(rCenter-r) + abs(cCenter-c)])
        
        return [i[0] for i in sorted(res, key=lambda x: x[1])]

# Find words that can be formed by characters
class Solution(object):
    def countCharacters(self, words, chars):
        return sum([len(i) for i in words if all(chars.count(x) >= i.count(x) for x in i)])

# Height checker
class Solution(object):
    def heightChecker(self, heights):
        return sum([1 for i in range(len(heights)) if heights[i] != sorted(heights)[i]])

# Mean of array after removing some elements
class Solution(object):
    def trimMean(self, arr):
        n = len(arr)
        arr.sort()
        cut = int(n * 0.05)
        trimmed_arr = arr[cut : n - cut]
        return float(sum(trimmed_arr)) / len(trimmed_arr)

# Relative sort array
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        order = {num: i for i, num in enumerate(arr2)}
        return sorted(arr1, key=lambda x: (order.get(x, len(arr2) + x)))

# Replace elements with greatest element on right side
class Solution(object):
    def replaceElements(self, arr):
        max_right = -1
        for i in range(len(arr) - 1, -1, -1):
            new_val = max_right
            max_right = max(max_right, arr[i])
            arr[i] = new_val
        return arr