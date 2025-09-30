class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        hehe=[]
        for i in range(len(nums)):
            if nums[i]==target:
                hehe.append(i)
                break
        if target not in nums:
            hehe.append(-1)
        for j in range(len(nums)-1,-1,-1):
            if nums[j]==target:
                hehe.append(j)
                break
        if target not in nums:
            hehe.append(-1)

        return hehe
        