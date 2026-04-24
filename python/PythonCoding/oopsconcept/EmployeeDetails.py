class EmployeeDetails:
    def __init__(self,empno,ename,basicpay):
        self.empno=empno
        self.__ename=ename
        self.basic_pay=basicpay
        self.da=20.0
        self.hra=10.0
        self.pf=5.5

    @property
    def ename(self):
        return self.__ename
    @ename.setter
    def ename(self,en):
        self.__ename=en


    def calculate_allowance(self):

