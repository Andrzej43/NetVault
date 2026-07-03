# test_netvault.py
"""
Tests for NetVault module.
"""

import unittest
from netvault import NetVault

class TestNetVault(unittest.TestCase):
    """Test cases for NetVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NetVault()
        self.assertIsInstance(instance, NetVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NetVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
