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

# Excel sheet column number
class Solution(object):
    def titleToNumber(self, columnTitle):
        res = 0
        for i in columnTitle: res = res * 26 + (ord(i) - ord('A') + 1)
        
        return res

# Ransom note
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        return all(ransomNote.count(i) <= magazine.count(i) for i in ransomNote)

# Keyboard row
class Solution(object):
    def findWords(self, words):
        def check_exists(word, row):
            if all(x.lower() in row for x in word): res.append(word)

        first, second, third = "qwertyuiop", "asdfghjkl", "zxcvbnm"
        res = []

        for i in words:
            if i.lower()[0] in first: check_exists(i, first)
            elif i.lower()[0] in second: check_exists(i, second)
            else: check_exists(i, third)
        
        return res

# Longest uncommon subsequence I
class Solution(object):
    def findLUSlength(self, a, b):
        def gen_subsec(word):
            res = []
            for i in range(len(word)):
                for x in range(i+1, len(word)+1):
                    res.append(word[i:x])
            return res
        
        sub_a = gen_subsec(a)
        sub_b = gen_subsec(b)
        uncommon = [i for i in sub_a if i not in sub_b] + [i for i in sub_b if i not in sub_a]
        uncommon.sort(key=lambda x: len(x))
        return len(uncommon[-1]) if len(uncommon) > 0 else -1

# Student attendance record I
class Solution(object):
    def checkRecord(self, s):
        return s.count("A") < 2 and "LLL" not in s

# Reverse words in a string III
class Solution(object):
    def reverseWords(self, s):
        return " ".join([i[::-1] for i in s.split(" ")])

# Robot return to origin
class Solution(object):
    def judgeCircle(self, moves):
        return moves.count("U")==moves.count("D") and moves.count("R")==moves.count("L")

# Jewels and stones
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        return sum([stones.count(i) for i in set(jewels)])

# Rotate string
class Solution(object):
    def rotateString(self, s, goal):
        all_rotates = [s]
        for i in range(1, len(s)):
            all_rotates.append(s[i:] + s[:i])
        
        return goal in all_rotates

# Unique morse code words
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse, alp = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."], "abcdefghijklmnopqrstuvwxyz"
        res = set()

        for i in words:
            new_w = ""
            for x in i:
                new_w += morse[alp.index(x)]
            res.add(new_w)
        
        return len(res)

# Most common word
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, ' ')
        words = paragraph.lower().split()
        word_count = {}
        for word in words:
            if word not in banned:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
        max_count = 0
        result = ''
        for word in word_count:
            if word_count[word] > max_count:
                max_count = word_count[word]
                result = word
        return result

# Merge sorted array
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        left, right = nums1[:m], nums2[:n]

        nums1[:] = left
        for i in right:
            nums1.append(i)
        nums1.sort()

# Pascal's triangle II
class Solution(object):
    def getRow(self, rowIndex):
        a = []

        for i in range(rowIndex+1):
            a.append([])
            a[i].append(1)
            for j in range(1, i):
                a[i].append(a[i-1][j-1] + a[i-1][j])
            if rowIndex != 0:
                a[i].append(1)
        
        return a[-1]

# Contains duplicate II
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        num_indices = {}

        for i, num in enumerate(nums):
            if num in num_indices and i - num_indices[num] <= k:
                return True
            num_indices[num] = i

        return False

# Island perimeter
class Solution(object):
    def islandPerimeter(self, grid):
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res += 4
                    if i > 0 and grid[i-1][j] == 1:  # up
                        res -= 1
                    if i < len(grid) - 1 and grid[i+1][j] == 1:  # down
                        res -= 1
                    if j > 0 and grid[i][j-1] == 1:  # left
                        res -= 1
                    if j < len(grid[0]) - 1 and grid[i][j+1] == 1:  # right
                        res -= 1
        return res

# Next greater element I
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        ans = []

        for num in nums1:
            if num in nums2:
                ind = nums2.index(num)
                added = False

                for i in nums2[ind+1:]:
                    if i > num:
                        ans.append(i)
                        added = True
                        break
                
                if not added: ans.append(-1)
        
        return ans

# Teemo attacking
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        if not timeSeries:
            return 0
        
        total = 0
        for i in range(len(timeSeries) - 1):
            total += min(timeSeries[i+1] - timeSeries[i], duration)
        total += duration 
        return total

# Relative ranks
class Solution(object):
    def findRelativeRanks(self, score):
        sr_scores = sorted(score, reverse=True)
        res = []

        for i in score:
            if i not in sr_scores[:3]: res.append(str(sr_scores.index(i)+1))
            else:
                if i == max(score): res.append("Gold Medal")
                elif i == sr_scores[1]: res.append("Silver Medal")
                else: res.append("Bronze Medal")
        
        return res