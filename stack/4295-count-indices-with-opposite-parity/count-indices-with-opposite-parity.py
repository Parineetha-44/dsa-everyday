class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        pari=[]
        i=0
        j=0
        for i in range(len(nums)):
            count=0
            for j in range(i+1,len(nums)):
                if nums[i]%2==0 and nums[j]%2!=0:
                    count+=1
                elif nums[i]%2!=0 and nums[j]%2==0:
                    count+=1
            pari.append(count)
        return pari
                
                

        