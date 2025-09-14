#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
שקף 1: מבוא להסתברות
Slide 1: Introduction to Probability

מבוסס על: Jon Krohn's Machine Learning Foundations series
Based on: Jon Krohn's Machine Learning Foundations series
This is the companion code to lectures and videos from Jon Krohn's Machine Learning Foundations series

קוד Python לחישוב הסתברויות בסיסיות וויזואליזציה של זריקת קובייה
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import webbrowser
import os
from pathlib import Path

# הגדרת פונט עברי
plt.rcParams['font.family'] = ['DejaVu Sans', 'Arial Unicode MS', 'Tahoma']
plt.rcParams['axes.unicode_minus'] = False

def show_slide():
    """הצגת השקף HTML"""
    slide_path = Path(__file__).parent / "slide1.html"
    if slide_path.exists():
        webbrowser.open(f"file://{slide_path.absolute()}")
        print("השקף נפתח בדפדפן")
    else:
        print("קובץ השקף לא נמצא")

def calculate_dice_probabilities():
    """חישוב הסתברויות זריקת קובייה הוגנת"""
    print("=== חישוב הסתברויות זריקת קובייה ===")
    
    # הגדרת תוצאות אפשריות
    outcomes = ['1', '2', '3', '4', '5', '6']
    
    # חישוב הסתברות לכל תוצאה
    probability = 1 / len(outcomes)
    print(f"הסתברות לכל תוצאה: {probability:.3f}")
    
    # הסתברות לקבלת מספר זוגי
    even_outcomes = ['2', '4', '6']
    prob_even = len(even_outcomes) / len(outcomes)
    print(f"הסתברות למספר זוגי: {prob_even:.3f}")
    
    # הסתברות לקבלת מספר אי-זוגי
    odd_outcomes = ['1', '3', '5']
    prob_odd = len(odd_outcomes) / len(outcomes)
    print(f"הסתברות למספר אי-זוגי: {prob_odd:.3f}")
    
    # הסתברות לקבלת מספר גדול מ-4
    high_outcomes = ['5', '6']
    prob_high = len(high_outcomes) / len(outcomes)
    print(f"הסתברות למספר גדול מ-4: {prob_high:.3f}")
    
    return outcomes, [probability] * len(outcomes)

