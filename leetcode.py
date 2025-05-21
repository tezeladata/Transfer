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