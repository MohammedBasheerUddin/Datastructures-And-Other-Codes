#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        num = num1 + num2   # merge both array into one
        num.sort()          # sort the new array
        mid = len(num)      # find length of new array
        if mid % 2 == 0:    # check if length is even or odd 
            mid = mid // 2  # if even calculate middle element
            return (num[mid-1] + num[mid]) / 2 # return the median for even length like (2 + 3) / 2
        else:
            return num[mid // 2] + 0.0 # return median for odd length, such as if array is [1,2,3] median will be 2 directly        
