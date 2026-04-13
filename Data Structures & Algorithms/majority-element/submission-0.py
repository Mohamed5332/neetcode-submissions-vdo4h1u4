class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length_limit = int(len(nums) / 2)
        dictionary = dict.fromkeys(nums ,0)
        for number in nums:
            dictionary[number] += 1

        for key , val in dictionary.items():
            if val > length_limit:
                return key
        