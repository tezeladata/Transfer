# Valid palindrome II
class Solution(object):
    def validPalindrome(self, s):
        def is_palindrome_range(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return is_palindrome_range(left+1, right) or is_palindrome_range(left, right-1)
            left += 1
            right -= 1

        return True

# Count binary substrings
class Solution(object):
    def countBinarySubstrings(self, s):
        prev, curr = 0, 1
        count = 0
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr += 1
            else:
                count += min(prev, curr)
                prev = curr
                curr = 1
                
        return count + min(prev, curr)

# Degree of an array
class Solution(object):
    def findShortestSubArray(self, nums):
        left = {}
        right = {}
        count = {}
        
        for i in range(len(nums)):
            num = nums[i]
            if num not in left:
                left[num] = i
            right[num] = i
            if num not in count:
                count[num] = 0
            count[num] += 1
        
        degree = max(count.values())
        min_len = len(nums)
        
        for num in count:
            if count[num] == degree:
                length = right[num] - left[num] + 1
                if length < min_len:
                    min_len = length
        
        return min_len

# Binary search
class Solution(object):
    def search(self, nums, target):
        low, high = 0, len(nums)-1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target: return mid
            elif nums[mid] < target: low = mid + 1
            else: high = mid - 1

        return -1

# To lower case
class Solution(object):
    def toLowerCase(self, s):
        return s.lower()

# Find pivot index
class Solution(object):
    def pivotIndex(self, nums):
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]): return i
        return -1

# Self dividing numbers
class Solution(object):
    def selfDividingNumbers(self, left, right):
        return [i for i in range(left, right+1) if "0" not in str(i) and (lambda n: all(n%int(i)==0 for i in str(n)))(i)]

# Find smallest letter greater than target
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        all_variants = []

        for i in letters:
            if alphabet.index(i) - alphabet.index(target) > 0: all_variants.append([i, alphabet.index(i) - alphabet.index(target)])
        
        return sorted(all_variants, key = lambda x: x[1])[0][0] if len(all_variants) > 0 else letters[0]

# Largest number at least twice of others
class Solution(object):
    def dominantIndex(self, nums):
        return nums.index(max(nums)) if all(max(nums) >= i*2 for i in [i for i in nums if i!=max(nums)]) else -1

# 