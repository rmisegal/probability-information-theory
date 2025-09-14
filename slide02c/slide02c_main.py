#!/usr/bin/env python3
"""
Slide 2c: Q-Q Plot - Uniform Distribution Test
Lecturer: Dr. Yoram Segal
Based on: Jon Krohn's Machine Learning Foundations series
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import warnings
import logging

# Suppress matplotlib warnings
warnings.filterwarnings('ignore')
logging.getLogger('matplotlib').setLevel(logging.ERROR)
plt.rcParams['font.family'] = ['DejaVu Sans']

def create_qq_plot():
    """
    Create Q-Q plot to test if data follows uniform distribution
    """
    print("=== Q-Q Plot: Uniform Distribution Test ===")
    
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Generate uniform data
    print("Generating 1000 uniform random samples between 0 and 10...")
    uniform_data = np.random.uniform(0, 10, 1000)
    
    # Sort the sample data
    sample_quantiles = np.sort(uniform_data)
    
    # Generate theoretical quantiles for uniform distribution
    n = len(sample_quantiles)
    theoretical_quantiles = np.linspace(0, 10, n)
    
    # Alternative: using percentiles
    percentiles = np.linspace(0.5/n, 1-0.5/n, n) * 100
    theoretical_quantiles_alt = np.percentile(np.random.uniform(0, 10, 10000), percentiles)
    
    # Create Q-Q plot
    plt.figure(figsize=(10, 8))
    
    # Scatter plot of quantiles
    plt.scatter(theoretical_quantiles, sample_quantiles, 
               alpha=0.6, s=20, color='blue', label='Sample vs Theoretical')
    
    # Perfect fit line (y = x)
    plt.plot([0, 10], [0, 10], 'r-', linewidth=2, 
             label='Perfect Fit (y=x)')
    
    # Calculate correlation coefficient
    correlation = np.corrcoef(theoretical_quantiles, sample_quantiles)[0,1]
    
    plt.xlabel('Theoretical Quantiles (Uniform Distribution)')
    plt.ylabel('Sample Quantiles')
    plt.title(f'Q-Q Plot: Uniform Distribution Test\nCorrelation: {correlation:.4f}')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Add diagonal reference lines
    plt.plot([0, 10], [0, 10], 'k--', alpha=0.3, linewidth=1)
    
    plt.tight_layout()
    plt.show()
    
    return correlation, theoretical_quantiles, sample_quantiles

def analyze_qq_plot_results(correlation, theoretical_quantiles, sample_quantiles):
    """
    Analyze the results of the Q-Q plot
    """
    print(f"\n=== Q-Q Plot Analysis ===")
    print(f"Correlation coefficient: {correlation:.4f}")
    
    # Interpretation of correlation
    if correlation > 0.99:
        interpretation = "Excellent fit - data very likely follows uniform distribution"
    elif correlation > 0.95:
        interpretation = "Good fit - data likely follows uniform distribution"
    elif correlation > 0.90:
        interpretation = "Moderate fit - some deviation from uniform distribution"
    else:
        interpretation = "Poor fit - data does not follow uniform distribution"
    
    print(f"Interpretation: {interpretation}")
    
    # Calculate deviations from perfect fit
    deviations = sample_quantiles - theoretical_quantiles
    mean_deviation = np.mean(np.abs(deviations))
    max_deviation = np.max(np.abs(deviations))
    
    print(f"Mean absolute deviation: {mean_deviation:.3f}")
    print(f"Maximum absolute deviation: {max_deviation:.3f}")
    
    # Kolmogorov-Smirnov test
    ks_statistic, p_value = stats.kstest(sample_quantiles, 'uniform', args=(0, 10))
    print(f"Kolmogorov-Smirnov test:")
    print(f"  KS statistic: {ks_statistic:.4f}")
    print(f"  p-value: {p_value:.4f}")
    
    if p_value > 0.05:
        print("  Result: Fail to reject null hypothesis - data appears uniform")
    else:
        print("  Result: Reject null hypothesis - data does not appear uniform")

def explain_qq_plot_concepts():
    """
    Explain the concepts behind Q-Q plots
    """
    print("\n=== Q-Q Plot Concepts ===")
    print("1. WHAT IS A Q-Q PLOT?")
    print("   - Quantile-Quantile plot compares two probability distributions")
    print("   - Plots quantiles of sample data vs theoretical distribution")
    print("   - If data follows the theoretical distribution, points lie on y=x line")
    
    print("\n2. HOW TO READ Q-Q PLOT:")
    print("   - X-axis: Theoretical quantiles (expected values)")
    print("   - Y-axis: Sample quantiles (observed values)")
    print("   - Straight line: Perfect match to theoretical distribution")
    print("   - Curved patterns: Systematic deviations from theoretical distribution")
    
    print("\n3. INTERPRETATION PATTERNS:")
    print("   - Points on diagonal: Good fit to distribution")
    print("   - S-shaped curve: Heavy tails (more extreme values)")
    print("   - Inverted S-curve: Light tails (fewer extreme values)")
    print("   - Systematic offset: Location parameter difference")
    
    print("\n4. PYTHON CODE EXPLANATION:")
    print("   - np.sort(): Sort sample data to get sample quantiles")
    print("   - np.linspace(): Generate evenly spaced theoretical quantiles")
    print("   - np.corrcoef(): Calculate correlation between quantiles")
    print("   - High correlation (>0.95) indicates good fit")

def demonstrate_different_distributions():
    """
    Show Q-Q plots for different distributions for comparison
    """
    print("\n=== Comparison with Other Distributions ===")
    
    np.random.seed(42)
    uniform_data = np.random.uniform(0, 10, 1000)
    normal_data = np.random.normal(5, 2, 1000)
    exponential_data = np.random.exponential(2, 1000)
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # Uniform vs Uniform (should be perfect)
    sample_q = np.sort(uniform_data)
    theoretical_q = np.linspace(0, 10, len(sample_q))
    axes[0].scatter(theoretical_q, sample_q, alpha=0.6, s=10)
    axes[0].plot([0, 10], [0, 10], 'r-', linewidth=2)
    axes[0].set_title('Uniform Data vs Uniform Distribution')
    axes[0].set_xlabel('Theoretical Quantiles')
    axes[0].set_ylabel('Sample Quantiles')
    axes[0].grid(True, alpha=0.3)
    
    # Normal vs Uniform (should show deviation)
    sample_q = np.sort(normal_data)
    theoretical_q = np.linspace(np.min(sample_q), np.max(sample_q), len(sample_q))
    axes[1].scatter(theoretical_q, sample_q, alpha=0.6, s=10, color='orange')
    axes[1].plot([np.min(sample_q), np.max(sample_q)], 
                [np.min(sample_q), np.max(sample_q)], 'r-', linewidth=2)
    axes[1].set_title('Normal Data vs Uniform Distribution')
    axes[1].set_xlabel('Theoretical Quantiles')
    axes[1].set_ylabel('Sample Quantiles')
    axes[1].grid(True, alpha=0.3)
    
    # Exponential vs Uniform (should show strong deviation)
    sample_q = np.sort(exponential_data)
    theoretical_q = np.linspace(np.min(sample_q), np.max(sample_q), len(sample_q))
    axes[2].scatter(theoretical_q, sample_q, alpha=0.6, s=10, color='green')
    axes[2].plot([np.min(sample_q), np.max(sample_q)], 
                [np.min(sample_q), np.max(sample_q)], 'r-', linewidth=2)
    axes[2].set_title('Exponential Data vs Uniform Distribution')
    axes[2].set_xlabel('Theoretical Quantiles')
    axes[2].set_ylabel('Sample Quantiles')
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to demonstrate Q-Q plot for uniform distribution testing
    """
    print("Slide 2c: Q-Q Plot - Uniform Distribution Test")
    print("Lecturer: Dr. Yoram Segal")
    print("=" * 55)
    
    # Create Q-Q plot
    correlation, theoretical_q, sample_q = create_qq_plot()
    
    # Analyze results
    analyze_qq_plot_results(correlation, theoretical_q, sample_q)
    
    # Explain concepts
    explain_qq_plot_concepts()
    
    # Show comparisons
    demonstrate_different_distributions()
    
    print("\nSlide 2c demonstration completed")
    print("This slide shows how to use Q-Q plots to test if data")
    print("follows a uniform distribution and interpret the results.")

if __name__ == "__main__":
    main()

