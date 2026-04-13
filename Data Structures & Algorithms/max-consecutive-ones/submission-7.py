class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0 
        counter = 0 
        max_length = 0 
        while i < len(nums):
            if nums[i] == 1 : 
                counter += 1
                i+=1
            else :
                if counter > max_length:
                    max_length = counter 
                while i < len(nums) and nums[i] == 0:
                    i+=1
                counter = 0 

        return max(counter, max_length)