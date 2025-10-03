class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        pari=[]
        for b in asteroids:
            while  pari and b<0 and pari[-1]>0:
                if pari[-1]<-b:
                    pari.pop()
                    continue
                elif pari[-1]==-b:
                    pari.pop()
                break
            else:
                pari.append(b)
        return pari

        