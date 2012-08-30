import unittest
import static_cache

class lbtypes_test(unittest.TestCase):
    def test_simple_cache(self):
        VALUE = 0
        
        @static_cache.cache
        def my_function(arg1):
            return VALUE
        
        self.assertEqual(my_function(0),0)
        VALUE = 1
        self.assertEqual(my_function(0),0)
        self.assertEqual(my_function(1),1)
        self.assertEqual(my_function(2),1)
        
    def test_complex_cache(self):
        VALUE = 0
        KEY = 0
        
        @static_cache.cache(key_function=lambda arg1: KEY)
        def my_function(arg1):
            return VALUE
        
        self.assertEqual(my_function(0),0)
        VALUE = 1
        self.assertEqual(my_function(0),0)
        self.assertEqual(my_function(1),0)
        self.assertEqual(my_function(2),0)
        KEY = 1
        self.assertEqual(my_function(0),1)
        self.assertEqual(my_function(1),1)
        self.assertEqual(my_function(2),1)
        
if __name__ == '__main__':
    unittest.main()