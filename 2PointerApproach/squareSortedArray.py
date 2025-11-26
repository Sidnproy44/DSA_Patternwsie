"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Constraints:
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in non-decreasing order.

    Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
 
 Hint : [-4, -2, -1, 0, 3, 5] can be thought of as two sorted subarrays : [ -4, -2, -1 ] and [ 0, 3, 5 ]
        [16, 4, 1] (decreasing order) and [0, 9, 25] (increasing order) can be merged to get the final sorted array of squares.
        two pointers approach can be used to merge these two sorted arrays.
 """

def sortedSquares(nums):
        i=-1
        for num in nums:
            if num<0:
                i+=1
            else:
                break

        if i == -1:
            return [num*num for num in nums]            

        if i == len(nums)-1 :
            return [num*num for num in nums[::-1]]

        j=i+1
        nums= [num*num for num in nums]
        squaredNums = []
        while i>=0 and j<len(nums):
            if nums[i] < nums[j]:
                squaredNums.append(nums[i])
                i-=1
            elif nums[i]==nums[j]:
                squaredNums.extend([nums[i],nums[j]])
                i-=1
                j+=1
            else:
                squaredNums.append(nums[j])
                j+=1  

        while i>=0:
            squaredNums.append(nums[i])
            i-=1

        while j < len(nums):
            squaredNums.append(nums[j])
            j+=1             

        return squaredNums         

 
if __name__ == "__main__":
    nums = [-7, -3, 2, 3, 11]
    result = sortedSquares(nums)
    print(f"The sorted array of squares is: {result}")
