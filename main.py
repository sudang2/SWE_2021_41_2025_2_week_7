from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    count=len(nums)
    
    for i in range(count):
        for j in range(i+1,count):
            if nums[i]+nums[j]==target:
                return [i,j]
    return 0