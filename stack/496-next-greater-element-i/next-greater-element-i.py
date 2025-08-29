class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        for i in range(0,len(nums1)):
            boo=False
            great=-1
            for j in range(len(nums2)) :
                if nums2[j]==nums1[i]:
                    boo=True
                if boo and nums2[j]>nums1[i]:
                    great=nums2[j]
                    break
            stack.append(great) 
        return stack