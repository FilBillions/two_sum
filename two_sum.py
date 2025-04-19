class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, value in enumerate(nums):
            number1 = value
            index1 = index
            for index, value in enumerate(nums):
                number2 = value
                index2 = index
                if index1 != index2:
                    answer = number1 + number2
                    if answer == target:
                        return index1, index2