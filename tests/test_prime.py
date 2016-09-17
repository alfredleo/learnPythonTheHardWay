import unittest
import prime

class Test(unittest.TestCase):
    """Unit tests for prime module."""
    
    def test_simple(self):
        self.assertEqual(prime.simple(7), True)
    
if __name__ == "__main__":
    unittest.main()