"""Given an array of integers nums and an integer target, return the two numbers such that they add up to target"""

# given array is not sorted, hence use hashmap approach

class Solution:
    def twoSum(self, arr, target):
        map = {}
#         For each element:
#         Compute target - num
#         Check if it exists in map
#         If yes → return indices
#         Else store current number
        for i, num in enumerate(arr):
            diff = target-num
            if diff in map:
                return [map[diff],i]
            else: 
                map[num] = i

        return None        

test1 = Solution()
print(test1.twoSum([1,3,2,5,4] , 6))
