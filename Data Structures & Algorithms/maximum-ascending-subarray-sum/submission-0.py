class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        summation = 0
        max_sum = float('-inf')
        for i in range(0 , len(nums)):
            if i == 0 or nums[i] > nums[i-1]:
                summation += nums[i]
            else :
                summation = nums[i]


            if summation > max_sum:
                max_sum = summation

        return max_sum        