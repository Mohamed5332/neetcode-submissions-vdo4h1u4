class NumArray:

    def __init__(self, nums: List[int]):
        temp = 0 
        self.prefixSum = []
        for i in range(0 , len(nums)):
            temp += nums[i]
            self.prefixSum.append(temp)


        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0 :
            return self.prefixSum[right]
        else :
            return self.prefixSum[right] - self.prefixSum[left - 1]   
        


