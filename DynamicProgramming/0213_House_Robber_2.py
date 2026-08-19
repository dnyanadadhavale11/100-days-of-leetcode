class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        def rob_line(houses):
            prev2 = 0
            prev1 = 0

            for money in houses:
                current = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = current

            return prev1

        # Case 1: Rob houses from 0 to n-2
        # Case 2: Rob houses from 1 to n-1
        return max(rob_line(nums[:-1]), rob_line(nums[1:]))