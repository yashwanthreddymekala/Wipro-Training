import pytest

from src.calculations import calculations

class TestCalculations:
    calc=calculations()

    @pytest.fixture(scope='module',autouse=True)
    def setup(self):
        print('fixture')
        
    def test_add(self):
        res=self.calc.add(10,5)
        assert res == 15,'Addition error'


    def test_sub(self):
        res=self.calc.sub(10,5)
        assert res == 5,'subtraction error'


    def test_mul(self):
        res=self.calc.mul(10,5)
        assert res == 50,'multiplication error'


    def test_div(self):
        res=self.calc.div(10,5)
        assert res == 2.0,'division error'

    def test_ne(self):
        res=self.calc.ne(10,10)
        assert res == True,'Not Equal'

    def test_diverr(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(10,0)


