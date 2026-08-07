# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]

def numSubarraysWithSum(nums, goal):
    if goal == 0:
        return count_subarrays(nums)
    count = 0
    left = 0
    total_sum = 0
    
    for right in range(len(nums)):
        total_sum = nums[right]
        while left <= right and total_sum > goal:
            total_sum 
    return None


def count_subarrays(arr):
    n = len(arr)
    return n * (n + 1) // 2
