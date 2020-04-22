import unittest
from .main import promise_all


def fetch(url):
    return url


class TestStringMethods(unittest.TestCase):

    def test_solve(self):
        urls = ['https://wikipedia.org']
        promise_all(map(fetch, urls))


if __name__ == '__main__':
    unittest.main()
