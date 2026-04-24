'''# Ask the user for their age
age = int(input("Enter your age: "))

# Check if the user is eligible to vote
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")'''



'''year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")'''


'''number = int(input("Enter a number: "))

# Check divisibility by 5
if number % 5 == 0:
    print(f"{number} is divisible by 5.")
else:
    print(f"{number} is not divisible by 5.")'''


'''char = input("Enter a character: ").lower()

# Check if it's a vowel or consonant
if char in "aeiou":
    print(char, "is a vowel.")
else:
    print(char, "is a consonant.")'''


'''password = input("Enter your password: ")

if len(password) >= 8:
    print("Your password is strong.")
else:
    print("Your password is too short. It should be at least 8 characters.")'''

'''
grade = input("Enter your grade (A, B, C, D, F): ").upper()

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case "D":
        print("Below Average")
    case "F":
        print("Fail")
    case _:
        print("Invalid grade entered")'''



'''color = input("Enter traffic light color (Red, Yellow, Green): ").capitalize()

match color:
    case "Red":
        print("Stop")
    case "Yellow":
        print("Wait")
    case "Green":
        print("Go")
    case _:
        print("Invalid color entered")'''



'''num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is {factorial}.")'''

'''

for number in range(1, 21):
    if number % 2 == 0:
        print(number)'''



'''count = 10

while count >= 0:
    print(count)
    count -= 1'''



'''text = input("Enter a string: ").lower()

vowel_count = 0

for char in text:
    if char in "aeiou":
        vowel_count += 1

print(f"The number of vowels in the string is: {vowel_count}")'''



for number in range(1, 11):
    if number == 5:
        continue
    if number == 8:
        break
    print(number)