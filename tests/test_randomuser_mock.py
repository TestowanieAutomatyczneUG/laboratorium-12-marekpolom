import unittest
from unittest.mock import *
from assertpy import *

from sample.randomuser import User


class TestUser(unittest.TestCase):

    def test_getUser(self):
        test_object = User()
        test_object.getUser = MagicMock(return_value = {'results': [{'gender': 'male'}]})

        assert_that(test_object.getUser()['results']).is_length(1)

    def test_getUsers(self):
        test_object = User()
        test_object.getUsers = MagicMock(return_value = {'results': [{'gender': 'male'}, {'gender': 'male'}, {'gender': 'male'}, {'gender': 'male'}]})

        assert_that(test_object.getUsers(4)['results']).is_length(4)

    def test_getBySeed(self):
        test_object = User()
        test_object.getBySeed = MagicMock(return_value = {'results': [{'name': {'first': 'Britney'}}]})

        assert_that(test_object.getBySeed('foobar')['results'][0]['name']['first']).is_equal_to('Britney')

    def test_getByNation(self):
        test_object = User()
        test_object.getByNation = MagicMock(return_value = {'results': [{'nat': 'US'}]})

        assert_that(test_object.getByNation('us')['results'][0]['nat']).is_equal_to('US')

    def test_getWithOpt(self):
        test_object = User()
        test_object.getWithOpt = MagicMock(return_value = {'results': [{'name': 'Britney', 'gender': 'male', 'nat': 'US'}]})

        assert_that(test_object.getWithOpt(['name', 'gender', 'nat'])['results'][0].keys()).is_length(3)

if __name__ == '__main__':
    unittest.main()
