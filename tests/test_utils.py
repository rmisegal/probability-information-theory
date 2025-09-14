#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Utilities for Output Capture and Error Logging
"""

import sys
import io
import contextlib
import subprocess
import json
from datetime import datetime
from pathlib import Path
import warnings

# Suppress matplotlib warnings in tests
warnings.filterwarnings("ignore", category=DeprecationWarning, module="matplotlib")
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
warnings.filterwarnings("ignore", message="findfont: Font family.*not found")

class OutputCapture:
    """Utility class for capturing stdout and stderr"""
    
    def __init__(self):
        self.stdout = io.StringIO()
        self.stderr = io.StringIO()
        self.original_stdout = sys.stdout
        self.original_stderr = sys.stderr
    
    def __enter__(self):
        sys.stdout = self.stdout
        sys.stderr = self.stderr
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.original_stdout
        sys.stderr = self.original_stderr
    
    def get_stdout(self):
        """Get captured stdout"""
        return self.stdout.getvalue()
    
    def get_stderr(self):
        """Get captured stderr"""
        return self.stderr.getvalue()
    
    def get_combined(self):
        """Get combined stdout and stderr"""
        return self.get_stdout() + self.get_stderr()

class ErrorLogger:
    """Utility class for logging test errors"""
    
    def __init__(self, test_name, log_dir="tests/logs"):
        self.test_name = test_name
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)
        self.log_file = self.log_dir / f"LOG_ERROR_{test_name}.json"
    
    def log_error(self, expected, actual, error_type="OUTPUT_MISMATCH", additional_info=None):
        """Log error details to JSON file"""
        error_data = {
            "timestamp": datetime.now().isoformat(),
            "test_name": self.test_name,
            "error_type": error_type,
            "expected": expected,
            "actual": actual,
            "additional_info": additional_info or {}
        }
        
        with open(self.log_file, 'w', encoding='utf-8') as f:
            json.dump(error_data, f, indent=2, ensure_ascii=False)
        
        print(f"ERROR LOG CREATED: {self.log_file}")
        return self.log_file
    
    def clear_log(self):
        """Clear existing log file"""
        if self.log_file.exists():
            self.log_file.unlink()

def run_module_with_capture(module_path, args=None):
    """Run a Python module and capture its output"""
    cmd = [sys.executable, str(module_path)]
    if args:
        cmd.extend(args)
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=Path(module_path).parent
        )
        return result.stdout, result.stderr, result.returncode
    except subprocess.TimeoutExpired:
        return "", "TIMEOUT: Process took longer than 30 seconds", 1
    except Exception as e:
        return "", f"ERROR: {str(e)}", 1

def check_output_patterns(output, expected_patterns, forbidden_patterns=None):
    """
    Check if output contains expected patterns and doesn't contain forbidden ones
    
    Args:
        output: The actual output string
        expected_patterns: List of strings that should be in output
        forbidden_patterns: List of strings that should NOT be in output
    
    Returns:
        tuple: (success: bool, errors: list)
    """
    errors = []
    
    # Check expected patterns
    for pattern in expected_patterns:
        if pattern not in output:
            errors.append(f"MISSING: Expected '{pattern}' not found in output")
    
    # Check forbidden patterns
    if forbidden_patterns:
        for pattern in forbidden_patterns:
            if pattern in output:
                errors.append(f"FORBIDDEN: Found '{pattern}' in output (should not be present)")
    
    return len(errors) == 0, errors

def create_test_summary(test_results):
    """Create a summary of all test results"""
    summary_file = Path("tests/logs/TEST_SUMMARY.json")
    summary_file.parent.mkdir(exist_ok=True)
    
    summary = {
        "timestamp": datetime.now().isoformat(),
        "total_tests": len(test_results),
        "passed": sum(1 for r in test_results if r["status"] == "PASSED"),
        "failed": sum(1 for r in test_results if r["status"] == "FAILED"),
        "results": test_results
    }
    
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    
    return summary_file

