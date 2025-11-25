"""Given an array of integers nums and an integer target, return the two numbers such that they add up to target"""




def two_sum(nums, target):
    i, j = 0, len(nums) - 1
    nums.sort()
    while i < j:
        if nums[i] + nums[j] == target:
            return [nums[i], nums[j]]
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1
    return []  # Return an empty list if no pair is found


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 13
    result = two_sum(nums, target)
    print(f"The two numbers that add up to {target} are: {result}")