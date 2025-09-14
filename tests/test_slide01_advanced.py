#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advanced Tests for Slide 1: Introduction to Probability
Includes output capture and error logging
"""

import unittest
import numpy as np
import sys
from pathlib import Path

# Add project path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from tests.test_utils import OutputCapture, ErrorLogger, run_module_with_capture, check_output_patterns
from slide01.slide01_main import calculate_dice_probabilities, simulate_dice_rolls

class TestSlide01Advanced(unittest.TestCase):
    """Advanced tests for Slide 1 with output validation"""
    
    def setUp(self):
        """Set up test environment"""
        self.error_logger = ErrorLogger("slide01_advanced")
        self.error_logger.clear_log()
    
    def test_calculate_dice_probabilities_output(self):
        """Test dice probability calculations with output validation"""
        expected_patterns = [
            "=== Dice Probability Calculations ===",
            "Probability for each outcome: 0.167",
            "Probability of even number: 0.500",
            "Probability of odd number: 0.500",
            "Probability of number > 4: 0.333"
        ]
        
        forbidden_patterns = [
            "findfont: Font family",
            "not found",
            "ERROR",
            "Exception",
            "Traceback"
        ]
        
        with OutputCapture() as capture:
            outcomes, probabilities = calculate_dice_probabilities()
        
        output = capture.get_combined()
        success, errors = check_output_patterns(output, expected_patterns, forbidden_patterns)
        
        if not success:
            self.error_logger.log_error(
                expected=expected_patterns,
                actual=output,
                error_type="OUTPUT_VALIDATION_FAILED",
                additional_info={"errors": errors}
            )
            self.fail(f"Output validation failed: {errors}")
        
        # Verify function results
        self.assertEqual(len(outcomes), 6)
        self.assertEqual(len(probabilities), 6)
        for prob in probabilities:
            self.assertAlmostEqual(prob, 1/6, places=3)
    
    def test_simulate_dice_rolls_output(self):
        """Test dice roll simulation with output validation"""
        expected_patterns = [
            "=== Simulation of 1000 Dice Rolls ===",
            "Simulation Results:",
            "(theoretical: 0.167)"
        ]
        
        forbidden_patterns = [
            "findfont: Font family",
            "not found",
            "ERROR",
            "Exception"
        ]
        
        with OutputCapture() as capture:
            rolls, frequencies = simulate_dice_rolls(1000)
        
        output = capture.get_combined()
        success, errors = check_output_patterns(output, expected_patterns, forbidden_patterns)
        
        if not success:
            self.error_logger.log_error(
                expected=expected_patterns,
                actual=output,
                error_type="SIMULATION_OUTPUT_FAILED",
                additional_info={"errors": errors}
            )
            self.fail(f"Simulation output validation failed: {errors}")
        
        # Verify simulation results
        self.assertEqual(len(rolls), 1000)
        self.assertEqual(len(frequencies), 6)
        self.assertAlmostEqual(sum(frequencies), 1.0, places=3)
    
    def test_slide01_main_execution(self):
        """Test complete slide01 main execution"""
        slide01_path = project_root / "slide01" / "slide01_main.py"
        
        stdout, stderr, returncode = run_module_with_capture(slide01_path)
        
        expected_patterns = [
            "Slide 1: Introduction to Probability",
            "Based on: Jon Krohn's Machine Learning Foundations series",
            "Lecturer: Dr. Yoram Segal",
            "=== Dice Probability Calculations ===",
            "=== Simulation of 1000 Dice Rolls ===",
            "=== Basic Probability Rules ===",
            "Slide 1 demonstration completed"
        ]
        
        forbidden_patterns = [
            "findfont: Font family",
            "not found",
            "ERROR",
            "Exception",
            "Traceback",
            "ModuleNotFoundError",
            "ImportError"
        ]
        
        combined_output = stdout + stderr
        success, errors = check_output_patterns(combined_output, expected_patterns, forbidden_patterns)
        
        if not success or returncode != 0:
            self.error_logger.log_error(
                expected=expected_patterns,
                actual=combined_output,
                error_type="MAIN_EXECUTION_FAILED",
                additional_info={
                    "errors": errors,
                    "return_code": returncode,
                    "stdout": stdout,
                    "stderr": stderr
                }
            )
            self.fail(f"Main execution failed. Return code: {returncode}, Errors: {errors}")
    
    def test_no_font_warnings(self):
        """Specifically test that there are no font warnings"""
        with OutputCapture() as capture:
            calculate_dice_probabilities()
        
        output = capture.get_combined()
        
        font_warnings = [
            "findfont: Font family",
            "Arial Unicode MS",
            "not found"
        ]
        
        found_warnings = []
        for warning in font_warnings:
            if warning in output:
                found_warnings.append(warning)
        
        if found_warnings:
            self.error_logger.log_error(
                expected="No font warnings",
                actual=output,
                error_type="FONT_WARNINGS_DETECTED",
                additional_info={"warnings_found": found_warnings}
            )
            self.fail(f"Font warnings detected: {found_warnings}")
    
    def test_html_slide_function(self):
        """Test HTML slide opening function"""
        from slide01.slide01_main import show_slide
        
        with OutputCapture() as capture:
            show_slide()
        
        output = capture.get_combined()
        
        # Should either open successfully or show helpful error message
        valid_outputs = [
            "Slide opened in browser",
            "Could not open slide automatically",
            "Slide file not found"
        ]
        
        has_valid_output = any(msg in output for msg in valid_outputs)
        
        if not has_valid_output:
            self.error_logger.log_error(
                expected=valid_outputs,
                actual=output,
                error_type="HTML_SLIDE_FUNCTION_FAILED"
            )
            self.fail(f"HTML slide function produced unexpected output: {output}")

class TestSlide01Performance(unittest.TestCase):
    """Performance tests for Slide 1"""
    
    def setUp(self):
        self.error_logger = ErrorLogger("slide01_performance")
        self.error_logger.clear_log()
    
    def test_execution_time(self):
        """Test that slide execution completes within reasonable time"""
        import time
        
        start_time = time.time()
        
        with OutputCapture():
            calculate_dice_probabilities()
            simulate_dice_rolls(1000)
        
        execution_time = time.time() - start_time
        
        # Should complete within 10 seconds
        if execution_time > 10:
            self.error_logger.log_error(
                expected="< 10 seconds",
                actual=f"{execution_time:.2f} seconds",
                error_type="PERFORMANCE_SLOW"
            )
            self.fail(f"Execution too slow: {execution_time:.2f} seconds")

if __name__ == '__main__':
    # Create logs directory
    Path("tests/logs").mkdir(exist_ok=True)
    
    # Run tests
    unittest.main(verbosity=2)

