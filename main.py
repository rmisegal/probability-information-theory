#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
פרויקט הסתברות ותורת המידע
Main entry point for the probability presentation project

מבוסס על: Jon Krohn's Machine Learning Foundations series
Based on: Jon Krohn's Machine Learning Foundations series
This is the companion code to lectures and videos from Jon Krohn's Machine Learning Foundations series

מרצה: דר. יורם סגל
Lecturer: Dr. Yoram Segal

מחבר: מערכת Manus AI
תאריך: ספטמבר 2025
"""

import sys
import os
import argparse
from pathlib import Path

# הוספת נתיב הפרויקט ל-PYTHONPATH
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def import_slide_module(slide_number):
    """ייבוא מודול שקף לפי מספר"""
    try:
        slide_dir = f"slide{slide_number:02d}"
        module_name = f"{slide_dir}.{slide_dir}_main"
        module = __import__(module_name, fromlist=[slide_dir])
        return module
    except ImportError as e:
        print(f"שגיאה בייבוא שקף {slide_number}: {e}")
        return None

def run_slide(slide_number):
    """הרצת שקף ספציפי"""
    print(f"מריץ שקף {slide_number}...")
    print("=" * 50)
    
    module = import_slide_module(slide_number)
    if module and hasattr(module, 'main'):
        try:
            module.main()
            print(f"\nשקף {slide_number} הושלם בהצלחה!")
        except Exception as e:
            print(f"שגיאה בהרצת שקף {slide_number}: {e}")
    else:
        print(f"לא נמצא מודול או פונקציית main עבור שקף {slide_number}")

def run_all_slides():
    """הרצת כל השקפים"""
    print("מריץ את כל השקפים...")
    print("=" * 60)
    
    for slide_num in range(1, 11):
        print(f"\n{'='*20} שקף {slide_num} {'='*20}")
        run_slide(slide_num)
        print("\n" + "="*60)

def list_slides():
    """הצגת רשימת השקפים הזמינים"""
    slides_info = [
        (1, "מבוא להסתברות"),
        (2, "התפלגות אחידה"),
        (3, "התפלגות נורמלית"),
        (4, "התפלגות בינומית"),
        (5, "התפלגות פואסון"),
        (6, "מדדי נטייה מרכזית"),
        (7, "מדדי פיזור"),
        (8, "מתאם וקורלציה"),
        (9, "אנטרופיה של שאנון"),
        (10, "דיברגנס KL ואנטרופיה צולבת")
    ]
    
    print("שקפים זמינים:")
    print("-" * 40)
    for num, title in slides_info:
        print(f"{num:2d}. {title}")

def run_tests():
    """הרצת כל הטסטים"""
    print("מריץ טסטים...")
    import subprocess
    
    try:
        result = subprocess.run([
            sys.executable, "-m", "pytest", "tests/", "-v"
        ], capture_output=True, text=True, cwd=project_root)
        
        print("תוצאות הטסטים:")
        print(result.stdout)
        if result.stderr:
            print("שגיאות:")
            print(result.stderr)
        
        return result.returncode == 0
    except Exception as e:
        print(f"שגיאה בהרצת הטסטים: {e}")
        return False

def main():
    """פונקציה ראשית"""
    parser = argparse.ArgumentParser(
        description="פרויקט הסתברות ותורת המידע",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
דוגמאות שימוש:
  python main.py --list                 # הצגת רשימת השקפים
  python main.py --slide 3              # הרצת שקף 3
  python main.py --all                  # הרצת כל השקפים
  python main.py --test                 # הרצת טסטים
        """
    )
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--slide', '-s', type=int, choices=range(1, 11),
                      help='מספר השקף להרצה (1-10)')
    group.add_argument('--all', '-a', action='store_true',
                      help='הרצת כל השקפים')
    group.add_argument('--list', '-l', action='store_true',
                      help='הצגת רשימת השקפים')
    group.add_argument('--test', '-t', action='store_true',
                      help='הרצת טסטים')
    
    args = parser.parse_args()
    
    print("פרויקט הסתברות ותורת המידע")
    print("=" * 40)
    
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

