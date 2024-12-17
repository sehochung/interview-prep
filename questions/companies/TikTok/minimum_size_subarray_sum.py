'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
'''

def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        N = len(nums)
        min_length = float('inf')
        left = 0
        current_sum = 0

        # iterate through each number
        for right in range(N):
            # Adding each number until current_sum is greater or equal to target
            current_sum += nums[right]
            # Making window smaller from the left until current_sum is less than target
            while current_sum >= target:
                # getting minimum length of window. right-left+1 represents current window
                min_length = min(right-left+1, min_length)
                # subtract most-left element when making window smaller from the left
                current_sum -= nums[left]
                # moving left pointer to the right by 1
                left+=1

        return min_length if min_length != float('inf') else 0
