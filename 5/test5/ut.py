import correct as cs
import test_solution as ts
import data_generator as dg
import unittest

# Generate data
dg.main()


# run unittests
class TestSolutions(unittest.TestCase):
    """
    Тест задания #5
    test_soluton --- тестируется
    correct --- точно верное решение (но медленное)
    """

    def test_cases(self):
        self.assertEqual(cs.main(), ts.main())


if __name__ == '__main__':
    unittest.main()
