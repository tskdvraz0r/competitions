class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter

        for idx, val in Counter(nums).items():
            if val == 1:
                return idx