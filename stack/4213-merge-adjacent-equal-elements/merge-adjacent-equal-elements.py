class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        st=[]
        s=0
        for i in range(len(nums)):
            veena=nums[i]
            while st and st[-1]==veena:
                veena+=st.pop()
            st.append(veena)
        return st
        