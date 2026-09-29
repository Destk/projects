#Перебор грубой силой с двумя циклами O(n**2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = []
        for i in range(len(nums)):
            c = target - nums[i]
            for j in range(i+1, len(nums)):
                if c == nums[j]:
                    index.append(i)
                    index.append(j)
        return index
#С помощью словаря O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            c = target - nums[i]
            if c in d:
                return [d[c], i]
            d[nums[i]] = i
        return []
