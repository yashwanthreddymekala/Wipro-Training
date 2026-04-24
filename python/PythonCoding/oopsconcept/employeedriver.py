#driver
from oopsconcept.EmployeeDetails import EmployeeDetails

eno=int(input('emp no:'))
name=input('emp name:')
bp=float(input('basic pay:'))
employee=EmployeeDetails(empno=eno,ename=name,basicpay=bp)
print('emp no:',employee.empno)
print('emp name:',employee.ename)
print('basic pay:',employee.basic_pay)
print('salary:',employee.calu)
