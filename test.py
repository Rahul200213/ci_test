from data import c
import unittest

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(c.add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(c.add(-1, -2), -3)

    def test_add_mixed_numbers(self):
        self.assertEqual(c.add(1, -2), -1)
        self.assertEqual(c.add(-1, 2), 1)

class TestStringAdd(unittest.TestCase):
    def test_add_two(self):
        self.assertEqual(c.string_add("hello","world"),"helloworld")
    def test_upper(self):
        s="hello"
        self.assertEqual(c.check_raise(),"test")
        self.assertEqual(s.capitalize(),"Hello")
        self.assertEqual(s.count('l'),2)
        self.assertIn(1,[1,2,3])
        self.assertDictEqual({'a':1},{'a':1})
        self.assertIs('abc','abc')
        self.assertTupleEqual((1,23),(1,23))
        

if __name__ == '__main__':
    unittest.main()

