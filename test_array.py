from povtor import *
import unittest


class TestMyFuckingProgram(unittest.TestCase):
    def test_array_search1(self):
        lst1 = [1, 2, 3, 4, 5]
        assert array_search(lst1, 8) == -1


    def test_array_search2(self):
        lst2 = [-1, -2, -3, -4, -5]
        assert array_search(lst2, -3) == 2


    def test_array_search3(self):
        lst3 = [10, 20, 30, 10, 10]
        assert array_search(lst3, 10) == 0


    def test_invert_array1(self):
        lst1 = [1, 2, 3, 4, 5]
        assert invert_array(lst1) == [5, 4, 3, 2, 1]


    def test_invert_array2(self):
        lst2 = [0, 0, 0, 0, 10]
        assert invert_array(lst2) == [10, 0, 0, 0, 0]


    def test_left_shift(self):
        lst1 = [0, 1, 2, 3, 4]
        assert left_shift(lst1, 5) == [1, 2, 3, 4, 0]


    def test_right_shift(self):
        lst1 = [1, 2, 3, 4, 0]
        assert right_shift(lst1, 5) == [0, 1, 2, 3, 4]


    def test_fib(self):
        n = 3
        assert fib(n) == 2


    def test_eratosfen(self):
        n = 10
        assert eratosfen(n) == ['0-составное',
                                '1-составное',
                                '2-простое',
                                '3-простое',
                                '4-составное',
                                '5-простое',
                                '6-составное',
                                '7-простое',
                                '8-составное',
                                '9-составное']


    def test_stek_skobka1(self):
        s = '{([])}'
        assert stek_skobka(s) == 'Yes'


    def test_stek_skobka2(self):
        s = '{([)]}'
        assert stek_skobka(s) == 'No'


    def test_insert_sort(self):
        s = [5, 4, 3, 2, 1]
        assert insert_sort(s) == [1, 2, 3, 4, 5]


    def test_insert_sort2(self):
        s = [5, 4, 3, 2, 1, -3]
        assert insert_sort2(s) == [-3, 1, 2, 3, 4, 5]


    def test_choise_sort(self):
        s = [5, 4, 3, 2, 1]
        assert choise_sort(s) == [1, 2, 3, 4, 5]


    def test_bubble_sort(self):
        s = [5, 4, 3, 2, 1]
        assert bubble_sort(s) == [1, 2, 3, 4, 5]


    def test_numer_digit(self):
        n = 4567
        assert numer_digit(n) == [7, 6, 5, 4]


    def test_numer_digit2(self):
        n = 4567
        assert numer_digit2(n) == [4, 5, 6, 7]


    def test_marge_sort(self):
        s = [5, 4, 3, 2, 1]
        assert marge_sort(s) == [1, 2, 3, 4, 5]


    def test_hoar_sort(self):
        s = [5, 4, 3, 2, 1]
        assert hoar_sort(s) == [1, 2, 3, 4, 5]


    def test_left_bourdary(self):
        s = [1, 3, 3, 6, 7, 9]
        assert left_bourdary(s, 3) == 0


    def test_right_bourdary(self):
        s = [1, 3, 3, 6, 7, 9]
        assert right_bourdary(s, 3) == 3