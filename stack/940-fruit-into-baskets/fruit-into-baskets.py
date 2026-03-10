class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq={}
        left=0
        ans=0
        for i in range(len(fruits)):
            if fruits[i] in freq:
                freq[fruits[i]]+=1
            else:
                freq[fruits[i]]=1
            while len(freq)>2:
                freq[fruits[left]]-=1
                if freq[fruits[left]]==0:
                    del freq[fruits[left]]
                left+=1
            ans = max(ans, i - left + 1)
        return ans
           

        