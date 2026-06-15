class Solution:
    def resultingString(self, s: str) -> str:
        st=[]
        for c in s:
            if st and (abs(ord(st[-1])-ord(c))==1 or abs(ord(st[-1])-ord(c))==25):
                st.pop()
            else:
                st.append(c)
        return "".join(st)