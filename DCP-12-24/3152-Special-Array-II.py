class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        special = [0]*len(nums)

        for i in range(len(nums)-1):
            if nums[i]%2 == nums[i+1]%2:
                special[i+1] = special[i]-1
            else:
                special[i+1] = special[i]+1

        result = []

        for x in queries:
            i = x[0]
            j = x[1]
            
            if j-i == special[j]-special[i]:
                result.append(True)
            else:
                result.append(False)
        return result


                
        