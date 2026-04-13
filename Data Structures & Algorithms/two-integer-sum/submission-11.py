class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = []
        result = []
        for item in nums : 
            temp.append(target - item)

        for i in range(0 , len(nums)):
            if temp[i] in nums : 
                result.append(i)

        if len(result) > 2 :
            for item in result:
                if nums[item] * 2 == target :
                   result.remove(item)
        
        return result                         
