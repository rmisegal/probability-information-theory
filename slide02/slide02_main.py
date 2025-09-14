#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Slide 2: Uniform Distribution

Based on: Jon Krohn's Machine Learning Foundations series
Lecturer: Dr. Yoram Segal

Python code for uniform distribution analysis and visualization
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import webbrowser
import sys
from pathlib import Path

# Suppress matplotlib warnings
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module="matplotlib")
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")

# Set font support
plt.rcParams['font.family'] = ['DejaVu Sans', 'Arial Unicode MS', 'Tahoma']
plt.rcParams['axes.unicode_minus'] = False

def show_slide():
    """Display HTML slide"""
    slide_path = Path(__file__).parent / "slide2.html"
    if slide_path.exists():
        webbrowser.open(f"file://{slide_path.absolute()}")
        print("Slide opened in browser")
    else:
        print("Slide file not found")

def generate_uniform_data(a=0, b=10, n_samples=1000):
    """Generate uniform distribution data"""
    print(f"=== Generating {n_samples} samples from Uniform Distribution [{a}, {b}] ===")
    
    np.random.seed(42)
    uniform_data = np.random.uniform(a, b, n_samples)
    
    mean_theoretical = (a + b) / 2
    var_theoretical = (b - a) ** 2 / 12
    
    mean_empirical = np.mean(uniform_data)
    var_empirical = np.var(uniform_data)
    
    print(f"Theoretical mean: {mean_theoretical:.3f}")
    print(f"Empirical mean: {mean_empirical:.3f}")
    print(f"Theoretical variance: {var_theoretical:.3f}")
    print(f"Empirical variance: {var_empirical:.3f}")
    
    return uniform_data

def create_uniform_visualization():
    """Create uniform distribution visualization"""
    data = generate_uniform_data(0, 10, 1000)
    
    plt.figure(figsize=(12, 8))
    
    # Histogram
    plt.subplot(2, 2, 1)
    plt.hist(data, bins=20, density=True, alpha=0.7, color='#12377A', edgecolor='black')
    plt.axhline(y=0.1, color='red', linestyle='--', linewidth=2, label='Theoretical density = 0.1')
    plt.title('Histogram of Uniform Distribution')
    plt.xlabel('Values')
    plt.ylabel('Density')
    plt.legend()
    plt.grid(alpha=0.3)
    
    # Q-Q Plot
    plt.subplot(2, 2, 2)
    stats.probplot(data, dist=stats.uniform, sparams=(0, 10), plot=plt)
    plt.title('Q-Q Plot - Uniform Distribution Test')
    plt.grid(alpha=0.3)
    
    # Box Plot
    plt.subplot(2, 2, 3)
    plt.boxplot(data, vert=True, patch_artist=True, 
                boxprops=dict(facecolor='#12377A', alpha=0.7))
    plt.title('Box Plot')
    plt.ylabel('Values')
    plt.grid(alpha=0.3)
    
    # CDF
    plt.subplot(2, 2, 4)
    x_sorted = np.sort(data)
    y_empirical = np.arange(1, len(x_sorted) + 1) / len(x_sorted)
    plt.plot(x_sorted, y_empirical, label='Empirical CDF', linewidth=2)
    
    x_theoretical = np.linspace(0, 10, 100)
    y_theoretical = x_theoretical / 10
    plt.plot(x_theoretical, y_theoretical, 'r--', label='Theoretical CDF', linewidth=2)
    
    plt.title('Cumulative Distribution Function (CDF)')
    plt.xlabel('Values')
    plt.ylabel('Cumulative Probability')
    plt.legend()
    plt.grid(alpha=0.3)
    
    plt.tight_layout()
    
    # Save the plot
    output_path = Path(__file__).parent / "uniform_distribution.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Plot saved to: {output_path}")
    
    plt.show()

def uniform_properties_analysis():
    """Analyze properties of uniform distribution"""
    print("\n=== Uniform Distribution Properties ===")
    
    # Different uniform distributions
    distributions = [
        (0, 1, "Standard Uniform"),
        (5, 15, "Uniform [5,15]"),
        (-10, 10, "Symmetric Uniform"),
        (0, 100, "Wide Range Uniform")
    ]
    
    print("Distribution Properties:")
    print("-" * 60)
    print(f"{'Range':<15} {'Mean':<8} {'Variance':<10} {'Std Dev':<8} {'Description'}")
    print("-" * 60)
    
    for a, b, desc in distributions:
        mean = (a + b) / 2
        variance = (b - a) ** 2 / 12
        std_dev = np.sqrt(variance)
        
        print(f"[{a:>2}, {b:>2}]      {mean:>6.1f}   {variance:>8.2f}   {std_dev:>6.2f}   {desc}")

def interactive_menu():
    """Interactive menu"""
    while True:
        print("\n" + "="*50)
        print("Slide 2: Uniform Distribution")
        print("="*50)
        print("1. Show HTML slide")
        print("2. Generate uniform data")
        print("3. Create visualization")
        print("4. Analyze properties")
        print("5. Run all")
        print("0. Exit")
        
        choice = input("\nChoose option (0-5): ").strip()
        
        if choice == '0':
            print("Exiting...")
            break
        elif choice == '1':
            show_slide()
        elif choice == '2':
            generate_uniform_data(0, 10, 1000)
        elif choice == '3':
            create_uniform_visualization()
        elif choice == '4':
            uniform_properties_analysis()
        elif choice == '5':
            main()
        else:
            print("Invalid choice. Please try again.")

def main():
    """Main function"""
    print("Slide 2: Uniform Distribution")
    print("Lecturer: Dr. Yoram Segal")
    print("=" * 40)
    
    # Generate uniform data
    uniform_data = generate_uniform_data(0, 10, 1000)
    
    # Create visualizations
    create_uniform_visualization()
    
    # Analyze properties
    uniform_properties_analysis()
    
    print("\nSlide 2 demonstration completed")

if __name__ == "__main__":
    # Check if running directly or through main.py
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        interactive_menu()
    else:
        main()

