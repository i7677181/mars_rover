import unittest

from solution import go


class TestSum(unittest.TestCase):
    """ A bunch of test cases for our solution """
    def test_solution_example(self):
        """Testing the example input"""
        assert '0 0 N' == go(
# no movement
'''1 1
0 0 N
'''
)

        assert '1 3 N\n5 1 E' == go(
# the test example
'''5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
'''
)
        assert '1 3 N' == go(
# the first test case of the test example
'''5 5
1 2 N
LMLMLMLMM'''
)

        assert '5 1 E' == go(
# the second test case of the test example
'''5 5
3 3 E
MMRMMRMRRM
'''
        )

    def test_out_of_bounds(self):
        """Testing incorrect input"""

        try:
            go(
# an example that will go out of bounds
'''5 5
3 3 E
MMMMM'''
)
        except IndexError:
            print('invalid input, out of bounds exception caught')
        else:
            raise RuntimeError("out of bounds not detected")

        try:
            go(
# an example that places the robot outside of the map
'''0 0
1 1 E
'''
)
        except IndexError:
            print('invalid input, out of bounds exception caught')
        else:
            raise RuntimeError("out of bounds not detected")


if __name__ == '__main__':
    unittest.main()


