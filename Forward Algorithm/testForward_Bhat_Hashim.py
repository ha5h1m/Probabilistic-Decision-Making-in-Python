import sys

sys.path.append('../src/')

import unittest
from ddt import ddt, data, unpack
import forward_Bhat_Hashim as targetCode  # change to file name


@ddt
class TestForward(unittest.TestCase):

    def assertNumericDictAlmostEqual(self, calculatedDictionary, expectedDictionary, places=7):
        self.assertEqual(calculatedDictionary.keys(), expectedDictionary.keys())
        for key in calculatedDictionary.keys():
            self.assertAlmostEqual(calculatedDictionary[key], expectedDictionary[key], places=places)

    @data(({0: 0.6, 1: 0.4}, 1, {0: {0: 0.2, 1: 0.8}, 1: {0: 0.7, 1: 0.3}},
           {0: {0: 0.2, 1: 0.2, 2: 0.6}, 1: {0: 0, 1: 0.8, 2: 0.2}}, {0: 0.14285714285714288,
                                                                      1: 0.8571428571428571}))  # (xT_1Distribution, eT, transitionTable, sensorTable, expectedResult)
    @unpack
    def test_forward(self, xT_1Distribution, eT, transitionTable, sensorTable, expectedResult):
        calculatedResult = targetCode.forward(xT_1Distribution, eT, transitionTable, sensorTable)

        self.assertNumericDictAlmostEqual(calculatedResult, expectedResult, places=4)

    @data(({0: 0.9, 1: 0.1}, 1, {0: {0: 0.5, 1: 0.5}, 1: {0: 0.2, 1: 0.8}},
           {0: {0: 0.1, 1: 0.1, 2: 0.8}, 1: {0: 2, 1: 0.3, 2: 0.5}}, {0: 0.22815533980582525,
                                                                      1: 0.7718446601941747}))  # (xT_1Distribution, eT, transitionTable, sensorTable, expectedResult)
    @unpack
    def test_forward2(self, xT_1Distribution, eT, transitionTable, sensorTable, expectedResult):
        calculatedResult = targetCode.forward(xT_1Distribution, eT, transitionTable, sensorTable)

        self.assertNumericDictAlmostEqual(calculatedResult, expectedResult, places=4)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

