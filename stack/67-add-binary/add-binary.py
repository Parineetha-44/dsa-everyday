class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal1=0
        decimal2=0
        for digit in a:
            decimal1=decimal1*2+int(digit)
        for digit in b:
            decimal2=decimal2*2+int(digit)
        c=decimal1+decimal2
        binary=""
        if c==0:
            return "0"
        while c>0:
            binary=str(c%2)+binary
            c=c//2
        return binary
        

        