class Solution(object):
    def removeElement(self, nums, val):
        
        l = len(nums)
        k = 0
        x = 0
        while x < l:
            if nums[x] == val:
                print("pop:", nums[x])
                nums.pop(x)
                l -= 1
            else:
                print("nums:", nums[x])
                x += 1
                k += 1

        print(nums)
        return k
