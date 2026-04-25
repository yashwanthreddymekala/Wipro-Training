'''class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        # Private instance variables
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    # Getter methods
    def get_account_number(self):
        return self.__account_number

    def get_account_holder(self):
        return self.__account_holder

    def get_balance(self):
        return self.__balance

    # Setter methods
    def set_account_number(self, account_number):
        self.__account_number = account_number

    def set_account_holder(self, account_holder):
        self.__account_holder = account_holder

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative!")

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive!")

    # Withdraw method
    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.__balance}")
            else:
                print("Insufficient balance!")
        else:
            print("Withdrawal amount must be positive!")

    # Method to display account information
    def display_account_info(self):
        print("----- Account Information -----")
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder: {self.__account_holder}")
        print(f"Balance: ${self.__balance}")
        print("-------------------------------")


# Demonstrating functionality
if __name__ == "__main__":
    # Creating bank account instances
    account1 = BankAccount("123456", "Alice", 1000)
    account2 = BankAccount("654321", "Bob", 500)

    # Display initial account info
    account1.display_account_info()
    account2.display_account_info()

    # Deposit money
    account1.deposit(200)
    account2.deposit(300)

    # Withdraw money
    account1.withdraw(150)
    account2.withdraw(1000)  # Should show insufficient balance

    # Update account info
    account1.set_account_holder("Alice Johnson")
    account1.display_account_info()'''





class Employee:
    def __init__(self, emp_id, name, salary):
        # Private instance variables
        self.__emp_id = emp_id
        self.__name = name
        self.__salary = salary

    # Getter methods
    def get_emp_id(self):
        return self.__emp_id

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    # Setter methods
    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    def set_name(self, name):
        self.__name = name

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative!")

    # Display employee information
    def display_info(self):
        print("----- Employee Information -----")
        print(f"Employee ID: {self.__emp_id}")
        print(f"Name: {self.__name}")
        print(f"Salary: ${self.__salary:.2f}")
        print("-------------------------------")

    # Method to give salary hike
    def give_hike(self, percentage):
        if percentage > 0:
            increment = self.__salary * (percentage / 100)
            self.__salary += increment
            print(f"Salary increased by {percentage}%. New salary: ${self.__salary:.2f}")
        else:
            print("Percentage must be positive!")


# Demonstration of functionality
if __name__ == "__main__":
    # Creating employee instances
    emp1 = Employee("E001", "John Doe", 50000)
    emp2 = Employee("E002", "Jane Smith", 60000)

    # Display initial information
    emp1.display_info()
    emp2.display_info()

    # Give salary hikes
    emp1.give_hike(10)  # 10% hike
    emp2.give_hike(5)   # 5% hike

    # Display updated information
    emp1.display_info()
    emp2.display_info()