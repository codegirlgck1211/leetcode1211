class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mpp = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in mpp:
                return [mpp[need],i]

            mpp[nums[i]] = i 

        return []

