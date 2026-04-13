class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        for i in range(len(flowerbed)):
            if flowerbed[i] != 1 and flowerbed[max(0,i-1)] != 1 and flowerbed[min(len(flowerbed) - 1,i+1)] != 1 :
                flowerbed[i] = 1
                if n == 0 : 
                    break 
                else :
                    n -= 1
        if n == 0 : 
            return True 
        else :
            return False                