class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedArray = sorted(heights)
        counter = 0

        for i in range(0 , len(heights)):
            if heights[i] != sortedArray[i]:
                counter += 1 

        return counter

        




