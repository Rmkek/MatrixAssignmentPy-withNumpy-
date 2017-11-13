from numpy import matrix as np_matrix
from numpy import take as np_take
from random import randint


# Are you sure this is a good architecture choice?
def create_matrix(size, content, rand_range):
    if content:
        return np_matrix(content)
    else:
        return np_matrix([[randint(rand_range[0], rand_range[1])
                           for x in range(size)] for y in range(size)])


class SquareMatrix:
    _size = None
    matrixAmount = 0

    def __init__(self, size=5, content=None, rand_range=(-128, 127)):
        # TODO: check if matrix size and created matrix size are actually same
        self._size = size
        SquareMatrix.matrixAmount += 1

        self.matrix = create_matrix(self._size, content, rand_range)

    def __str__(self):
        return self.matrix.__str__()

    def __lt__(self, other):
        return (self.matrix < other.matrix).take(1).item()

    def __eq__(self, other):
        return (self.matrix == other.matrix).take(1).item()

    def __gt__(self, other):
        return (self.matrix > other.matrix).take(1).item()

    def __add__(self, other):
        return self.matrix.__add__(other.matrix)

    def get_diagonal_sum(self):
        return self.matrix.diagonal().sum()

    def transpose(self):
        return self.matrix.transpose()

    def __get_size(self):
        return self._size

    def __get_matrixes(self):
        return SquareMatrix.matrixAmount

    size = property(__get_size)
    matrixes = property(__get_matrixes)


def main():
    matrix = SquareMatrix(4, [[1, 2, 3, 4],
                              [5, 1, 2, 3],
                              [6, 5, 3, 8],
                              [9, 23, 15, 2]])

    matrix3 = SquareMatrix(4, [[1, 1, 1, 1],
                              [1, 1, 1, 1],
                              [1, 1, 1, 1],
                              [1, 1, 1, 1]])
    matrix2 = SquareMatrix(3, None, (-14, 27))


if __name__ == '__main__':
    main()
