#functions
'''def add(n1,n2):
    sum=n1+n2
    return sum

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2




#driver
num1=int(input("enter a number:"))
num2=int(input("enter another number:"))
res=mul(num1,num2)
print('mul',res)
'''
#Arbitary
'''def add(*nums):
    sum=0
    for n in nums:
        sum+=n
    return sum
print(add(6,7,8))
print(add(6,7,8,55,6))
'''
#lambda function
'''num1=int(input("enter a number:"))
num2=int(input("enter another number:"))

add=lambda n1,n2: n1+n2
print(add(num1,num2))'''

numbers=[1,2,3,4,5]

sq=lambda nums:[num*num for num in nums if num%2==0]
print(sq(numbers))