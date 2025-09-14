#!/usr/bin/env python3
"""
Slide 2b: Histogram of Uniform Distribution
Lecturer: Dr. Yoram Segal
Based on: Jon Krohn's Machine Learning Foundations series
"""

import matplotlib.pyplot as plt
import numpy as np
import warnings
import logging

# Suppress matplotlib warnings
warnings.filterwarnings('ignore')
logging.getLogger('matplotlib').setLevel(logging.ERROR)
plt.rcParams['font.family'] = ['DejaVu Sans']

def create_uniform_histogram():
    """
    Create histogram of uniform distribution
    Shows how uniform data appears in histogram form
    """
    print("=== Histogram of Uniform Distribution ===")
    
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Generate uniform data
    print("Generating 1000 uniform random samples between 0 and 10...")
    uniform_data = np.random.uniform(0, 10, 1000)
    
    # Create histogram
    plt.figure(figsize=(10, 6))
    counts, bins, patches = plt.hist(uniform_data, bins=20, alpha=0.7, 
                                   edgecolor='black', color='skyblue')
    
    # Add data labels on top of bars
    for i, count in enumerate(counts):
        plt.text(bins[i] + (bins[1]-bins[0])/2, count + 1, 
                str(int(count)), ha='center', fontsize=8, fontweight='bold')
    
    plt.xlabel('Value Range')
    plt.ylabel('Frequency')
    plt.title('Histogram of Uniform Distribution (1000 samples)')
    plt.grid(True, alpha=0.3)
    
    # Add theoretical expectation line
    expected_count = len(uniform_data) / len(counts)
    plt.axhline(y=expected_count, color='red', linestyle='--', 
                label=f'Expected: {expected_count:.1f}')
    plt.legend()
    
    # Statistical analysis
    print(f"\nStatistical Analysis:")
    print(f"Total samples: {len(uniform_data)}")
    print(f"Number of bins: {len(counts)}")
    print(f"Expected count per bin: {expected_count:.1f}")
    print(f"Actual counts range: {int(min(counts))} - {int(max(counts))}")
    print(f"Standard deviation of counts: {np.std(counts):.2f}")
    
    # Uniformity test
    chi_square = np.sum((counts - expected_count)**2 / expected_count)
    print(f"Chi-square statistic: {chi_square:.3f}")
    print(f"Degrees of freedom: {len(counts) - 1}")
    
    plt.tight_layout()
    plt.show()
    
    return uniform_data, counts, bins

def analyze_bin_distribution(counts, bins):
    """
    Analyze the distribution of data across bins
    """
    print("\n=== Bin Distribution Analysis ===")
    
    bin_width = bins[1] - bins[0]
    print(f"Bin width: {bin_width:.2f}")
    
    for i, count in enumerate(counts):
        bin_start = bins[i]
        bin_end = bins[i+1]
        print(f"Bin {i+1:2d}: [{bin_start:4.1f} - {bin_end:4.1f}] = {int(count):3d} samples")

def demonstrate_uniform_properties():
    """
    Demonstrate key properties of uniform distribution histogram
    """
    print("\n=== Uniform Distribution Properties ===")
    print("1. HISTOGRAM CHARACTERISTICS:")
    print("   - All bins should have approximately equal height")
    print("   - Height variations are due to random sampling")
    print("   - More samples → more uniform appearance")
    
    print("\n2. MATHEMATICAL PROPERTIES:")
    print("   - Probability density function: f(x) = 1/(b-a)")
    print("   - For range [0,10]: f(x) = 1/10 = 0.1")
    print("   - Expected frequency per bin = Total_samples / Number_of_bins")
    
    print("\n3. PYTHON CODE EXPLANATION:")
    print("   - np.random.uniform(0, 10, 1000): Generate 1000 uniform samples")
    print("   - plt.hist(data, bins=20): Create histogram with 20 bins")
    print("   - bins parameter controls granularity of the histogram")

def main():
    """
    Main function to demonstrate uniform distribution histogram
    """
    print("Slide 2b: Histogram of Uniform Distribution")
    print("Lecturer: Dr. Yoram Segal")
    print("=" * 50)
    
    # Create and analyze histogram
    uniform_data, counts, bins = create_uniform_histogram()
    
    # Analyze bin distribution
    analyze_bin_distribution(counts, bins)
    
    # Demonstrate properties
    demonstrate_uniform_properties()
    
    print("\nSlide 2b demonstration completed")
    print("This slide shows how uniform data appears in histogram form")
    print("and demonstrates the key characteristics of uniform distribution.")

if __name__ == "__main__":
    main()

