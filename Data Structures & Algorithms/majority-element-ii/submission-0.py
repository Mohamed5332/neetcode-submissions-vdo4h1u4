class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dictionary = dict.fromkeys(nums , 0)
        limit = int(len(nums) / 3) # truncate here is a ceil 
        res = []

        for item in nums : 
            dictionary[item] += 1


        for key , val in dictionary.items() :
            if val > limit :
                res.append(key)

        return res
