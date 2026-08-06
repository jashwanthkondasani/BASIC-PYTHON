# arr=[11,22,33,44,55]
# for num in range(len(arr)):
  # print(arr[num]
# sum=0
# arr=[11,22,33,44,55]
# for i in range(len(arr)):
#   sum+=arr[i]
# print(sum)

# arr=[11,22,300]
# largest=arr[0]
# for i in range(len(arr)):
#   if arr[i]>largest:
#     largest=arr[i]
# print(largest)
nums=[122,44,55]
largest=0
second=0
for i in  range(len(nums)):
  if nums[i]>largest:
    second=largest
    largest=nums[i]
  if nums[i]>second or second!=largest:

    print(second)