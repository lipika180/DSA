class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result=[]

        for x in nums:
            if x!=0:
                result.append(x)

        while len(result)<len(nums):
                result.append(0)
        nums[:]=result
        