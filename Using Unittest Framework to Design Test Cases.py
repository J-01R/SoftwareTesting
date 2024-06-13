import unittest
import sympy as sp
import numpy as np
from scipy import linalg


def numpy_determinant(arr):
    if len(sp.Matrix(arr).rref()[1]) < max(np.shape(arr)):
        return 0
    else:
        return np.linalg.det(arr)


def scipy_determinant(arr):
    return linalg.det(arr)


class ArrValue:
    value = np.array([[2, 1],
                      [2, 2]])


class TestMethods(unittest.TestCase):
    def test_positive(self):
        arr1 = [[1, 1], [1, 1]]
        print(arr1)
        arr_det_np = numpy_determinant(arr1)
        arr2 = [[1, 1], [1, 1]]
        print(arr2)
        arr_det_sc = scipy_determinant(arr2)
        message = "The two determinant values are not equal"
        self.assertEqual(arr_det_np, arr_det_sc, message)

    def test1(self):
        arr1 = ArrValue()
        arr_det_np = numpy_determinant(arr1.value)
        arr2 = ArrValue()
        arr_det_sc = scipy_determinant(arr2.value)
        message = "The two determinant values are not equal"
        self.assertEqual(arr_det_np, arr_det_sc, message)

    def test2(self):
        arr1 = ArrValue()
        print(arr1.value)
        arr_det_np = numpy_determinant(arr1.value)
        new_column = [[0], [0]]
        arr2 = np.append(arr1.value, new_column, axis=1)
        arr_det_sc = scipy_determinant(arr1.value)
        message = "The two determinant values are not equal"
        self.assertEqual(arr_det_np, arr_det_sc, message)

    def test3(self):
        arr1 = ArrValue()
        arr_det_np = numpy_determinant(arr1.value)
        arr2 = np.linalg.inv(arr1.value)
        arr_det_sc = scipy_determinant(arr2)
        message = "The two determinant values are not equal"
        self.assertEqual(arr_det_np, arr_det_sc, message)

    def test4(self):
        arr1 = ArrValue()
        arr_det_np = numpy_determinant(arr1.value)
        arr2 = arr1.value.transpose()
        arr_det_sc = scipy_determinant(arr2)
        message = "The two determinant values are not equal"
        self.assertEqual(arr_det_np, arr_det_sc, message)

    def test5(self):
        arr1 = np.array([[3, -6],
                         [1, -2]])
        arr_det_np = numpy_determinant(arr1)
        arr2 = np.square(arr1)
        arr_det_sc = scipy_determinant(arr2)
        message = "The two determinant values are not equal"
        self.assertEqual(arr_det_np, arr_det_sc, message)


if __name__ == '__main__':
    unittest.main()
