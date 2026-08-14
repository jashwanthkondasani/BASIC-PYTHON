# name="jashwanth"
# count=0
# for ch in name:
#   count+=1
# print(count)
# count=0
# name="jashwanth"
# vowels="aeiou"
# count=0
# for ch in name:
#   if ch in vowels:
#     count+=1
# print(count)
# name="KONDASANI JAShwanth kumar reddy"
# upper_count=0
# lower_count=0
# for ch in name:
#   if upper_count in name:
#      upper_count+=1
#   else:
#      lower_count+=1
# print("uppercase letters",upper_count)
# print("lowercase letters",lower_count)
# name="KondaSaniJashwanthKumarReddy"
# upper_count=0
# lower_count=0
# for ch in name:
#   if ch.isupper():
#     upper_count+=1
#   else:
#     lower_count+=1
# print("upperletters",upper_count)
# print("lower_count",lower_count)
# nums=[10,20,30,40,50]
# maximum=nums[0]
# for num in nums:
#    if num>maximum:
#       maximum=num
# print(maximum)
# nums=[1,2,4,66,3,1,0]
# minimum=nums[0]
# for num in nums:
#   if num<minimum:
#     minimum=num
# print(minimum)
# name="ammananna"
# print(name.upper())
# print(name.lower())
# print(name.title())
# name="123nanna"
# print(name.capitalize())  
# print(name.isalpha())
# print(name.isalnum())
# name="jashKONDASASNI"
# upper_count=0
# lower_count=0
# for ch in name:
#   if ch.isupper():
#     upper_count+=1
#   else:
#     lower_count+=1
# print("uppercount",upper_count)
# print("lowercount",lower_count)
# name="jashwanth kumar reddy"
# count=0
# vowels="aeiouAEIOU"
# for ch in name:
#   if ch !=vowels:
#     count+=1
# print(count)
# text="cook"
# reverse=""
# for ch in text:
#   reverse=ch+reverse
# if text==reverse:
#   print("it was an palinrome")
# else:
# #   print("not an plainrome ")
# def greet():
#   print("namste")
# print("hello")
# greet()
# print("gud byeee")
# def reverse_string(text):
#     reverse = ""
#     for ch in text:
#         reverse = ch + reverse
#     return reverse
# text=input()
# print(reverse_string(text))
# def reverse(s):
#   left=0
#   right=len(s)-1
#   while left<right:
#     s[left],s[right]=s[right],s[left]
#     left+=1
#     right-=1
# s=input()
# print(reverse(s))
# name="jashwanth kumar redddy"
# freq={}
# for ch in name:
#   if ch in freq:
#     freq[ch]+=1
#   else:
#     freq[ch]=1
#   print(ch,":",freq[ch],end=" ")
# name="jashwanthreddy"
# frequency={}
# for ch in name:
#   frequency[name]=frequency.get(ch,0)+1
# for ch in name:
#   print(ch,":",frequency[name])
text = "banana"

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

most_frequent = ""
highest = 0

for ch, count in freq.items():
    if count > highest:
        highest = count
        most_frequent = ch

print("Most frequent:", most_frequent)
print("Frequency:", highest)