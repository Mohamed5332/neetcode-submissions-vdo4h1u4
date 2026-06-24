class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_with_Zero = 0
        total_without_zero = 1
        zero_counter = 0 
        for item in nums :
            total_with_Zero = total_with_Zero * item

        for item in nums :
            if item  != 0 :
                total_without_zero = total_without_zero * item
            else :
                zero_counter += 1
                continue    


        result = []
        for item in nums:
            if item == 0 and zero_counter > 1 :
                result.append(total_with_Zero)
            elif item == 0 and zero_counter <= 1:
                result.append(total_without_zero)
            elif item != 0 and zero_counter >= 1:
                result.append(total_with_Zero)
            else :
                result.append(int(total_without_zero/item))    
        
        return result
