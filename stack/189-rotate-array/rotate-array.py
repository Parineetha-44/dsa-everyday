class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        p=k%len(nums)
        def x(left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        x(0,len(nums)-1)
        x(0,p-1)
        x(p,len(nums)-1)