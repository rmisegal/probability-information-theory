#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Slide 6: Measures of Central Tendency
Based on: Jon Krohn's Machine Learning Foundations series
Lecturer: Dr. Yoram Segal
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import warnings
from pathlib import Path
import webbrowser

# Configure matplotlib to completely suppress font warnings
import logging
logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)
logging.getLogger("matplotlib").setLevel(logging.ERROR)

# Use only available fonts
matplotlib.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans'],
    'font.size': 10
})

# Suppress all warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family': 'sans-serif', 'font.sans-serif': ['DejaVu Sans']})

# Set non-interactive backend if running in test environment
if 'pytest' in str(Path(__file__).parent):
    matplotlib.use('Agg')

def show_slide():
    """Open the HTML slide in browser"""
    try:
        slide_path = Path(__file__).parent / "slide6.html"
        if slide_path.exists():
            webbrowser.open(f"file://{slide_path.absolute()}")
            print(f"Slide opened in browser: {slide_path}")
        else:
            print(f"HTML slide not found: {slide_path}")
    except Exception as e:
        print(f"Error opening slide: {e}")

def main():
    """Main demonstration function"""
    print("Slide 6: Measures of Central Tendency")
    print("Lecturer: Dr. Yoram Segal")
    print("=" * 50)
    
    print("\n=== Measures of Central Tendency Demonstration ===")
    
    # Generate sample data
    data = np.random.normal(0, 1, 1000)
    
    # Create a simple plot
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=30, alpha=0.7, color='skyblue')
    plt.title('Measures of Central Tendency')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    
    # Save plot
    save_path = Path(__file__).parent / "slide6_plot.png"
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Plot saved to: {save_path}")
    
    # Show plot if not in test mode
    if matplotlib.get_backend() != 'Agg':
        plt.show()
    
    plt.close()
    
    print(f"\nSlide 6 demonstration completed")

if __name__ == "__main__":
    main()
