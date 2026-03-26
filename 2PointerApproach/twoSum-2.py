# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.


# Hint : for sorted array --->two pointer ,  for unsorted array ---> hash map

class Solution:
    def twoSum(self, numbers, target):
        left , right = 0 , len(numbers) -1

        while left < right :
            curr_sum = numbers[left] + numbers[right]
            if curr_sum== target:
                return [left, right]
            elif curr_sum < target:
                left+=1
            elif curr_sum > target:
                right-=1

        return None

testSubject1 = Solution()
test2 = Solution()

print(testSubject1.twoSum([1, 2 ,3, 4, 5], 6))                
print(test2.twoSum([2, 7, 11, 15], 9))                
