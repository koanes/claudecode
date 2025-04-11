"""
Tests for the hello_world module.
"""
import unittest
from hello_world import get_greeting

class TestHelloWorld(unittest.TestCase):
    """
    Test cases for the hello_world module.
    """
    
    def test_get_greeting(self):
        """
        Test that get_greeting returns the expected message.
        """
        self.assertEqual(get_greeting(), "Hello, World!")