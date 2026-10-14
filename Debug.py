class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        left = 0 
        right = 0
        count = 0

        while left < len(nums):

            if nums[left] == nums [right] == k:
                count += 1
                left += 1
            elif nums[left] + nums [right] == k and left < right:
                count += 1
                left += 1
            elif right < len(nums) - 1:
                right += 1
            else:
                right = len(nums) - 1

        return count

if __name__ == "__main__":
    s = Solution()
    mat = s.subarraySum([1,2,3], 3)
    print(mat)