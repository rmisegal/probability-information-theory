#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
שקף 2: התפלגות אחידה
Slide 2: Uniform Distribution

מבוסס על: Jon Krohn's Machine Learning Foundations series
מרצה: דר. יורם סגל
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import webbrowser
from pathlib import Path

plt.rcParams['font.family'] = ['DejaVu Sans', 'Arial Unicode MS', 'Tahoma']

def show_slide():
    """הצגת השקף HTML"""
    slide_path = Path(__file__).parent / "slide2.html"
    if slide_path.exists():
        webbrowser.open(f"file://{slide_path.absolute()}")
        print("השקף נפתח בדפדפן")
    else:
        print("קובץ השקף לא נמצא")

def generate_uniform_data(a=0, b=10, n_samples=1000):
    """יצירת נתונים מהתפלגות אחידה"""
    print(f"=== יצירת {n_samples} דגימות מהתפלגות אחידה [{a}, {b}] ===")
    
    np.random.seed(42)
    uniform_data = np.random.uniform(a, b, n_samples)
    
    mean_theoretical = (a + b) / 2
    var_theoretical = (b - a) ** 2 / 12
    
    mean_empirical = np.mean(uniform_data)
    var_empirical = np.var(uniform_data)
    
    print(f"ממוצע תיאורטי: {mean_theoretical:.3f}")
    print(f"ממוצע אמפירי: {mean_empirical:.3f}")
    print(f"שונות תיאורטית: {var_theoretical:.3f}")
    print(f"שונות אמפירית: {var_empirical:.3f}")
    
    return uniform_data

def create_uniform_visualization():
    """יצירת ויזואליזציה של התפלגות אחידה"""
    data = generate_uniform_data(0, 10, 1000)
    
    plt.figure(figsize=(12, 8))
    
    # היסטוגרמה
    plt.subplot(2, 2, 1)
    plt.hist(data, bins=20, density=True, alpha=0.7, color='#12377A', edgecolor='black')
    plt.axhline(y=0.1, color='red', linestyle='--', linewidth=2, label='צפיפות תיאורטית = 0.1')
    plt.title('היסטוגרמה של התפלגות אחידה')
    plt.xlabel('ערכים')
    plt.ylabel('צפיפות')
    plt.legend()
    plt.grid(alpha=0.3)
    
    # Q-Q Plot
    plt.subplot(2, 2, 2)
    stats.probplot(data, dist=stats.uniform, sparams=(0, 10), plot=plt)
    plt.title('Q-Q Plot - בדיקת התפלגות אחידה')
    plt.grid(alpha=0.3)
    
    # Box Plot
    plt.subplot(2, 2, 3)
    plt.boxplot(data, vert=True, patch_artist=True, 
                boxprops=dict(facecolor='#12377A', alpha=0.7))
    plt.title('Box Plot')
    plt.ylabel('ערכים')
    plt.grid(alpha=0.3)
    
    # CDF
    plt.subplot(2, 2, 4)
    x_sorted = np.sort(data)
    y_empirical = np.arange(1, len(x_sorted) + 1) / len(x_sorted)
    plt.plot(x_sorted, y_empirical, label='CDF אמפירי', linewidth=2)
    
    x_theoretical = np.linspace(0, 10, 100)
    y_theoretical = x_theoretical / 10
    plt.plot(x_theoretical, y_theoretical, 'r--', label='CDF תיאורטי', linewidth=2)
    
    plt.title('פונקציית התפלגות מצטברת (CDF)')
    plt.xlabel('ערכים')
    plt.ylabel('הסתברות מצטברת')
    plt.legend()
    plt.grid(alpha=0.3)
    
    plt.tight_layout()
    
    # שמירת הגרף
    output_path = Path(__file__).parent / "uniform_distribution.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"הגרף נשמר ב: {output_path}")
    
    plt.show()

def main():
    """פונקציה ראשית"""
    print("שקף 2: התפלגות אחידה")
    print("מרצה: דר. יורם סגל")
    print("=" * 40)
    
    # יצירת נתונים אחידים
    uniform_data = generate_uniform_data(0, 10, 1000)
    
    # יצירת ויזואליזציות
    create_uniform_visualization()
    
    print("\nסיום הדגמה - שקף 2")

if __name__ == "__main__":
    main()

