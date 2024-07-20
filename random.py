
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(nums):
            if(i!=i+1):
                return false
        
        return true