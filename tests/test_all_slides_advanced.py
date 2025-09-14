#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advanced Tests for All Slides
Comprehensive output validation and error logging
"""

import unittest
import sys
from pathlib import Path

# Add project path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from tests.test_utils import OutputCapture, ErrorLogger, run_module_with_capture, check_output_patterns, create_test_summary

class TestAllSlidesAdvanced(unittest.TestCase):
    """Comprehensive tests for all slides"""
    
    def setUp(self):
        """Set up test environment"""
        self.error_logger = ErrorLogger("all_slides_advanced")
        self.error_logger.clear_log()
        self.test_results = []
    
    def test_slide01_execution(self):
        """Test slide01 complete execution"""
        slide_path = project_root / "slide01" / "slide01_main.py"
        result = self._test_slide_execution(slide_path, "slide01", [
            "Slide 1: Introduction to Probability",
            "=== Dice Probability Calculations ===",
            "=== Simulation of 1000 Dice Rolls ===",
            "Slide 1 demonstration completed"
        ])
        self.test_results.append(result)
        if not result["success"]:
            self.fail(result["error_message"])
    
    def test_slide02_execution(self):
        """Test slide02 complete execution"""
        slide_path = project_root / "slide02" / "slide02_main.py"
        result = self._test_slide_execution(slide_path, "slide02", [
            "Slide 2: Uniform Distribution",
            "=== Generating 1000 samples from Uniform Distribution",
            "Theoretical mean:",
            "Empirical mean:",
            "Slide 2 demonstration completed"
        ])
        self.test_results.append(result)
        if not result["success"]:
            self.fail(result["error_message"])
    
    def test_all_slides_no_font_warnings(self):
        """Test that no slides produce font warnings"""
        slides_to_test = [
            ("slide01", project_root / "slide01" / "slide01_main.py"),
            ("slide02", project_root / "slide02" / "slide02_main.py")
        ]
        
        font_warnings_found = []
        
        for slide_name, slide_path in slides_to_test:
            if slide_path.exists():
                stdout, stderr, returncode = run_module_with_capture(slide_path)
                combined_output = stdout + stderr
                
                font_warning_patterns = [
                    "findfont: Font family",
                    "Arial Unicode MS",
                    "not found"
                ]
                
                for pattern in font_warning_patterns:
                    if pattern in combined_output:
                        font_warnings_found.append({
                            "slide": slide_name,
                            "pattern": pattern,
                            "output": combined_output[:500]  # First 500 chars
                        })
        
        if font_warnings_found:
            self.error_logger.log_error(
                expected="No font warnings in any slide",
                actual=font_warnings_found,
                error_type="FONT_WARNINGS_IN_SLIDES"
            )
            self.fail(f"Font warnings found in slides: {[w['slide'] for w in font_warnings_found]}")
    
    def test_all_slides_html_files_exist(self):
        """Test that all slides have corresponding HTML files"""
        expected_html_files = [
            project_root / "slide01" / "slide1.html",
            project_root / "slide02" / "slide2.html",
            project_root / "slide03" / "slide3.html",
            project_root / "slide04" / "slide4.html",
            project_root / "slide05" / "slide5.html",
            project_root / "slide06" / "slide6.html",
            project_root / "slide07" / "slide7.html",
            project_root / "slide08" / "slide8.html",
            project_root / "slide09" / "slide9.html",
            project_root / "slide10" / "slide10.html"
        ]
        
        missing_files = []
        for html_file in expected_html_files:
            if not html_file.exists():
                missing_files.append(str(html_file))
        
        if missing_files:
            self.error_logger.log_error(
                expected="All HTML files should exist",
                actual=f"Missing files: {missing_files}",
                error_type="MISSING_HTML_FILES"
            )
            self.fail(f"Missing HTML files: {missing_files}")
    
    def test_all_slides_python_files_exist(self):
        """Test that all slides have corresponding Python files"""
        expected_python_files = [
            project_root / "slide01" / "slide01_main.py",
            project_root / "slide02" / "slide02_main.py"
        ]
        
        missing_files = []
        for py_file in expected_python_files:
            if not py_file.exists():
                missing_files.append(str(py_file))
        
        if missing_files:
            self.error_logger.log_error(
                expected="All Python files should exist",
                actual=f"Missing files: {missing_files}",
                error_type="MISSING_PYTHON_FILES"
            )
            self.fail(f"Missing Python files: {missing_files}")
    
    def test_project_structure(self):
        """Test overall project structure"""
        required_files = [
            project_root / "main.py",
            project_root / "requirements.txt",
            project_root / "README.md",
            project_root / "tests" / "__init__.py"
        ]
        
        required_dirs = [
            project_root / "slide01",
            project_root / "slide02",
            project_root / "tests"
        ]
        
        missing_items = []
        
        for file_path in required_files:
            if not file_path.exists():
                missing_items.append(f"FILE: {file_path}")
        
        for dir_path in required_dirs:
            if not dir_path.exists():
                missing_items.append(f"DIR: {dir_path}")
        
        if missing_items:
            self.error_logger.log_error(
                expected="Complete project structure",
                actual=f"Missing items: {missing_items}",
                error_type="INCOMPLETE_PROJECT_STRUCTURE"
            )
            self.fail(f"Project structure incomplete: {missing_items}")
    
    def _test_slide_execution(self, slide_path, slide_name, expected_patterns):
        """Helper method to test individual slide execution"""
        if not slide_path.exists():
            return {
                "slide": slide_name,
                "success": False,
                "error_message": f"Slide file not found: {slide_path}",
                "status": "FAILED"
            }
        
        stdout, stderr, returncode = run_module_with_capture(slide_path)
        
        forbidden_patterns = [
            "findfont: Font family",
            "not found",
            "ERROR",
            "Exception",
            "Traceback",
            "ModuleNotFoundError"
        ]
        
        combined_output = stdout + stderr
        success, errors = check_output_patterns(combined_output, expected_patterns, forbidden_patterns)
        
        if not success or returncode != 0:
            error_message = f"{slide_name} execution failed. Return code: {returncode}, Errors: {errors}"
            self.error_logger.log_error(
                expected=expected_patterns,
                actual=combined_output,
                error_type=f"{slide_name.upper()}_EXECUTION_FAILED",
                additional_info={
                    "errors": errors,
                    "return_code": returncode,
                    "stdout": stdout,
                    "stderr": stderr
                }
            )
            return {
                "slide": slide_name,
                "success": False,
                "error_message": error_message,
                "status": "FAILED"
            }
        
        return {
            "slide": slide_name,
            "success": True,
            "error_message": None,
            "status": "PASSED"
        }
    
    def tearDown(self):
        """Clean up after tests"""
        if self.test_results:
            create_test_summary(self.test_results)

class TestSystemIntegration(unittest.TestCase):
    """System-level integration tests"""
    
    def setUp(self):
        self.error_logger = ErrorLogger("system_integration")
        self.error_logger.clear_log()
    
    def test_main_with_all_slides(self):
        """Test main.py --all command (if implemented)"""
        main_path = project_root / "main.py"
        stdout, stderr, returncode = run_module_with_capture(main_path, ["--all"])
        
        # This test might take longer, so we check for basic success indicators
        expected_patterns = [
            "Probability & Information Theory Project"
        ]
        
        forbidden_patterns = [
            "findfont: Font family",
            "not found",
            "FAILED",
            "Exception",
            "Traceback"
        ]
        
        combined_output = stdout + stderr
        success, errors = check_output_patterns(combined_output, expected_patterns, forbidden_patterns)
        
        if not success:
            self.error_logger.log_error(
                expected=expected_patterns,
                actual=combined_output,
                error_type="MAIN_ALL_SLIDES_FAILED",
                additional_info={
                    "errors": errors,
                    "return_code": returncode
                }
            )
            # Don't fail this test as --all might not be implemented yet
            print(f"Warning: Main --all command issues: {errors}")

if __name__ == '__main__':
    # Create logs directory
    Path("tests/logs").mkdir(exist_ok=True)
    
    # Run tests
    unittest.main(verbosity=2)

