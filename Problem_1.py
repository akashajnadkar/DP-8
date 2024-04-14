'''
Time Complexity - O(n)
Space Complexity - O(n)

Works on Leetcode
'''
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count = 0
        arr = [0] * len(nums) #initially number of slice are 0 for all elements
        for i in range(2,len(nums)):
            #if there are 3 consecutive elements with same diff we add 1 to the number of slices at previous element 
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                arr[i] = arr[i-1] + 1
                #add to total count
                count += arr[i]
        return count
        