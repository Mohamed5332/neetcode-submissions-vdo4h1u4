class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        setStorage = set(nums) # o(n)
        res = []
        for i in range( 1 , len(nums) + 1): # o(n)
            if i not in setStorage : #o(1)
                res.append(i)

        return res # Totaly o(2n) = o(n)
        """
        storage = [0 for i in range(0 , len(nums))] # o(n)
        result = []
        for i in range(0 , len(nums)): # o(n)
            storage[nums[i] - 1] = 1 # act as a marker..

        for i in range(0 , len(nums)): # o(n)
            if storage[i] != 1 :
                result.append(i+1)

        return result # Totally o(3n) = o(n)

        