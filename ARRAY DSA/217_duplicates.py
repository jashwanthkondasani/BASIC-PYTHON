# nums=[1,2,3,4,2]
# l=0
# r=1
# while r<len(nums):
#   if nums[l]==nums[r]:
#     print(True)
#     break
#   l+=1
#   r+=1
# else:
#   print(False)
# class Solution:
#     def containsDuplicate(self,nums):

#       nums.sort()
#       for i in range(len(nums)-1):
#          if nums[i]==nums[i+1]:
#             return True
#       return False
# s=Solution()
# print(s.containsDuplicate([1,2,3,4,2,2,1]))