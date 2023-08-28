class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # selection sort

        for i in range(len(nums)):
            small = nums[i]
            minIndex = i

            for j in range(i+1, len(nums)):
                if nums[j] < small:
                    small = nums[j]
                    minIndex = j
            
            if minIndex != i:
                nums[i], nums[minIndex] = nums[minIndex], nums[i]
        return nums
