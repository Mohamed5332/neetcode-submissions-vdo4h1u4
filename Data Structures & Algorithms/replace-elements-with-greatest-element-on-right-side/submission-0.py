class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(0, len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
            else :    
                max_element = max(arr[i+1:])
                arr[i] = max_element

        return arr

# o(n^2)

        