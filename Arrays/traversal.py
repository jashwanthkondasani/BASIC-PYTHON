# nums=[1,2,33,44,555,666]
# for i in range(len(nums)):
#     print(nums[i])
# nums=[11,22,44,55,66,77,88]
# sum=0
# for i in range(len(nums)):
#     sum+=nums[i]
# print(sum)
# nums=[11,33,44,55,77]
# total=1
# for i in range(len(nums)):
#   total*=nums[i]
# print(total)
# def sum(nums):
#   total=0
#   for i in range(len(nums)):
#     total+=nums[i]
#   print(total)
# sum([11,22,33])
# nums=[11,22,33,44]
# for i in range(len(nums)):
#   print(nums[i])
# nums=[1,2,3,4,5,6,7]
# total=0
# for i in range(len(nums)):
#   total+=nums[i]
# average=total/len(nums)
# print(average)
# nums=[11,22,33]
# largest=-1
# second=-1
# for i in range(len(nums)):
#   if largest>second:
#     second=largest
#     second=largest
#   if largest >second:
#     second=largest
# print(second)
# nums=[11,22,44,22,33,444]
# largest=nums[0]
# second=-1
# for i in range(len(nums)):
#   if nums[i]>largest:
#       second=largest
#       largest=nums[i]
#   elif nums[i]>second and nums[i]!=largest:
#       second=nums[i]
# print(largest)
# print(second)
# nums=[11,3,4,66,56789]
# largest=nums[0]
# second=-1
# for i in range(len(nums)):
#   if nums[i]>largest:
#     second=largest
#     largest=nums[i]
#   elif second>nums[i] and second!=largest:
#     second=nums[i]
# print(largest)
# print(second)
# nums=[1,22,44,55,22,-1,-1234]
# lowest=nums[0]
# second=0
# for i in range(len(nums)):
#   if nums[i]<lowest:
#     second=lowest
#     lowest=nums[i]
#   elif second<nums[i] and second!=lowest:
#     second=nums[i]
# print(lowest)
# print(second)
# nums=[11,22,44,55]
def sort(nums):
  for i in range(len(nums)-1):
      if nums[i]>nums[i+1]:
          return False
  return True
print(sort([11,1,2,4]))

