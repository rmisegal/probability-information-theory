#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for Slide 2: Uniform Distribution
"""

import unittest
import numpy as np
import sys
from pathlib import Path

# Suppress matplotlib warnings
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module="matplotlib")
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for tests

# Add project path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from slide02.slide02_main import generate_uniform_data

class TestSlide02(unittest.TestCase):
    """Tests for Slide 2"""
    
    def test_generate_uniform_data(self):
        """Test uniform data generation"""
        a, b = 0, 10
        n_samples = 1000
        data = generate_uniform_data(a, b, n_samples)
        
        # Check number of samples
        self.assertEqual(len(data), n_samples)
        
        # Check value range
        self.assertTrue(all(a <= x <= b for x in data))
        
        # Check mean (with tolerance)
        expected_mean = (a + b) / 2
        actual_mean = np.mean(data)
        self.assertAlmostEqual(actual_mean, expected_mean, delta=0.5)
        
        # Check variance (with tolerance)
        expected_var = (b - a) ** 2 / 12
        actual_var = np.var(data)
        self.assertAlmostEqual(actual_var, expected_var, delta=1.0)
    
    def test_uniform_properties(self):
        """Test theoretical properties of uniform distribution"""
        a, b = 5, 15
        
        # Theoretical mean
        expected_mean = (a + b) / 2
        self.assertEqual(expected_mean, 10)
        
        # Theoretical variance
        expected_var = (b - a) ** 2 / 12
        self.assertAlmostEqual(expected_var, 8.333, places=3)

if __name__ == '__main__':
    unittest.main(verbosity=2)

