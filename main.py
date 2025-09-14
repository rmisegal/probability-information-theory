#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Probability & Information Theory Project
Main entry point for the probability presentation project

Based on: Jon Krohn's Machine Learning Foundations series
Lecturer: Dr. Yoram Segal

Author: Manus AI System
Date: September 2025
"""

import sys
import os
import argparse
from pathlib import Path
from datetime import datetime
import pytz

# Project version and info
__version__ = "1.0.0"
__build_date__ = "2025-09-14"

# Add project path to PYTHONPATH
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Suppress matplotlib warnings
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module="matplotlib")
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")

def get_jerusalem_time():
    """Get current time in Jerusalem timezone"""
    jerusalem_tz = pytz.timezone('Asia/Jerusalem')
    return datetime.now(jerusalem_tz).strftime("%Y-%m-%d %H:%M:%S %Z")

def print_header():
    """Print application header with version info"""
    print("=" * 70)
    print("Probability & Information Theory Project")
    print(f"Version: {__version__}")
    print(f"Build Date: {__build_date__}")
    print(f"Current Time (Jerusalem): {get_jerusalem_time()}")
    print("Based on: Jon Krohn's Machine Learning Foundations series")
    print("Lecturer: Dr. Yoram Segal")
    print("=" * 70)

def import_slide_module(slide_number):
    """Import slide module by number"""
    try:
        slide_dir = f"slide{slide_number:02d}"
        module_name = f"{slide_dir}.{slide_dir}_main"
        module = __import__(module_name, fromlist=[slide_dir])
        return module
    except ImportError as e:
        print(f"Error importing slide {slide_number}: {e}")
        return None

def run_slide(slide_number):
    """Run specific slide"""
    print(f"Running slide {slide_number}...")
    print("=" * 50)
    print("NOTE: Graphs will open in separate windows.")
    print("      Close graph windows to continue execution.")
    print("=" * 50)
    
    module = import_slide_module(slide_number)
    if module and hasattr(module, 'main'):
        try:
            module.main()
            print(f"\nSlide {slide_number} completed successfully!")
            print("If graph windows are still open, please close them to continue.")
        except Exception as e:
            print(f"Error running slide {slide_number}: {e}")
    else:
        print(f"Module or main function not found for slide {slide_number}")

def run_all_slides():
    """Run all slides"""
    print("Running all slides...")
    print("=" * 60)
    print("IMPORTANT: Each slide will open graph windows.")
    print("           Close each graph window to proceed to the next slide.")
    print("=" * 60)
    
    for slide_num in range(1, 11):
        print(f"\n{'='*20} Slide {slide_num} {'='*20}")
        run_slide(slide_num)
        print("\n" + "="*60)

def list_slides():
    """Display list of available slides"""
    slides_info = [
        (1, "Introduction to Probability"),
        (2, "Uniform Distribution"),
        (3, "Normal Distribution"),
        (4, "Binomial Distribution"),
        (5, "Poisson Distribution"),
        (6, "Measures of Central Tendency"),
        (7, "Measures of Dispersion"),
        (8, "Correlation and Correlation Matrix"),
        (9, "Shannon Entropy"),
        (10, "KL Divergence and Cross-Entropy")
    ]
    
    print("Available Slides:")
    print("-" * 40)
    for num, title in slides_info:
        print(f"{num:2d}. {title}")

def run_tests():
    """Run all tests including advanced output validation tests"""
    print("Running tests...")
    print("NOTE: Tests may open graph windows briefly.")
    print("      These will close automatically.")
    print("      Advanced tests include output validation and error logging.")
    print("-" * 50)
    
    import subprocess
    
    try:
        # Run all test files including advanced ones
        test_files = [
            "tests/test_slide01.py",
            "tests/test_slide02.py", 
            "tests/test_slide01_advanced.py",
            "tests/test_main_advanced.py",
            "tests/test_all_slides_advanced.py"
        ]
        
        all_passed = True
        
        for test_file in test_files:
            if Path(test_file).exists():
                print(f"\nRunning {test_file}...")
                result = subprocess.run([
                    sys.executable, "-m", "pytest", test_file, "-v", "--tb=short"
                ], capture_output=True, text=True, cwd=project_root)
                
                if result.returncode == 0:
                    print(f"✅ {test_file} - PASSED")
                else:
                    print(f"❌ {test_file} - FAILED")
                    print("STDOUT:", result.stdout[-500:])  # Last 500 chars
                    if result.stderr:
                        print("STDERR:", result.stderr[-500:])
                    all_passed = False
            else:
                print(f"⚠️  {test_file} - NOT FOUND")
        
        # Check for error logs
        logs_dir = Path("tests/logs")
        if logs_dir.exists():
            error_logs = list(logs_dir.glob("LOG_ERROR_*.json"))
            if error_logs:
                print(f"\n⚠️  Found {len(error_logs)} error log(s):")
                for log_file in error_logs:
                    print(f"   - {log_file}")
                print("   Check these files for detailed error information.")
        
        if all_passed:
            print("\n🎉 All tests passed successfully!")
        else:
            print("\n❌ Some tests failed. Check error logs for details.")
            
        return all_passed
        
    except Exception as e:
        print(f"Error running advanced tests: {e}")
        print("Falling back to basic test run...")
        
        # Fallback to basic pytest
        result = subprocess.run([
            sys.executable, "-m", "pytest", "tests/", "-v", "--tb=short"
        ], capture_output=True, text=True, cwd=project_root)
        
        print("Test Results:")
        print(result.stdout)
        if result.stderr:
            print("Errors:")
            print(result.stderr)
        
        return result.returncode == 0

def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description="Probability & Information Theory Project",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Usage Examples:
  python main.py --list                 # Show list of slides
  python main.py --slide 3              # Run slide 3
  python main.py --all                  # Run all slides
  python main.py --test                 # Run tests
        """
    )
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--slide', '-s', type=int, choices=range(1, 11),
                      help='Slide number to run (1-10)')
    group.add_argument('--all', '-a', action='store_true',
                      help='Run all slides')
    group.add_argument('--list', '-l', action='store_true',
                      help='Show list of slides')
    group.add_argument('--test', '-t', action='store_true',
                      help='Run tests')
    
    args = parser.parse_args()
    
    print_header()
    
    if args.list:
        list_slides()
    elif args.slide:
        run_slide(args.slide)
    elif args.all:
        run_all_slides()
    elif args.test:
        success = run_tests()
        sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()

