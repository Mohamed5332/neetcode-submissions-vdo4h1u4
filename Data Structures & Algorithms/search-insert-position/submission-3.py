class Solution:

    def function(self, nums , left , right , target):
        mid = int( (left + right) / 2)

        # handle cases of not found
        if right == -1 :
            return 0
    
        if left == len(nums):
            return left
        

        # handle case that the target exist already..
        if nums[mid] == target:
            return mid

        # solution normal cases
        if nums[mid] < target and target < nums[min(len(nums)-1, mid+1)]:
            return mid + 1

        if nums[mid] > target and nums[max(0 , mid-1)] < target  :
            return mid  
    

        # recurrsive action..
        elif nums[mid] > target :
            return self.function(nums , left , mid - 1 , target)
    

        elif nums[mid] < target :
            return self.function(nums , mid + 1 , right , target)

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.function(nums , 0 , len(nums) - 1 , target)
        