# def largest(num):
#   largest=num[0]
#   for i in range(1,len(num)):
#     if num[i]>largest:
#       largest=num[i]
#   return largest
# nums=[1,3,4,5,6]
# print(largest(nums))
def smallest(num):
  smallest=num[0]
  for i in range(1,len(num)):
    if num[i]<smallest:
      smallest=num[i]
  return smallest