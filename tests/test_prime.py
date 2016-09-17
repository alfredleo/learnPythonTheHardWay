import unittest
import prime

class Test(unittest.TestCase):
    """Unit tests for prime module."""
    
    def test_simple(self):
        self.assertEqual(prime.simple(7), True)
    
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        
    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())
    
if __name__ == "__main__":
    unittest.main()