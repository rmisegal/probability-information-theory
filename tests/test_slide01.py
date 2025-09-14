#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
טסטים לשקף 1: מבוא להסתברות
Tests for Slide 1: Introduction to Probability
"""

import unittest
import numpy as np
import sys
from pathlib import Path

# הוספת נתיב הפרויקט
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from slide01.slide01_main import calculate_dice_probabilities, simulate_dice_rolls

class TestSlide01(unittest.TestCase):
    """טסטים לשקף 1"""
    
    def test_calculate_dice_probabilities(self):
        """בדיקת חישוב הסתברויות קובייה"""
        outcomes, probabilities = calculate_dice_probabilities()
        
        # בדיקת מספר התוצאות
        self.assertEqual(len(outcomes), 6)
        self.assertEqual(len(probabilities), 6)
        
        # בדיקת ערכי ההסתברויות
        expected_prob = 1/6
        for prob in probabilities:
            self.assertAlmostEqual(prob, expected_prob, places=3)
        
        # בדיקת סכום ההסתברויות
        self.assertAlmostEqual(sum(probabilities), 1.0, places=3)
    
    def test_simulate_dice_rolls(self):
        """בדיקת סימולציית זריקות קובייה"""
        n_rolls = 1000
        rolls, frequencies = simulate_dice_rolls(n_rolls)
        
        # בדיקת מספר הזריקות
        self.assertEqual(len(rolls), n_rolls)
        
        # בדיקת טווח הערכים
        self.assertTrue(all(1 <= roll <= 6 for roll in rolls))
        
        # בדיקת סכום התדירויות
        self.assertAlmostEqual(sum(frequencies), 1.0, places=3)
        
        # בדיקה שהתדירויות קרובות לתיאורטי (עם סובלנות)
        expected_freq = 1/6
        for freq in frequencies:
            self.assertAlmostEqual(freq, expected_freq, delta=0.05)
    
    def test_probability_rules(self):
        """בדיקת חוקי הסתברות בסיסיים"""
        # הסתברות לזוגי
        prob_even = 3/6
        self.assertAlmostEqual(prob_even, 0.5, places=3)
        
        # הסתברות לאי-זוגי
        prob_odd = 3/6
        self.assertAlmostEqual(prob_odd, 0.5, places=3)
        
        # סכום הסתברויות משלימות
        self.assertAlmostEqual(prob_even + prob_odd, 1.0, places=3)
        
        # הסתברות משלימה
        prob_six = 1/6
        prob_not_six = 1 - prob_six
        self.assertAlmostEqual(prob_not_six, 5/6, places=3)
    
    def test_conditional_probability(self):
        """בדיקת הסתברות מותנית"""
        # P(6|זוגי) = 1/3 (מתוך 3 מספרים זוגיים)
        prob_six_given_even = 1/3
        self.assertAlmostEqual(prob_six_given_even, 0.333, places=3)

class TestDataValidation(unittest.TestCase):
    """טסטים לוולידציה של נתונים"""
    
    def test_numpy_random_seed(self):
        """בדיקת עקביות הזרע האקראי"""
        np.random.seed(42)
        rolls1 = np.random.randint(1, 7, 100)
        
        np.random.seed(42)
        rolls2 = np.random.randint(1, 7, 100)
        
        # בדיקה שהתוצאות זהות
        np.testing.assert_array_equal(rolls1, rolls2)
    
    def test_probability_bounds(self):
        """בדיקת גבולות הסתברות"""
        _, probabilities = calculate_dice_probabilities()
        
        for prob in probabilities:
            # הסתברות חייבת להיות בין 0 ל-1
            self.assertGreaterEqual(prob, 0)
            self.assertLessEqual(prob, 1)

if __name__ == '__main__':
    # הרצת הטסטים
    unittest.main(verbosity=2)

