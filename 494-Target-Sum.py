class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # self.total_ways = 0

        # def calculate_ways(nums,curr_index,curr_sum,target):
        #     if curr_index == len(nums):
        #         if curr_sum == target:
        #             self.total_ways += 1
        #     else:
        #         calculate_ways(nums,curr_index+1,curr_sum+nums[curr_index],target)
        #         calculate_ways(nums,curr_index+1,curr_sum-nums[curr_index],target)
        
        # calculate_ways(nums,0,0,target)

        # return self.total_ways

        
        total_sum = sum(nums)
        dp = [[0] * (2 * total_sum + 1) for _ in range(len(nums))]

        # Initialize the first row of the DP table
        dp[0][nums[0] + total_sum] = 1
        dp[0][-nums[0] + total_sum] += 1

        # Fill the DP table
        for index in range(1, len(nums)):
            for sum_val in range(-total_sum, total_sum + 1):
                if dp[index - 1][sum_val + total_sum] > 0:
                    dp[index][sum_val + nums[index] + total_sum] += dp[
                        index - 1
                    ][sum_val + total_sum]
                    dp[index][sum_val - nums[index] + total_sum] += dp[
                        index - 1
                    ][sum_val + total_sum]

        # Return the result if the target is within the valid range
        return (
            0
            if abs(target) > total_sum
            else dp[len(nums) - 1][target + total_sum]
        )

        