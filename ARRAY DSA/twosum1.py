# nums=[2,7,11,15]
# l=1
# r=-1
# target=13
# for i in range(len(nums)):
#    if nums[l]+nums[r]==target:
#       l+=1
#       r+=1
# print(l,r)
# nums=[1,22,33,44]
# target=23
# l=0
# r=len(nums)-1
# while l<r:
#   total=nums[l]+nums[r]
#   if total==target:
#     print(l,r)
#     break
 
#   elif total<target:
#     l+=1

#   else:
#     r-=1
class solution:
  def twoSum(self,nums,target):
    for i in range(len(nums)):
      for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
          return [i,j]
s=solution()
print(s.twoSum([2,7,11,15],9))
# print(s.twoSum([1,22,33,44],23))
