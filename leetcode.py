# Minimum element after replacement with digit sum
class Solution(object):
    def minElement(self, nums):
        return min([sum([int(x) for x in str(i)]) for i in nums])