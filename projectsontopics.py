# print("--------------------------------------------------")
# print("WELCOME TO PYTHON LOGIN SYSTEM")
# print("--------------------------------------------------")
# username=input("enter user name:-")
# password=input("enter the passwor:-")
# if username=="admin" and password=="python@123":
#   print("login successfull \n welcome admin") 
# else:
#   print("sorry invalid credentials")
# num1=int(input("enter  the first number:-"))
# num2=int(input("enter the second number:-"))
# operator=input("enter the operator:-")
# if operator=="+":
#     print("addition of two numbers",num1+num2)
# elif operator=="-":
#     print("subraction of two numbers",num1-num2)
# elif operator=="*":
#     print("multiplication of two numbers",num1*num2)
# elif operator=="/":
#     print("division of two numbers",num1/num2)
# marks=int(input("enter the marks:-"))
# if 90<= marks <=100:
#   print("A grade")
# elif 70<= marks <=90:
#   print("Bgrade")

# grade system
# score=int(input("enter the score:-"))
# if 90<=score <=100:
#   print("excellent")
# else:
#   print("scores are not valid")
#  nested if 
# pin=1729
# balance=100000
# user_pin=int(input("enter your pin:-"))
# if user_pin==pin:
#     print("pin is correct")
#     withdrawl_amount=int(input("enter the amount to withdraw:-"))
#     if withdrawl_amount<=balance:
#         print("please collect your cash")
#     else:
#         print("insufficient balance")
# else:
#     print("invalid pin")
# pin=int(input("enter your pin:-"))
# balance=1000
# if pin==123:
#     amount=100
#     if amount<=balance:
#         print("please collect your cash\n thank u for choosing my bank ")
#     else:
#         print("insufficient balance")
# else:
#     print("invali pin")
salary=int(input("enter your salary:-"))
if salary>=40000:
  age=int(input("enter your age:-"))
  if age>=25:
        print("loan is approved")
        cibil_score=int(input("enter your cibil score:-"))
        if cibil_score>=700:
            print("congratulations! you are eligible for the loan")
        else:
            print("sorry you are not eligible for the loan")
  else:
        print("sorry loan is not approval")

else:
  print("sorry loan is not approval")
  

