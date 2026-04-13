class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary_s = dict.fromkeys(s,0)
        dictionary_t = dict.fromkeys(t,0)
        counter = 0 

        for i in range(len(s)):
            dictionary_s[s[i]] += 1

        for i in range(len(t)):
            dictionary_t[t[i]] += 1

        if len(dictionary_s) == len(dictionary_t):
            for key , val in dictionary_s.items() :
                if val == dictionary_t.get(key) : 
                    counter += 1
        else :
            return False           

        if counter != len(dictionary_s):
            return False
        else :
            return True
        