class Solution:
    def maxProduct(self, n: int) -> int:
        temp=n
        x=[]
        ans=0
        while temp>0:
            r=temp%10
            x.append(r)
            temp//=10
        for i in range(len(x)):
            for j in range(i+1,len(x)):
                mu=x[i]*x[j]
                if mu>ans:
                    ans=mu
        return ans

        