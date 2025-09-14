#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for Slide 1: Introduction to Probability
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

from slide01.slide01_main import calculate_dice_probabilities, simulate_dice_rolls

class TestSlide01(unittest.TestCase):
    """Tests for Slide 1"""
    
    def test_calculate_dice_probabilities(self):
        """Test dice probability calculations"""
        outcomes, probabilities = calculate_dice_probabilities()
        
        # Check number of outcomes
        self.assertEqual(len(outcomes), 6)
        self.assertEqual(len(probabilities), 6)
        
        # Check probability values
        expected_prob = 1/6
        for prob in probabilities:
            self.assertAlmostEqual(prob, expected_prob, places=3)
        
        # Check sum of probabilities
        self.assertAlmostEqual(sum(probabilities), 1.0, places=3)
    
    def test_simulate_dice_rolls(self):
        """Test dice roll simulation"""
        n_rolls = 1000
        rolls, frequencies = simulate_dice_rolls(n_rolls)
        
        # Check number of rolls
        self.assertEqual(len(rolls), n_rolls)
        
        # Check value range
        self.assertTrue(all(1 <= roll <= 6 for roll in rolls))
        
        # Check sum of frequencies
        self.assertAlmostEqual(sum(frequencies), 1.0, places=3)
        
        # Check frequencies are close to theoretical (with tolerance)
        expected_freq = 1/6
        for freq in frequencies:
            self.assertAlmostEqual(freq, expected_freq, delta=0.05)
    
    def test_probability_rules(self):
        """Test basic probability rules"""
        # Probability of even
        prob_even = 3/6
        self.assertAlmostEqual(prob_even, 0.5, places=3)
        
        # Probability of odd
        prob_odd = 3/6
        self.assertAlmostEqual(prob_odd, 0.5, places=3)
        
        # Sum of complementary probabilities
        self.assertAlmostEqual(prob_even + prob_odd, 1.0, places=3)
        
        # Complementary probability
        prob_six = 1/6
        prob_not_six = 1 - prob_six
        self.assertAlmostEqual(prob_not_six, 5/6, places=3)
    
    def test_conditional_probability(self):
        """Test conditional probability"""
        # P(6|even) = 1/3 (out of 3 even numbers)
        prob_six_given_even = 1/3
        self.assertAlmostEqual(prob_six_given_even, 0.333, places=3)

class TestDataValidation(unittest.TestCase):
    """Tests for data validation"""
    
    def test_numpy_random_seed(self):
        """Test random seed consistency"""
        np.random.seed(42)
        rolls1 = np.random.randint(1, 7, 100)
        
        np.random.seed(42)
        rolls2 = np.random.randint(1, 7, 100)
        
        # Check results are identical
        np.testing.assert_array_equal(rolls1, rolls2)
    
    def test_probability_bounds(self):
        """Test probability bounds"""
        _, probabilities = calculate_dice_probabilities()
        
        for prob in probabilities:
            # Probability must be between 0 and 1
            self.assertGreaterEqual(prob, 0)
            self.assertLessEqual(prob, 1)

if __name__ == '__main__':
    # Run tests
    unittest.main(verbosity=2)

