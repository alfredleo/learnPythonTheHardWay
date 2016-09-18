import unittest
import prime

class Test(unittest.TestCase):
    """Unit tests for prime module."""
    
    def test_simple(self):
        # Prime numbers
        self.assertTrue(prime.simple(2))
        self.assertTrue(prime.simple(7))
        self.assertTrue(prime.simple(13))
        # 33,265 digits Mersenne prime, 1988 January 29 by Walter Colquitt & Luke Welsh
        # self.assertTrue(prime.simple(2**110503-1))  # use numpy package
        
        # Composite numbers
        self.assertFalse(prime.simple(1729))  # Ramanujan's famous taxi-cab number 7,13,19,91,133,247
        self.assertFalse(prime.simple(1))
        self.assertFalse(prime.simple(8))
    
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        
    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())
    
if __name__ == "__main__":
    unittest.main()