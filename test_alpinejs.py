# test_alpinejs.py
"""
Tests for AlpineJS module.
"""

import unittest
from alpinejs import AlpineJS

class TestAlpineJS(unittest.TestCase):
    """Test cases for AlpineJS class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AlpineJS()
        self.assertIsInstance(instance, AlpineJS)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AlpineJS()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
