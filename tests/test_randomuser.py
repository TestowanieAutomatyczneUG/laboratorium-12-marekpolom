import unittest
from assertpy import *

from sample.randomuser import User


class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.temp = User()

    def test_getUser(self):
        assert_that(self.temp.getUser()['results']).is_length(1)

    def test_getUsers(self):
        assert_that(self.temp.getUsers(4)['results']).is_length(4)

    def test_getBySeed(self):
        assert_that(self.temp.getBySeed('foobar')['results'][0]['name']['first']).is_equal_to('Britney')

    def test_getByNation(self):
        assert_that(self.temp.getByNation('us')['results'][0]['nat']).is_equal_to('US')

    def test_getWithOpt(self):
        assert_that(self.temp.getWithOpt(['name', 'gender', 'nat'])['results'][0].keys()).is_length(3)

if __name__ == '__main__':
    unittest.main()
