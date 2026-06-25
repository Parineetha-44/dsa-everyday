class Solution:
    def decodeString(self, s: str) -> str:
        numb=[]
        stri=[]
        curr=""
        num=0
        for p in s:
            if p.isdigit():
                num=num*10+int(p)
            elif p=='[':
                numb.append(num)
                stri.append(curr)
                num=0
                curr=""
            elif p==']':
                repeat=numb.pop()
                previous=stri.pop()
                curr=previous+curr*repeat
            else:
                curr+=p
        return curr

        
