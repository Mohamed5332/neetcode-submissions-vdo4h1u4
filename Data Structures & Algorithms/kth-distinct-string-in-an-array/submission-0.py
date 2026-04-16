class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = 1
        dictionary = dict.fromkeys(arr , 0)
        for item in arr:
            dictionary[item] +=1

        print(dictionary)
        for key , val in dictionary.items():
            if val == 1:
                if counter == k :
                    return key
                else :
                    counter +=1
        return ""            

        