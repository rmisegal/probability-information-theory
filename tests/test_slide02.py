#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
טסטים לשקף 2: התפלגות אחידה
Tests for Slide 2: Uniform Distribution
"""

import unittest
import numpy as np
import sys
from pathlib import Path

# הוספת נתיב הפרויקט
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from slide02.slide02_main import generate_uniform_data

class TestSlide02(unittest.TestCase):
    """טסטים לשקף 2"""
    
    def test_generate_uniform_data(self):
        """בדיקת יצירת נתונים אחידים"""
        a, b = 0, 10
        n_samples = 1000
        data = generate_uniform_data(a, b, n_samples)
        
        # בדיקת מספר הדגימות
        self.assertEqual(len(data), n_samples)
        
        # בדיקת טווח הערכים
        self.assertTrue(all(a <= x <= b for x in data))
        
        # בדיקת ממוצע (עם סובלנות)
        expected_mean = (a + b) / 2
        actual_mean = np.mean(data)
        self.assertAlmostEqual(actual_mean, expected_mean, delta=0.5)
        
        # בדיקת שונות (עם סובלנות)
        expected_var = (b - a) ** 2 / 12
        actual_var = np.var(data)
        self.assertAlmostEqual(actual_var, expected_var, delta=1.0)
    
    def test_uniform_properties(self):
        """בדיקת מאפיינים תיאורטיים של התפלגות אחידה"""
        a, b = 5, 15
        
        # ממוצע תיאורטי
        expected_mean = (a + b) / 2
        self.assertEqual(expected_mean, 10)
        
        # שונות תיאורטית
        expected_var = (b - a) ** 2 / 12
        self.assertAlmostEqual(expected_var, 8.333, places=3)

if __name__ == '__main__':
    unittest.main(verbosity=2)

