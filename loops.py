# while loop

# count=1
# while count<=5:
#     print("jaisriram")
#     count+=2
# count=5
# while count>=1:
#     print("jaisriram")
#     count-=2

# count=1
# while count<=20:
#     print("jaisriram")
#     count*=2
# count=1
# while count<=3:
#   print("jaisriram")
#   count+=1
# count=5
# while count>=1:
#     print(count)
#     count-=2
# count=100
# while count>=10:
#   print(count)
#   count=count//2
# x=1
# y=5
# while x<=5:
#   print(x,y)
#   x+=1
#   y-=1
# attempt=1
# while attempt<=3:
#   print("login attempt",attempt)
#   attempt+=1
# print("Account locked")
# table=7
# i=1
# while i <=10:
#   print(table,"x",i,"=",table*i)
#   i+=1
# x,y,z=map(int,input("enter three numbers:-").split())
# if x==y and x==z and y==x and y==z and z==x and z==y:
#   print("all numbers are equal")
# elif x!=y and x!=z and y!=x and y!=z and z!=x and z!=y:
#   print("all numbers are different")
# else:
#    print("two numbers are equal")
# i=int(input("enter a number:-"))
# j=int(input("enter a number:-"))
# print(i,"X",j,"=",i*j)
# n=1
# while n<=5:
#     print("jaisriram")
#     n+=1
# count=1
# while count<=5:
#     print("jaisriram")
#     count+=1

#  for loop --------
# for i in range(1,6):
#     print("jaisriram")
# for i in range(5):
#     print("jaisriram")
# for i in range(1,11):
#   print(i)
# for i in range(10,0,-1):
#    print(i)
# for  i in range(1,11):
#     if i%2==0:
#         print(i,"is even")
#     else:
#         print(i,"is odd")
# sum=0
# for i in range(1,11):
#     sum+=i
# print(sum)fac
# fact=1
# for i in range(1,6):
#   fact*=i
# print(fact)
# for i in range(1,6):
#    if i%2==0:
#        print(i,"is even")
#    else:
#        print(i,"is odd")
# for i in range(1,11):
#     if i%2==0:
#         print(i,"is even")
#     else:
#         print(i,"is odd")
# even_sum=0
# odd_sum=0
# for i in range(1,11):
#     if i%2==0:
#         even_sum+=i
#     else:
#         odd_sum+=i
# print("Sum of even numbers:",even_sum)
# print("Sum of odd numbers:",odd_sum)
# sum=0
# for i in range(1,15):
#   if i%7==0:
#     sum+=i
# print(sum)

# count=0
# sum=0
# for i in range(1,200):
#   if i%5==0:
#     sum+=i
#     print(i)
#     count+=1
# print("sum",sum)
# print("count",count)
# for i in range(1,10):
#   if i==7:
#     break
#   print(i)
# for i in range(1,15):
#   if i==7:
#     continue
#   print(i)

# for i in range(1, 16):
#     if i % 15 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
# n=123243243
# count=0
# while n>0:
#   digit=n%10
#   count+=1
#   n//=10
# print(count)
# num=123
# rev=0
# while num>0:
#   digit=num%10
#   rev=rev*10+digit
#   num//=10
# print(rev)
# n=100323289787
# largest=0
# while n>0:
#   digit=n%10
#   if digit>largest:
#       largest=digit
#   n//=10
# print(largest)
# n=23242
# smallest=0
# while n>0:
#   digit=n%10
#   if digit<smallest:
#     smallest=digit
#   n//=10
# print(smallest)
# n=7
# count=0
# for i in range(1,n+1):
#   if n%i==0:
#     count+=1
# if count==2:
#   print("prime")
# else:
#   print("not a prime")
# for num in range(1,1000):
#   count=0
#   for i in range(1,num+1):
#     if num%i==0:
#       count+=1
#   if count==2:
#     print(num,end=" ")
# n=153
# original=n
# total=0
# while n>0:
#   digit=n%10
#   total+=digit**3
#   n//=10
# if original==total:
#   print("armstrong number")
# else:
#   print("not an armstrong number ")
