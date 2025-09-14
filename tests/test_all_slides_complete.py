#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive Tests for All 10 Slides
Tests all slides without opening GUI windows
"""

import unittest
import sys
from pathlib import Path

# Add project path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from tests.test_utils import OutputCapture, ErrorLogger, run_module_with_capture, check_output_patterns

class TestAllSlidesComplete(unittest.TestCase):
    """Test all 10 slides comprehensively"""
    
    def setUp(self):
        """Set up test environment"""
        self.error_logger = ErrorLogger("all_slides_complete")
        self.error_logger.clear_log()
        self.main_path = project_root / "main.py"
    
    def test_slide_01_execution(self):
        """Test slide 1 execution"""
        self._test_slide_execution(1, [
            "Running slide 1",
            "Opening HTML slide 1",
            "Slide 1: Introduction to Probability",
            "=== Dice Probability Calculations ===",
            "Slide 1 completed successfully"
        ])
    
    def test_slide_02_execution(self):
        """Test slide 2 execution"""
        self._test_slide_execution(2, [
            "Running slide 2",
            "Opening HTML slide 2",
            "Slide 2: Uniform Distribution",
            "=== Generating 1000 samples from Uniform Distribution",
            "Slide 2 completed successfully"
        ])
    
    def test_slide_03_execution(self):
        """Test slide 3 execution"""
        self._test_slide_execution(3, [
            "Running slide 3",
            "Opening HTML slide 3",
            "Slide 3: Normal Distribution",
            "=== Generating 1000 samples from Normal Distribution",
            "Slide 3 completed successfully"
        ])
    
    def test_slide_04_execution(self):
        """Test slide 4 execution"""
        self._test_slide_execution(4, [
            "Running slide 4",
            "Opening HTML slide 4",
            "Slide 4: Binomial Distribution",
            "Slide 4 completed successfully"
        ])
    
    def test_slide_05_execution(self):
        """Test slide 5 execution"""
        self._test_slide_execution(5, [
            "Running slide 5",
            "Opening HTML slide 5",
            "Slide 5: Poisson Distribution",
            "Slide 5 completed successfully"
        ])
    
    def test_slide_06_execution(self):
        """Test slide 6 execution"""
        self._test_slide_execution(6, [
            "Running slide 6",
            "Opening HTML slide 6",
            "Slide 6: Measures of Central Tendency",
            "Slide 6 completed successfully"
        ])
    
    def test_slide_07_execution(self):
        """Test slide 7 execution"""
        self._test_slide_execution(7, [
            "Running slide 7",
            "Opening HTML slide 7",
            "Slide 7: Measures of Dispersion",
            "Slide 7 completed successfully"
        ])
    
    def test_slide_08_execution(self):
        """Test slide 8 execution"""
        self._test_slide_execution(8, [
            "Running slide 8",
            "Opening HTML slide 8",
            "Slide 8: Correlation and Correlation Matrix",
            "Slide 8 completed successfully"
        ])
    
    def test_slide_09_execution(self):
        """Test slide 9 execution"""
        self._test_slide_execution(9, [
            "Running slide 9",
            "Opening HTML slide 9",
            "Slide 9: Shannon Entropy",
            "Slide 9 completed successfully"
        ])
    
    def test_slide_10_execution(self):
        """Test slide 10 execution"""
        self._test_slide_execution(10, [
            "Running slide 10",
            "Opening HTML slide 10",
            "Slide 10: KL Divergence and Cross-Entropy",
            "Slide 10 completed successfully"
        ])
    
    def test_all_slides_no_font_warnings(self):
        """Test that NO slides produce font warnings"""
        font_warnings_found = []
        
        for slide_num in range(1, 11):
            stdout, stderr, returncode = run_module_with_capture(self.main_path, ["--slide", str(slide_num)])
            combined_output = stdout + stderr
            
            font_warning_patterns = [
                "findfont: Font family",
                "Arial",
                "not found"
            ]
            
            for pattern in font_warning_patterns:
                if pattern in combined_output:
                    font_warnings_found.append({
                        "slide": slide_num,
                        "pattern": pattern,
                        "output_sample": combined_output[:200]  # First 200 chars
                    })
        
        if font_warnings_found:
            self.error_logger.log_error(
                expected="No font warnings in any slide",
                actual=font_warnings_found,
                error_type="FONT_WARNINGS_IN_SLIDES"
            )
            self.fail(f"Font warnings found in slides: {[w['slide'] for w in font_warnings_found]}")
    
    def test_all_python_files_exist(self):
        """Test that all Python files exist for slides 1-10"""
        missing_files = []
        
        for slide_num in range(1, 11):
            slide_dir = f"slide{slide_num:02d}"
            python_file = project_root / slide_dir / f"{slide_dir}_main.py"
            
            if not python_file.exists():
                missing_files.append(str(python_file))
        
        if missing_files:
            self.error_logger.log_error(
                expected="All Python files should exist for slides 1-10",
                actual=f"Missing files: {missing_files}",
                error_type="MISSING_PYTHON_FILES"
            )
            self.fail(f"Missing Python files: {missing_files}")
    
    def test_all_html_files_exist(self):
        """Test that all HTML files exist for slides 1-10"""
        missing_files = []
        
        for slide_num in range(1, 11):
            slide_dir = f"slide{slide_num:02d}"
            html_file = project_root / slide_dir / f"slide{slide_num}.html"
            
            if not html_file.exists():
                missing_files.append(str(html_file))
        
        if missing_files:
            self.error_logger.log_error(
                expected="All HTML files should exist for slides 1-10",
                actual=f"Missing files: {missing_files}",
                error_type="MISSING_HTML_FILES"
            )
            self.fail(f"Missing HTML files: {missing_files}")
    
    def _test_slide_execution(self, slide_num, expected_patterns):
        """Helper method to test individual slide execution"""
        stdout, stderr, returncode = run_module_with_capture(self.main_path, ["--slide", str(slide_num)])
        
        forbidden_patterns = [
            "findfont: Font family",
            "Arial.*not found",
            "ERROR",
            "Exception",
            "Traceback",
            "ModuleNotFoundError"
        ]
        
        combined_output = stdout + stderr
        success, errors = check_output_patterns(combined_output, expected_patterns, forbidden_patterns)
        
        if not success or returncode != 0:
            self.error_logger.log_error(
                expected=expected_patterns,
                actual=combined_output,
                error_type=f"SLIDE_{slide_num:02d}_EXECUTION_FAILED",
                additional_info={
                    "errors": errors,
                    "return_code": returncode,
                    "stdout": stdout[:500],  # First 500 chars
                    "stderr": stderr[:500]   # First 500 chars
                }
            )
            self.fail(f"Slide {slide_num} execution failed. Return code: {returncode}, Errors: {errors}")

class TestMainProgramComplete(unittest.TestCase):
    """Test main program with all slides"""
    
    def setUp(self):
        self.error_logger = ErrorLogger("main_program_complete")
        self.error_logger.clear_log()
        self.main_path = project_root / "main.py"
    
    def test_main_list_shows_all_slides(self):
        """Test that --list shows all 10 slides"""
        stdout, stderr, returncode = run_module_with_capture(self.main_path, ["--list"])
        
        expected_patterns = [
            "Available Slides:",
            "1. Introduction to Probability",
            "2. Uniform Distribution", 
            "3. Normal Distribution",
            "4. Binomial Distribution",
            "5. Poisson Distribution",
            "6. Measures of Central Tendency",
            "7. Measures of Dispersion",
            "8. Correlation and Correlation Matrix",
            "9. Shannon Entropy",
            "10. KL Divergence and Cross-Entropy"
        ]
        
        combined_output = stdout + stderr
        success, errors = check_output_patterns(combined_output, expected_patterns)
        
        if not success or returncode != 0:
            self.error_logger.log_error(
                expected=expected_patterns,
                actual=combined_output,
                error_type="MAIN_LIST_INCOMPLETE",
                additional_info={
                    "errors": errors,
                    "return_code": returncode
                }
            )
            self.fail(f"Main --list doesn't show all slides. Errors: {errors}")

if __name__ == '__main__':
    # Create logs directory
    Path("tests/logs").mkdir(exist_ok=True)
    
    # Run tests
    unittest.main(verbosity=2)

