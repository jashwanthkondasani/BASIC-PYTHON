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
# def sort(nums):
#   for i in range(len(nums)-1):
#       if nums[i]>nums[i+1]:
#           return False
#   return True
# print(sort([11,1,2,4]))
# nums=[11,22,44,55,-1,-33,-44]
# count=0
# for num in nums:
#   if num>0:
#     count+=1
# print("count",count)
        # print(num)
# nums=[11,22,-22,-34]
# for num in nums:
#   if num>=0:
#     print(num)

# def is_sorted(nums):
#   for i in range(len(nums)-1):
#     if nums[i]>nums[i+1]:
#       return False
#   return True
# nums=[11,22,33,44,55]
# print(is_sorted(nums))
# nums=[11,22,33,55,22,22]
# count=0
# target=22
# for num in nums:
#   if num==target  :
#     count+=1
# print("target:-",target,"count:-",count)
# nums=[11,22,33,44,44,44,44]
# freq={}
# for num in nums:
#   if num in freq:
#     freq[num]+=1
#   else:
#     freq[num]=1
# print(freq)
# nums = [10, 50, 20, 80, 30]

# max_value = nums[0]
# max_index = 0

# for i in range(len(nums)):
#     if nums[i] > max_value:
#         max_value = nums[i]
#         max_index = i

# print(max_value)
# print(max_index)
# arr=[21,22,33,44,55]
# target=22
# found=False
# for num in arr:
#   if num==target:
#     found=True
#     break
# print(found)
# nums=[11,22,33,44,44,44]
# target=44
# count=0
# for num in nums:
#   if num==target:
#     count+=1
# print(count)
# nums=[11,22,33,44,55]
# even=0
# odd=0
# for num in nums:
#   if num%2==0:
#     even+=1
#   else:
#     odd+=1
# print("even count:-",even)
# print("odd_count:-",odd)