import unittest
from Main import SquareMatrix

# testMain -> test/testMain.py but IFU with python importing


class TestSquareMatrixMethods(unittest.TestCase):
    def setUp(self):
        self.matrix = SquareMatrix(4, [[1, 2, 3, 4],
                                       [5, 1, 2, 3],
                                       [6, 5, 3, 8],
                                       [9, 23, 15, 2]])
        self.transposedMatrix = SquareMatrix(4, [[1, 5, 6, 9],
                                                 [2, 1, 5, 23],
                                                 [3, 2, 3, 15],
                                                 [4, 3, 8, 2]])
        self.equalMatrix = SquareMatrix(4, [[1, 2, 3, 4],
                                            [5, 1, 2, 3],
                                            [6, 5, 3, 8],
                                            [9, 23, 15, 2]])

        self.summedMatrix = SquareMatrix(4, [[2, 4, 6, 8],
                                             [10, 2, 4, 6],
                                             [12, 10, 6, 16],
                                             [18, 46, 30, 4]])

    def test_MatrixPrints(self):
        print(self.matrix)  # TODO: Capture console output and compare it to expected output

    def test_mainDiagonalSumWorks(self):
        self.assertEqual(self.matrix.get_diagonal_sum(), 7)

    def test_transposeWorks(self):
        self.assertEqual(self.matrix.transpose(), self.transposedMatrix)

    def test_matrixAreEqual(self):
        self.assertEqual(self.matrix, self.equalMatrix)

    def test_matrixAddMethodIsWorking(self):
        self.assertEqual(self.matrix + self.equalMatrix, self.summedMatrix)


if __name__ == '__main__':
    unittest.main()
