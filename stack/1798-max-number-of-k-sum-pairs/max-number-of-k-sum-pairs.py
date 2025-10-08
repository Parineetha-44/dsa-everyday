class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums1=sorted(nums)
        pari=0
        veena=len(nums1)-1
        count=0
        while pari<veena:
            sum= nums1[pari]+nums1[veena]
            if sum==k:
                pari+=1
                veena-=1
                count+=1
            elif sum<k:
                pari+=1
            else:
                veena-=1
        return count


        
