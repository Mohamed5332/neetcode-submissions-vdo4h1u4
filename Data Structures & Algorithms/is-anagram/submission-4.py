class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {item : 0 for item in s}
        dict2 = {item : 0 for item in t}

        for item in s : 
           dict1[item] += 1
        for item in t : 
           dict2[item] +=1 

        return dict1 == dict2   
                
        