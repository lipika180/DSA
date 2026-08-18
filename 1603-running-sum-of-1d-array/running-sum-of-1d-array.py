class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        total=0

        for x in nums:
            total+=x
            ans.append(total)
        return ans
        