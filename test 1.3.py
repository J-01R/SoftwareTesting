import unittesting
import sympy as sp
import numpy as np
from scripy import linalg

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
        arr1 = []
        arr_det_np = numpy_determinant(arr1)
        arr2 = []
        arr_det_sc = scipy_determinant(arr2)
        message = "The two determinant values are not equal"
        self.assertEqual(arr_det_np, arr_det_sc, message)

        if __name__ == '__main__':
            unittest.main()

            #   Test case 1
            arr1 = ArrValue()
            arr_det_np = numpy_determinant(arr1.value)
            arr2 = ArrValue()
            arr_det_sc = scipy_determinant(arr2.value)
