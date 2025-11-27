# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# brutforce solution tc- O(n2) sc- (1)
# such types of flags only stored temporarily inside the loop iteration. it does not presists outside the loop
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # this is an output space and it's not counted in complexity
        result = []
        n = len(nums)
        # this loop is giving an index so we started from 1
        for i in range(1, n+1):
            flag = False
            # this loop is checking number with that index
            for j in range(n):
                if nums[j] == i:
                    flag = True
                    break
            # default flag = false condition
            if not flag:
                result.append(i)
        return result
solution =Solution()
print(solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
