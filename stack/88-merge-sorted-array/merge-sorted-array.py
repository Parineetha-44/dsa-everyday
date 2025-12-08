class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==0:
            return 
        j=0
        for i in range(m+n):
            if nums1[i]==0:
                nums1[i]=nums2[j]
                j+=1
                if j==len(nums2):
                    break
        nums1.sort()