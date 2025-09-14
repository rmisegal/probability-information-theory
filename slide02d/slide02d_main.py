#!/usr/bin/env python3
"""
Slide 2d: Box Plot - How to Read Box Plots
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

def create_box_plot():
    """
    Create box plot for uniform distribution and explain components
    """
    print("=== Box Plot: How to Read Box Plots ===")
    
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Generate uniform data
    print("Generating 1000 uniform random samples between 0 and 10...")
    uniform_data = np.random.uniform(0, 10, 1000)
    
    # Calculate quartiles and statistics
    q1 = np.percentile(uniform_data, 25)
    q2 = np.percentile(uniform_data, 50)  # median
    q3 = np.percentile(uniform_data, 75)
    iqr = q3 - q1
    
    # Calculate whiskers (1.5 * IQR rule)
    lower_whisker = q1 - 1.5 * iqr
    upper_whisker = q3 + 1.5 * iqr
    
    # Find actual whisker values (within data range)
    actual_lower = np.min(uniform_data[uniform_data >= lower_whisker])
    actual_upper = np.max(uniform_data[uniform_data <= upper_whisker])
    
    # Find outliers
    outliers = uniform_data[(uniform_data < lower_whisker) | (uniform_data > upper_whisker)]
    
    print(f"\nBox Plot Statistics:")
    print(f"Q1 (25th percentile): {q1:.3f}")
    print(f"Q2 (50th percentile - Median): {q2:.3f}")
    print(f"Q3 (75th percentile): {q3:.3f}")
    print(f"IQR (Interquartile Range): {iqr:.3f}")
    print(f"Lower whisker: {actual_lower:.3f}")
    print(f"Upper whisker: {actual_upper:.3f}")
    print(f"Number of outliers: {len(outliers)}")
    
    # Create box plot
    plt.figure(figsize=(10, 8))
    
    # Create the box plot
    box_plot = plt.boxplot(uniform_data, patch_artist=True, 
                          labels=['Uniform Distribution'])
    
    # Customize the box plot
    box_plot['boxes'][0].set_facecolor('lightblue')
    box_plot['boxes'][0].set_alpha(0.7)
    box_plot['medians'][0].set_color('red')
    box_plot['medians'][0].set_linewidth(3)
    
    # Add annotations
    plt.annotate(f'Q3: {q3:.2f}', xy=(1.1, q3), xytext=(1.3, q3),
                arrowprops=dict(arrowstyle='->', color='blue'),
                fontsize=10, color='blue')
    
    plt.annotate(f'Median: {q2:.2f}', xy=(1.1, q2), xytext=(1.3, q2),
                arrowprops=dict(arrowstyle='->', color='red'),
                fontsize=10, color='red')
    
    plt.annotate(f'Q1: {q1:.2f}', xy=(1.1, q1), xytext=(1.3, q1),
                arrowprops=dict(arrowstyle='->', color='blue'),
                fontsize=10, color='blue')
    
    plt.ylabel('Values')
    plt.title('Box Plot: Uniform Distribution\nHow to Read Box Plot Components')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return q1, q2, q3, iqr, outliers

def explain_box_plot_components():
    """
    Explain each component of a box plot
    """
    print("\n=== Box Plot Components Explained ===")
    print("1. THE BOX (Rectangle):")
    print("   - Contains the middle 50% of the data")
    print("   - Bottom edge: Q1 (25th percentile)")
    print("   - Top edge: Q3 (75th percentile)")
    print("   - Height: IQR (Interquartile Range) = Q3 - Q1")
    
    print("\n2. THE MEDIAN LINE:")
    print("   - Red line inside the box")
    print("   - Represents Q2 (50th percentile)")
    print("   - Divides the data into two equal halves")
    print("   - Position indicates skewness of distribution")
    
    print("\n3. THE WHISKERS (Lines extending from box):")
    print("   - Extend to the furthest points within 1.5 × IQR")
    print("   - Lower whisker: Q1 - 1.5 × IQR (or minimum value)")
    print("   - Upper whisker: Q3 + 1.5 × IQR (or maximum value)")
    print("   - Show the range of 'normal' data variation")
    
    print("\n4. OUTLIERS (Individual points):")
    print("   - Data points beyond the whiskers")
    print("   - Values < Q1 - 1.5 × IQR or > Q3 + 1.5 × IQR")
    print("   - Represent unusual or extreme observations")
    
    print("\n5. INTERPRETING UNIFORM DISTRIBUTION:")
    print("   - Box should be roughly centered")
    print("   - Median line should be near the center of the box")
    print("   - Whiskers should be approximately equal length")
    print("   - Few or no outliers expected")

def demonstrate_box_plot_reading():
    """
    Demonstrate how to read and interpret box plots
    """
    print("\n=== How to Read Box Plots ===")
    
    # Create multiple distributions for comparison
    np.random.seed(42)
    uniform_data = np.random.uniform(0, 10, 1000)
    normal_data = np.random.normal(5, 1.5, 1000)
    skewed_data = np.random.exponential(2, 1000)
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 6))
    
    # Uniform distribution
    bp1 = axes[0].boxplot(uniform_data, patch_artist=True)
    bp1['boxes'][0].set_facecolor('lightblue')
    axes[0].set_title('Uniform Distribution\n(Symmetric, centered median)')
    axes[0].set_ylabel('Values')
    axes[0].grid(True, alpha=0.3)
    
    # Normal distribution
    bp2 = axes[1].boxplot(normal_data, patch_artist=True)
    bp2['boxes'][0].set_facecolor('lightgreen')
    axes[1].set_title('Normal Distribution\n(Symmetric, few outliers)')
    axes[1].set_ylabel('Values')
    axes[1].grid(True, alpha=0.3)
    
    # Skewed distribution
    bp3 = axes[2].boxplot(skewed_data, patch_artist=True)
    bp3['boxes'][0].set_facecolor('lightcoral')
    axes[2].set_title('Exponential Distribution\n(Right-skewed, many outliers)')
    axes[2].set_ylabel('Values')
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    print("\nComparison Analysis:")
    print("- Uniform: Symmetric box, median centered, equal whiskers")
    print("- Normal: Symmetric box, median centered, some outliers")
    print("- Exponential: Asymmetric box, median shifted, many outliers")

def python_code_explanation():
    """
    Explain the Python code for creating box plots
    """
    print("\n=== Python Code Explanation ===")
    print("1. DATA GENERATION:")
    print("   np.random.uniform(0, 10, 1000) - Generate uniform random numbers")
    print("   np.random.seed(42) - Set seed for reproducible results")
    
    print("\n2. QUARTILE CALCULATION:")
    print("   np.percentile(data, 25) - Calculate Q1 (25th percentile)")
    print("   np.percentile(data, 50) - Calculate Q2 (median)")
    print("   np.percentile(data, 75) - Calculate Q3 (75th percentile)")
    
    print("\n3. BOX PLOT CREATION:")
    print("   plt.boxplot(data, patch_artist=True) - Create box plot")
    print("   patch_artist=True - Allows coloring the boxes")
    print("   box_plot['boxes'][0].set_facecolor() - Set box color")
    print("   box_plot['medians'][0].set_color() - Set median line color")
    
    print("\n4. CUSTOMIZATION:")
    print("   plt.annotate() - Add text annotations with arrows")
    print("   arrowprops=dict() - Configure arrow appearance")
    print("   plt.grid(True, alpha=0.3) - Add semi-transparent grid")

def main():
    """
    Main function to demonstrate box plot reading and interpretation
    """
    print("Slide 2d: Box Plot - How to Read Box Plots")
    print("Lecturer: Dr. Yoram Segal")
    print("=" * 50)
    
    # Create and analyze box plot
    q1, q2, q3, iqr, outliers = create_box_plot()
    
    # Explain components
    explain_box_plot_components()
    
    # Demonstrate reading
    demonstrate_box_plot_reading()
    
    # Explain Python code
    python_code_explanation()
    
    print("\nSlide 2d demonstration completed")
    print("This slide teaches how to read and interpret box plots")
    print("using uniform distribution as an example.")

if __name__ == "__main__":
    main()

