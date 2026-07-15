class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        def p(t):
            h,m,s= map(int, t.split(":"))
            return h*3600+m*60+s
        return p(endTime)-p(startTime)
