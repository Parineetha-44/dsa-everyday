class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        one = set(nums)

        two = set()
        for x in one:
            for v in nums:
                two.add(x ^ v)

        three = set()
        for x in two:
            for v in nums:
                three.add(x ^ v)

        return len(three)