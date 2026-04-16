class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        setStorage = set(nums) # o(n)
        res = []
        for i in range( 1 , len(nums) + 1): # o(n)
            if i not in setStorage : #o(1)
                res.append(i)

        return res # Totaly o(2n) = o(n)
        
        