from src.calculations import calculations


class Testcalc:
    calc=calculations()

    def test_area_of_square(self):
        res=self.calc.area_of_square(10)
        assert res==100,'area error'

    def test_peri_of_square(self):
        res = self.calc.peri_of_square(5,10)
        assert res == 30, 'peri error'
