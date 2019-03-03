import unittest
from {{cookiecutter.app_name}} import util


class TestUtil(unittest.TestCase):

    def test_pluck(self):
        things = {'blah': 'bleh', 'foo': 'bar'}
        foo, blah = util.pluck(things, 'foo', 'blah')

        self.assertEqual(foo, 'bar')
        self.assertEqual(blah, 'bleh')

        other = {'blah': 'bleh', 'foo': 'bar'}
        _, not_there = util.pluck(other, 'foo', 'not_there')
        self.assertEqual(not_there, None)

    def test_filter_dict(self):
        things = {'blah': 'bleh', 'foo': 'bar', 'yo': 'omit'}
        res = util.filter_dict(things, 'blah', 'foo')

        self.assertEqual(len(res.keys()), 2)
        self.assertTrue('blah' in res)
        self.assertTrue('foo' in res)
        self.assertFalse('yo' in res)

        res = util.filter_dict(things, 'chicken')

        self.assertTrue('chicken' not in res)

    def test_deep_get(self):
        things = {
            'one': {
                'two': 'tree'
            },
            'foo': 'bar',
            'yo': 'omit'
        }
        is_none = util.deep_get(things, 'chillax')
        self.assertIsNone(is_none)

        is_tree = util.deep_get(things, 'one.two')
        self.assertEqual(is_tree, 'tree')

        is_none = util.deep_get(things, 'one.five')
        self.assertIsNone(is_none)

    def test_delim_split(self):
        raw_str = 'the, quick,brown  ,   fox, tripped'
        chunks = util.delim_split(raw_str)
        self.assertEqual(len(chunks), 5)
        for c in chunks:
            self.assertTrue(' ' not in c)

        raw_str = 'the| quick|brown  |   fox| tripped'
        chunks = util.delim_split(raw_str)
        self.assertEqual(len(chunks), 1)

        chunks = util.delim_split(raw_str, '|')
        self.assertEqual(len(chunks), 5)
        for c in chunks:
            self.assertTrue(' ' not in c)
