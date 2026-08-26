class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        seen=set()
        for i in range(len(nums)):
            count=0
            s=" "
            for j in range(i,len(nums)):
                if nums[j]%p==0:
                    count+=1
                if count>k:
                    break
                s+=str(nums[j])+','
                seen.add(s)
        return len(seen)
