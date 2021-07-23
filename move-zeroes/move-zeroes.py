class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        n = len(nums);
        for num in nums:        # this loop shifts all values > 0 to 1st,2nd.... positions
            if(num != 0):        # j variable helps in assigning >0 values to the respective positions  
                nums[j] = num   # and it also keeps count of no. values > 0
                j += 1
                
        for i in range(j, n):  # this loop assigns value = 0 to remaining cells
            nums[i] = 0