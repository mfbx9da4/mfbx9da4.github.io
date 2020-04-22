import unittest
from .main import parse_grid, find_locations, valid_moves, Pos


class TestStringMethods(unittest.TestCase):
    def test_convert_location_to_string(self):
        self.assertEqual(Pos(r=3, c=4).as_string(), "D5")
        self.assertEqual(Pos(r=2, c=3).as_string(), "C4")

    def test_parse_grid(self):
        grid = """
        ........
        ........
        ........
        ...BW...
        ...WB...
        ........
        ........
        ........
        """
        ans = parse_grid(grid)
        expected = [
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', 'B', 'W', '.', '.', '.'],
            ['.', '.', '.', 'W', 'B', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.']
        ]
        self.assertEqual(ans, expected)

    def test_find_locations(self):
        grid = [
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', 'B', 'W', '.', '.', '.'],
            ['.', '.', '.', 'W', 'B', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.']
        ]
        locations = find_locations(grid, "B")
        expected = [
            Pos(**{'r': 3, 'c': 3}),
            Pos(**{'r': 4, 'c': 4})
        ]
        self.assertEqual(locations, expected)

    def test_valid_moves(self):
        grid = """
        ........
        ........
        ........
        ...BW...
        ...WB...
        ........
        ........
        ........
        """
        ans = valid_moves(grid, "B")
        expected = {"C5", "D6", "E3", "F4"}
        self.assertEqual(ans, expected)


if __name__ == '__main__':
    unittest.main()
