/* 
find peak element such that the target element is greater than its neighbours
arr = [1,2,1,3,5,6,4]       output must be index of 2 or 6
*/



class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        left , right = 0 , len(arr) -1

        while left < right:
            mid = (left + right) // 2

            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left
