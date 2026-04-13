class Solution:
    def countSeniors(self, details: List[str]) -> int:
        sum = 0 
        counter = 0 
        for i in range(len(details)):
            sum = 0 
            for j in range(11 , len(details[1]) - 2):
                sum = sum * 10 + int(details[i][j])
            if sum > 60 : 
                counter += 1 

        return counter
        