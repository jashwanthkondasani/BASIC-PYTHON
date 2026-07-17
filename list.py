# list creating 
# movies=["rrr","kgf","bahubali"]
# indexing
# print(movies[0])
# print(movies[-1])
# # print(movies[2])
# marks=[1,2,3,4,5,6,7,8,9]
# print(marks[::-1])
# print(movies)
# slicing
# marks=[11,22,33,44,55,66,77]
# print(marks[1:3])
# print(marks[1:5:2])
# print(marks[3::1])
# print(marks[::-1])
# print(marks[2:2])
# using loops 
# names=["jash","nani","pandu"]
# for name in names:
#     print(name)
# names=["jash","nani","pandu"]
# for i in range(len(names)):
#     print(i,names[i])
# num=[1,2,3,4,5,6,7,8,9]
# for i in num:
#   if i%2==0:
#     print(i)
# marks=[11,22,33,44,55,66,77]
# total=0
# passed=0
# failed=0
# lowest=marks[0]
# highest=marks[0]
# for i in marks:
#   total+=i
#   if i>=highest:
#     highest=i
#   if i<=lowest:
#     lowest=i
#   if i>=35:
#     passed+=1
#   else:
#     failed+=1
# average=total/len(marks)
# print("total marks:",total)
# print("average marks:",average)
# print("highest marks:",highest)
# print("lowest marks:",lowest)
# print("number of students passed:",passed)
# print("number of students failed:",failed)
# num=[1,2,3,4,5,6,7,8,9]
# even=0
# odd=0
# for i in num:
#   if i%2==0:
#     even+=1
#   else:
#     odd+=1
# print("number of even numbers:",even)
# print("number of odd numbers:",odd)
# operations 
# 
# num=[1,2,3,4,5,6,7,8,9]
# num.append(10)
# print(num)
# num.insert(0,0)
# print(num)
# numbers.extend(11)
# print(num)
# list1=[1,2,3,4,5]
# list2=[6,7,8,9,10]
# list1.extend(list2)
# print(list1)
# list1=[1,2,3,4,5]
# list1.remove(3)
# print(list1)
# list=["apple","banana","cherry"]
# list.pop(1)
# print(list) 
# list1=[1,2,3,4,5]
# list1.clear()
# print(list1)
list1=[1,2,3,4,5 ]
del list1[1]
print(list1)