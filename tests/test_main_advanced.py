#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advanced Tests for Main Program
Includes output capture and error logging
"""

import unittest
import sys
from pathlib import Path

# Add project path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from tests.test_utils import OutputCapture, ErrorLogger, run_module_with_capture, check_output_patterns

class TestMainAdvanced(unittest.TestCase):
    """Advanced tests for main program with output validation"""
    
    def setUp(self):
        """Set up test environment"""
        self.error_logger = ErrorLogger("main_advanced")
        self.error_logger.clear_log()
        self.main_path = project_root / "main.py"
    
    def test_main_list_command(self):
        """Test main.py --list command output"""
        stdout, stderr, returncode = run_module_with_capture(self.main_path, ["--list"])
        
        expected_patterns = [
            "======================================================================",
            "Probability & Information Theory Project",
            "Version: 1.0.0",
            "Build Date: 2025-09-14",
            "Current Time (Jerusalem):",
            "Based on: Jon Krohn's Machine Learning Foundations series",
            "Lecturer: Dr. Yoram Segal",
            "======================================================================",
            "Available Slides:",
            "1. Introduction to Probability",
            "2. Uniform Distribution",
            "3. Normal Distribution",
            "4. Binomial Distribution",
            "5. Poisson Distribution"
        ]
        
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
            self.error_logger.log_error(
                expected=expected_patterns,
                actual=combined_output,
                error_type="MAIN_LIST_FAILED",
                additional_info={
                    "errors": errors,
                    "return_code": returncode,
                    "stdout": stdout,
                    "stderr": stderr
                }
            )
            self.fail(f"Main --list failed. Return code: {returncode}, Errors: {errors}")
    
    def test_main_version_info(self):
        """Test that version information is displayed correctly"""
        stdout, stderr, returncode = run_module_with_capture(self.main_path, ["--list"])
        
        version_patterns = [
            "Version: 1.0.0",
            "Build Date: 2025-09-14",
            "Current Time (Jerusalem):",
            "IDT" or "IST"  # Israel timezone
        ]
        
        combined_output = stdout + stderr
        
        missing_patterns = []
        for pattern in version_patterns:
            if pattern not in combined_output:
                missing_patterns.append(pattern)
        
        if missing_patterns:
            self.error_logger.log_error(
                expected=version_patterns,
                actual=combined_output,
                error_type="VERSION_INFO_MISSING",
                additional_info={"missing_patterns": missing_patterns}
            )
            self.fail(f"Version information missing: {missing_patterns}")
    
    def test_main_test_command(self):
        """Test main.py --test command"""
        stdout, stderr, returncode = run_module_with_capture(self.main_path, ["--test"])
        
        expected_patterns = [
            "Running tests...",
            "test session starts",
            "passed"
        ]
        
        forbidden_patterns = [
            "findfont: Font family",
            "FAILED",
            "ERROR",
            "Exception",
            "Traceback"
        ]
        
        combined_output = stdout + stderr
        success, errors = check_output_patterns(combined_output, expected_patterns, forbidden_patterns)
        
        if not success or returncode != 0:
            self.error_logger.log_error(
                expected=expected_patterns,
                actual=combined_output,
                error_type="MAIN_TEST_FAILED",
                additional_info={
                    "errors": errors,
                    "return_code": returncode,
                    "stdout": stdout,
                    "stderr": stderr
                }
            )
            self.fail(f"Main --test failed. Return code: {returncode}, Errors: {errors}")
    
    def test_main_slide_execution(self):
        """Test main.py --slide 1 command"""
        stdout, stderr, returncode = run_module_with_capture(self.main_path, ["--slide", "1"])
        
        expected_patterns = [
            "Running Slide 1: Introduction to Probability",
            "=== Dice Probability Calculations ===",
            "Slide 1 completed successfully"
        ]
        
        forbidden_patterns = [
            "findfont: Font family",
            "not found",
            "ERROR",
            "Exception",
            "Traceback"
        ]
        
        combined_output = stdout + stderr
        success, errors = check_output_patterns(combined_output, expected_patterns, forbidden_patterns)
        
        if not success or returncode != 0:
            self.error_logger.log_error(
                expected=expected_patterns,
                actual=combined_output,
                error_type="MAIN_SLIDE_EXECUTION_FAILED",
                additional_info={
                    "errors": errors,
                    "return_code": returncode,
                    "stdout": stdout,
                    "stderr": stderr
                }
            )
            self.fail(f"Main slide execution failed. Return code: {returncode}, Errors: {errors}")
    
    def test_main_help_command(self):
        """Test main.py --help command"""
        stdout, stderr, returncode = run_module_with_capture(self.main_path, ["--help"])
        
        expected_patterns = [
            "usage:",
            "--list",
            "--slide",
            "--test",
            "--all"
        ]
        
        combined_output = stdout + stderr
        success, errors = check_output_patterns(combined_output, expected_patterns)
        
        if not success:
            self.error_logger.log_error(
                expected=expected_patterns,
                actual=combined_output,
                error_type="MAIN_HELP_FAILED",
                additional_info={"errors": errors}
            )
            self.fail(f"Main --help failed. Errors: {errors}")
    
    def test_main_invalid_command(self):
        """Test main.py with invalid command"""
        stdout, stderr, returncode = run_module_with_capture(self.main_path, ["--invalid"])
        
        # Should show error message and help
        expected_patterns = [
            "error:",
            "usage:"
        ]
        
        combined_output = stdout + stderr
        success, errors = check_output_patterns(combined_output, expected_patterns)
        
        # Return code should be non-zero for invalid command
        if returncode == 0:
            self.error_logger.log_error(
                expected="Non-zero return code",
                actual=f"Return code: {returncode}",
                error_type="INVALID_COMMAND_HANDLING"
            )
            self.fail("Invalid command should return non-zero exit code")
        
        if not success:
            self.error_logger.log_error(
                expected=expected_patterns,
                actual=combined_output,
                error_type="INVALID_COMMAND_OUTPUT",
                additional_info={"errors": errors}
            )
            self.fail(f"Invalid command output validation failed: {errors}")

class TestMainCredits(unittest.TestCase):
    """Test credit and attribution display"""
    
    def setUp(self):
        self.error_logger = ErrorLogger("main_credits")
        self.error_logger.clear_log()
        self.main_path = project_root / "main.py"
    
    def test_credits_display(self):
        """Test that all required credits are displayed"""
        stdout, stderr, returncode = run_module_with_capture(self.main_path, ["--list"])
        
        required_credits = [
            "Based on: Jon Krohn's Machine Learning Foundations series",
            "Lecturer: Dr. Yoram Segal"
        ]
        
        combined_output = stdout + stderr
        
        missing_credits = []
        for credit in required_credits:
            if credit not in combined_output:
                missing_credits.append(credit)
        
        if missing_credits:
            self.error_logger.log_error(
                expected=required_credits,
                actual=combined_output,
                error_type="CREDITS_MISSING",
                additional_info={"missing_credits": missing_credits}
            )
            self.fail(f"Required credits missing: {missing_credits}")

if __name__ == '__main__':
    # Create logs directory
    Path("tests/logs").mkdir(exist_ok=True)
    
    # Run tests
    unittest.main(verbosity=2)

