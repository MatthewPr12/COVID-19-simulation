"""creating arrays"""

import ctypes

class Array:
    """class arrey"""
    def __init__(self, size):
        """initialisation"""
        assert size > 0
        self._size = size
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self.clear(None)

    def __len__(self):
        """returns len"""
        return self._size

    def __getitem__(self, index):
        """returns item"""
        assert 0 <= index < len(self)
        return self._elements[index]

    def __setitem__(self, index, value):
        """sets item"""
        assert 0 <= index < len(self)
        self._elements[index] = value

    def clear(self, value):
        """clears item"""
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        """iterating"""
        return _ArrayIterator(self._elements)

class _ArrayIterator:
    """iterating array class"""
    def __init__(self, the_array):
        """initialisation"""
        self._array_ref = the_array
        self._cur_index = 0

    def __iter__(self):
        """iterating"""
        return self

    def __next__(self):
        """next method"""
        if self._cur_index < len(self._array_ref):
            entry = self._array_ref[self._cur_index]
            self._cur_index += 1
            return entry
        else:
            raise StopIteration

class Array2D:
    """class Array 2d"""
    def __init__(self, num_rows, num_cols):
        """initialisation"""
        self.rows = Array(num_rows)
        for i in range(num_rows):
            self.rows[i] = Array(num_cols)

    def num_rows(self):
        """num of rows"""
        return len(self.rows)

    def num_cols(self):
        """num of colons"""
        return len(self.rows[0])

    def clear(self, value):
        """clear value"""
        for row in range(self.num_rows()):
            self.rows[row].clear(value)

    def __getitem__(self, index_tuple):
        """get item"""
        assert len(index_tuple) == 2
        row = index_tuple[0]
        col = index_tuple[1]
        assert 0 <= row <= self.num_rows() and 0 <= col <= self.num_cols()
        array_1d = self.rows[row]
        return array_1d[col]

    def __setitem__(self, index_tuple, value):
        """set item"""
        assert len(index_tuple) == 2
        row = index_tuple[0]
        col = index_tuple[1]
        assert 0 <= row < self.num_rows() and 0 <= col < self.num_cols()
        array_1d = self.rows[row]
        array_1d[col] = value
