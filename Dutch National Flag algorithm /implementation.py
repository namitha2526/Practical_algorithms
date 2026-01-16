def sortZeroOneTwo(self, nums):
        # Initialize three pointers: low and mid at 0, high at end
        low, mid, high = 0, 0, len(nums) - 1

        # Traverse until mid crosses high
        while mid <= high:
            # If element is 0, swap with low, move both low and mid forward
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            # If element is 1, just move mid forward
            elif nums[mid] == 1:
                mid += 1
            # If element is 2, swap with high, move only high backward
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

# Driver code
nums = [2, 0, 2, 1, 1, 0]
obj = Solution()
obj.sortZeroOneTwo(nums)
print(nums)