def create_dice_visualization():
    """יצירת ויזואליזציה של הסתברויות זריקת קובייה"""
    outcomes, probabilities = calculate_dice_probabilities()
    
    # יצירת הגרף
    plt.figure(figsize=(10, 6))
    bars = plt.bar(outcomes, probabilities, color='#12377A', alpha=0.8, edgecolor='#0f2d5f', linewidth=2)
    
    # הוספת ערכים על העמודות
    for bar, prob in zip(bars, probabilities):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.005,
                f'{prob:.3f}', ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    # עיצוב הגרף
    plt.title('הסתברות זריקת קובייה הוגנת', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('תוצאת הקובייה', fontsize=14)
    plt.ylabel('הסתברות', fontsize=14)
    plt.ylim(0, 0.2)
    plt.grid(axis='y', alpha=0.3)
    
    # הוספת קו ממוצע
    plt.axhline(y=1/6, color='red', linestyle='--', alpha=0.7, label='הסתברות תיאורטית')
    plt.legend()
    
    plt.tight_layout()
    
    # שמירת הגרף
    output_path = Path(__file__).parent / "dice_probability_chart.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"הגרף נשמר ב: {output_path}")
    
    plt.show()
    
    return plt.gcf()

def simulate_dice_rolls(n_rolls=1000):
    """סימולציה של זריקות קובייה"""
    print(f"\n=== סימולציה של {n_rolls} זריקות קובייה ===")
    
    # סימולציה
    np.random.seed(42)  # לתוצאות עקביות
    rolls = np.random.randint(1, 7, n_rolls)
    
    # חישוב תדירויות
    unique, counts = np.unique(rolls, return_counts=True)
    frequencies = counts / n_rolls
    
    print("תוצאות הסימולציה:")
    for outcome, freq in zip(unique, frequencies):
        print(f"  {outcome}: {freq:.3f} (תיאורטי: 0.167)")
    
    # יצירת השוואה ויזואלית
    plt.figure(figsize=(12, 5))
    
    # גרף 1: תדירויות מהסימולציה
    plt.subplot(1, 2, 1)
    plt.bar(unique, frequencies, color='#059669', alpha=0.8, label='סימולציה')
    plt.axhline(y=1/6, color='red', linestyle='--', alpha=0.7, label='תיאורטי')
    plt.title('תדירויות מסימולציה')
    plt.xlabel('תוצאת הקובייה')
    plt.ylabel('תדירות')
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    
    # גרף 2: היסטוגרמה של כל הזריקות
    plt.subplot(1, 2, 2)
    plt.hist(rolls, bins=np.arange(0.5, 7.5, 1), color='#DC2626', alpha=0.7, edgecolor='black')
    plt.title(f'היסטוגרמה של {n_rolls} זריקות')
    plt.xlabel('תוצאת הקובייה')
    plt.ylabel('מספר זריקות')
    plt.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    
    # שמירת הגרף
    output_path = Path(__file__).parent / "dice_simulation.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"גרף הסימולציה נשמר ב: {output_path}")
    
    plt.show()
    
    return rolls, frequencies

def probability_rules_examples():
    """דוגמאות לחוקי הסתברות"""
    print("\n=== חוקי הסתברות בסיסיים ===")
    
    # חוק החיבור (אירועים זרים)
    prob_even = 3/6  # זוגי
    prob_odd = 3/6   # אי-זוגי
    prob_all = prob_even + prob_odd
    print(f"P(זוגי) + P(אי-זוגי) = {prob_even:.3f} + {prob_odd:.3f} = {prob_all:.3f}")
    
    # הסתברות משלימה
    prob_not_six = 1 - (1/6)
    print(f"P(לא 6) = 1 - P(6) = 1 - {1/6:.3f} = {prob_not_six:.3f}")
    
    # הסתברות מותנית (בהנחה שהתוצאה זוגית)
    prob_six_given_even = 1/3  # מתוך 3 מספרים זוגיים, אחד הוא 6
    print(f"P(6|זוגי) = {prob_six_given_even:.3f}")

def interactive_menu():
    """תפריט אינטראקטיבי"""
    while True:
        print("\n" + "="*50)
        print("שקף 1: מבוא להסתברות")
        print("="*50)
        print("1. הצג שקף HTML")
        print("2. חשב הסתברויות בסיסיות")
        print("3. צור ויזואליזציה")
        print("4. הרץ סימולציה")
        print("5. דוגמאות לחוקי הסתברות")
        print("6. הרץ הכל")
        print("0. יציאה")
        
        choice = input("\nבחר אפשרות (0-6): ").strip()
        
        if choice == '0':
            print("יציאה...")
            break
        elif choice == '1':
            show_slide()
        elif choice == '2':
            calculate_dice_probabilities()
        elif choice == '3':
            create_dice_visualization()
        elif choice == '4':
            simulate_dice_rolls(1000)
        elif choice == '5':
            probability_rules_examples()
        elif choice == '6':
            main()
        else:
            print("בחירה לא חוקית. נסה שוב.")

def main():
    """פונקציה ראשית"""
    print("שקף 1: מבוא להסתברות")
    print("מבוסס על: Jon Krohn's Machine Learning Foundations series")
    print("=" * 60)
    
    # חישוב הסתברויות בסיסיות
    calculate_dice_probabilities()
    
    # יצירת ויזואליזציה
    create_dice_visualization()
    
    # סימולציה
    simulate_dice_rolls(1000)
    
    # דוגמאות לחוקי הסתברות
    probability_rules_examples()
    
    print("\nסיום הדגמה - שקף 1")

if __name__ == "__main__":
    # בדיקה אם הקובץ מורץ ישירות או דרך main.py
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        interactive_menu()
    else:
        main()

