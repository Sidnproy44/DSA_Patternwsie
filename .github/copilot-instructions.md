# Copilot Instructions for 2-Pointer Project

## Project Overview
This is a Python implementation of two-pointer algorithm problems, starting with the Two Sum challenge. The project focuses on practicing efficient algorithmic solutions using the two-pointer technique.

## Code Structure
- **`twoSum.py`**: Core implementation file for two-pointer algorithm solutions

## Two-Pointer Algorithm Pattern
When implementing two-pointer solutions:
1. **Input handling**: Accept sorted or unsorted arrays and a target value
2. **Pointer initialization**: Start with pointers at opposite ends (left=0, right=len-1) for sorted arrays, or use hash-based approaches for unsorted
3. **Convergence logic**: Move pointers based on comparison with target:
   - If sum < target: increment left pointer
   - If sum > target: decrement right pointer
   - If sum == target: found solution
4. **Return format**: Return indices (0-indexed) as a list/tuple, or empty list if no solution found

## Key Constraints to Remember
- Time complexity target: O(n) for optimal solutions
- Space complexity: O(1) for two-pointer (sorted) approach, O(n) for hash-based (unsorted)
- Handle edge cases: empty arrays, single element, duplicate values, negative numbers

## Testing Approach
When adding test cases:
- Test basic case: `[2, 7, 11, 15], target=9` → `[0, 1]`
- Test edge cases: negative numbers, duplicates, no solution exists
- Validate both sorted and unsorted array handling if applicable
