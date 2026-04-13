class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_element = arr[-1]
        for i in range(len(arr) - 2, -1,-1):
            if arr[i] > max_element:
                temp = max_element
                max_element = arr[i] 
                arr[i] = temp
            else :
                arr[i] = max_element

        arr[-1] = -1   
        return arr

# o(n^2) # what about some enhancement..o(n)=> achieved...