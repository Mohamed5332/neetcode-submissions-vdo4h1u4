class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        summation = []
        temp = 0
        countRigth = 0 
        countLeft = 0
        # building the summation array 

        for i in range(0 , len(nums)):
            temp += nums[i]
            summation.append(temp)


        for i in range(0 , len(nums)):
            countLeft = 0 
            countRigth = 0 
            if i == 0:
                countRigth = summation[-1] - summation[i]
                countLeft = 0
            elif i == len(nums) - 1:
                countRigth = 0 
                countLeft = summation[i-1]
            else :
                countRigth = summation[-1] - summation[i]
                countLeft = summation[i-1]


            if countRigth == countLeft :
                return i
        return -1        
                

        