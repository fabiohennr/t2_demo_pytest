# Como fazer casos de teste usando framework

#Seperar arquivos de programa dos arquivos de testes
#No Google: name conversion pytest

import pytest
from calculator import Calculator #from calculator import * # or add, subtract, multiply, divide

class TestCalculator():
    # def test_aux_function(): #def test_aux_function(): #não reconhece o teste
    #     pass

    sanityOnly = True

    def setup_class(self):
        print("\nIniciando setup...") # Print aqui é lixo! pytest -s -v (só imprime forçando)
        self.calc = Calculator()

    def teardown_class(self):
        print("\nIniciando teardown...") # Print aqui é lixo! pytest -s -v (só imprime forçando)
        self.calc = Calculator()

    def setup_method(self, method):
        print("\nCleanup do teste...")

    def test_add(self):
        assert self.calc.add(2, 3) == 5

    @pytest.mark.skip(reason="Duplicated by Heitor")
    def test_add_2(self):
        assert self.calc.add(2, 3) == 5

    @pytest.mark.skipif(sanityOnly, reason="Sanity test suite")
    def test_subtract(self):
        assert self.calc.subtract(1, 3) == -2

    @pytest.mark.parametrize(
            ("a", "b", "expected"),
            [(2, 4, 8),
            (3, 3, 9),
            (1, 7, 7)]
        )
    def test_multiply_generic(self, a, b, expected):
        assert self.calc.multiply(a, b) == expected

    def test_divide(self):
        assert self.calc.divide(10, 2) == 5

    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.divide(5, 0)


# # Como fazer casos de teste usando framework

# #Seperar arquivos de programa dos arquivos de testes
# #No Google: name conversion pytest

# import pytest
# from calculator import Calculator #from calculator import * # or add, subtract, multiply, divide

# class TestCalculator():
#     # def test_aux_function(): #def test_aux_function(): #não reconhece o teste
#     #     pass

#     sanityOnly = True

#     def setup_class(self):
#         print("\nIniciando setup...") # Print aqui é lixo! pytest -s -v (só imprime forçando)
#         self.calc = Calculator()

#     def teardown_class(self):
#         print("\nIniciando teardown...") # Print aqui é lixo! pytest -s -v (só imprime forçando)
#         self.calc = Calculator()

#     def setup_method(self, method):
#         print("\nCleanup do teste...")

#     def test_add(self):
#         assert self.calc.add(2, 3) == 5

#     @pytest.mark.skip(reason="Duplicated by Heitor")
#     def test_add_2(self):
#         assert self.calc.add(2, 3) == 5

#     @pytest.mark.skipif(sanityOnly, reason="Sanity test suite")
#     def test_subtract(self):
#         assert self.calc.subtract(1, 3) == -2

#     def test_multiply(self):
#         assert self.calc.multiply(2, 3) == 6

#     def test_divide(self):
#         assert self.calc.divide(10, 2) == 5

#     def test_divide_by_zero(self):
#         with pytest.raises(ZeroDivisionError):
#             self.calc.divide(5, 0)




# # Como fazer casos de teste usando framework

# #Seperar arquivos de programa dos arquivos de testes
# #No Google: name conversion pytest

# import pytest
# from calculator import Calculator #from calculator import * # or add, subtract, multiply, divide

# class TestCalculator():
#     # def test_aux_function(): #def test_aux_function(): #não reconhece o teste
#     #     pass

#     def setup_class(self):
#         print("\nIniciando setup...") # Print aqui é lixo! pytest -s -v (só imprime forçando)
#         self.calc = Calculator()

#     def teardown_class(self):
#         print("\nIniciando teardown...") # Print aqui é lixo! pytest -s -v (só imprime forçando)
#         self.calc = Calculator()

#     def test_add(self):
#         #assert add(2, 3) == 7, "Expect was 5, but received {}".format(add(2, 3))
#         #assert add(2, 3) == 5
#         #self.calc = Calculator()
#         assert self.calc.add(2, 3) == 5

#     def test_subtract(self):
#         #self.calc = Calculator()
#         assert self.calc.subtract(1, 3) == -2

#     def test_multiply(self):
#         #self.calc = Calculator()
#         assert self.calc.multiply(2, 3) == 6

#     def test_divide(self):
#         #self.calc = Calculator()
#         assert self.calc.divide(10, 2) == 5

#     def test_divide_by_zero(self):
#         #self.calc = Calculator()
#         with pytest.raises(ZeroDivisionError):
#             self.calc.divide(5, 0)