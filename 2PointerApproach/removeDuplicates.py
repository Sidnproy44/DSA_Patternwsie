""" Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored."""

def remove_duplicates(nums : list[int]):
    i, j= 0, 1
    if len(nums)==0:
        return 0
    while j < len(nums):
        if nums[j] in nums[0:i+1]:
            j+=1
        else:
            i+=1
            nums[i]=nums[j]
            j+=1

    return i+1 , nums[0:i+1]

if __name__== "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    k , unique_nums= remove_duplicates(nums)
    print(f"The number of unique elements is {k} and the array with unique elements is {unique_nums}")         

