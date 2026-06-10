class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_s = set(nums)

        for i in num_s:
            if i-1 not in num_s:
                count = 1
                curr = i
                while curr+1 in num_s:
                    count += 1
                    curr += 1
                longest = max(count,longest)

        return longest

                