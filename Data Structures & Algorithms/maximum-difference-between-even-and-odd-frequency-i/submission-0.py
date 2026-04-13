class Solution:
    def maxDifference(self, s: str) -> int:
        # initialization 
        dictionary = dict.fromkeys(s , 0)
        max_odd = 0
        min_even = float('inf')
        for ch in s : 
            dictionary[ch] += 1 
        # Logic 
        for key , value in dictionary.items():
            if value % 2 == 0 : # even value 
                if value < min_even:
                    min_even = value
            else :
                if value > max_odd : # odd value 
                    max_odd = value        

        # result
        return max_odd - min_even # max difference..
        