#biggest of two numbers
'''
num1=int(input("enter a number:"))
num2=int(input("enter another number:"))

if num1==num2:
    print("both are equal")
elif num1>num2:
    print(num1, " is greater")
else:
    print(num2, "is greater")
'''
#biggest of three numbers
'''num1=int(input("enter a number:"))
num2=int(input("enter another number:"))
num3=int(input("enter another number:"))

if num1==num2 and num2==num3:
    print("all values are equal")
elif num1>num2 and num1>num3:
    print(num1,"num1 is greater")
elif num2>num1 and num2>num3:
    print(num2, "num2 is greater")
elif num3>num1 and num3>num2:
    print(num3,"num3 is greater")
'''
#weekday
choice=int(input("enter a number btw 1-7:"))
match choice:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case _:
        print("invalid choice")
