class Solution:
  def BinarySearch(self,nums,target):
    l=0
    r=len(nums)-1

    while l<=r:
        mid=(l+r)//2
        if nums[mid]==target:
           return mid
     
        elif nums[mid]<target:
           l=mid+1
        else:
           r=mid-1
    return -1
s=Solution()
print(s.BinarySearch([1,2,4,5,6,7],5))