class Solution:
    def minOperations(self, nums: list[int]) -> int:
        def isprime(x):
            if x<2:
                return False
            else:
                for i in range(2,int(x**0.5)+1):
                    if x%i==0:
                        return False
        
                return True
        c=0
        p=0
        for i in range(len(nums)):
            x=nums[i]
            if i%2==0:
                while not isprime(x):
                    x+=1
            else:
                while isprime(x):
                    x+=1
            p+=x-nums[i]
        return p
