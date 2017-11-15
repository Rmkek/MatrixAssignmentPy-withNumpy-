from numpy import matrix as np_matrix
from random import randint


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
        self._size = size
        SquareMatrix.matrixAmount += 1
        self.matrix = create_matrix(self._size, content, rand_range)

        # check if matrix size and created matrix size are actually same
        if not self.matrix.shape[0] == self.matrix.shape[1]:
            raise TypeError('Matrix is not square-shaped.')

    def __str__(self):
        return self.matrix.__str__()

    def __lt__(self, other):
        return (self.matrix < other.matrix).take(1).item()

    def __eq__(self, other):
        if not (self.matrix.shape[0] == other.matrix.shape[0] and self.matrix.shape[1] == other.matrix.shape[1]):
            raise TypeError('Matrixes are not the same shape.')

        first_list = self.matrix.tolist()
        second_list = other.matrix.tolist()

        for i in range(0, len(first_list)):
            if not first_list[i] == second_list[i]:
                return False

        return True

    def __gt__(self, other):
        return (self.matrix > other.matrix).take(1).item()

    def __add__(self, other):
        return SquareMatrix(self.size, self.matrix.__add__(other.matrix).tolist())

    def get_diagonal_sum(self):
        return self.matrix.diagonal().sum()

    def transpose(self):
        self.matrix = self.matrix.transpose()
        return self

    def __get_size(self):
        return self._size

    def __get_matrixes(self):
        return SquareMatrix.matrixAmount

    size = property(__get_size)
    matrixes = property(__get_matrixes)


def main():
    first_matrix = SquareMatrix(5, [
        [1, 2, 3, 4, 5],
        [2, 3, 7, 4, 5],
        [6, 3, 42, 42, 42],
        [42, 42, 42, 42, 42],
        [42, 42, 42, 42, 42]])

    second_matrix = SquareMatrix(5, [
        [42, 42, 42, 42, 42],
        [42, 42, 42, 42, 42],
        [42, 42, 42, 42, 42],
        [42, 42, 42, 42, 42],
        [42, 42, 42, 42, 42]
    ])

    third_matrix = SquareMatrix(4, None, (-42, 42))
    fourth_matrix = SquareMatrix(4, None, (-1337, 1337))
    fifth_matrix = SquareMatrix(42, None, (-42, 42))

    print('Main diagonal sum of 5-shaped matrixes, first_matrix: {}; second_matrix: {}'.format(
        first_matrix.get_diagonal_sum(), second_matrix.get_diagonal_sum()))
    print('third_matrix before transpose: \n{}'.format(third_matrix))
    print('third_matrix after being transposed: \n{}'.format(third_matrix.transpose()))
    print('fourth_matrix before transpose: \n{}'.format(fourth_matrix))
    print('fourth_matrix after being transposed: \n{}'.format(fourth_matrix.transpose()))
    print('Sum of two 5-shaped matrixes: \n{}'.format(first_matrix + second_matrix))
    print('third_matrix > fourth_matrix: {}'.format(third_matrix > fourth_matrix))
    print('third_matrix > fifth_matrix: {}'.format(third_matrix > fifth_matrix))
    print('Therefore, fifth_matrix is the biggest matrix of all.')




if __name__ == '__main__':
    main()
