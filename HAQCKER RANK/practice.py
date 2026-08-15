# def leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     return False
# n=int(input())
# arr=map(int,input().split())
# arr1=list(arr)
# arr1=list(set(arr1))
# arr1.sort()
# print(arr1[-2])
def runnerup(arr):
    arr1=list(arr)
    arr1=list(set(arr1))
    arr1.sort()
    return arr1[-2]
