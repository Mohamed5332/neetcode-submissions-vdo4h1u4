class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        result = []
        dictionary2 = dict.fromkeys(nums2 ,0)
        for i in range(len(nums2)):
            stack.append(nums2[i])
            for j in range(i , len(nums2)):
                if stack[-1] < nums2[j]:
                    dictionary2[stack[-1]] = nums2[j]
                    stack.pop()
                    break 
                if j == len(nums2)-1:
                    dictionary2[stack[-1]] = -1


        for item in nums1:
            result.append(dictionary2[item])

        return result

        