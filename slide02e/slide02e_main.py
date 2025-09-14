#!/usr/bin/env python3
"""
Slide 2e: Cumulative Distribution Function (CDF)
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

def create_cdf_plot():
    """
    Create CDF plot for uniform distribution
    Shows both theoretical and empirical CDF
    """
    print("=== Cumulative Distribution Function (CDF) ===")
    
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Generate uniform data
    print("Generating 1000 uniform random samples between 0 and 10...")
    uniform_data = np.random.uniform(0, 10, 1000)
    
    # Create theoretical CDF
    x_theoretical = np.linspace(0, 10, 100)
    cdf_theoretical = x_theoretical / 10  # F(x) = x/10 for uniform [0,10]
    
    # Create empirical CDF
    x_empirical = np.sort(uniform_data)
    y_empirical = np.arange(1, len(x_empirical) + 1) / len(x_empirical)
    
    # Create the plot
    plt.figure(figsize=(12, 8))
    
    # Plot theoretical CDF
    plt.plot(x_theoretical, cdf_theoretical, 'r-', linewidth=3, 
             label='Theoretical CDF: F(x) = x/10')
    
    # Plot empirical CDF
    plt.plot(x_empirical, y_empirical, 'b-', alpha=0.7, linewidth=2,
             label='Empirical CDF (from sample)')
    
    # Add key points
    key_points_x = [0, 2.5, 5.0, 7.5, 10.0]
    key_points_y = [x/10 for x in key_points_x]
    
    plt.scatter(key_points_x, key_points_y, color='red', s=100, zorder=5)
    
    # Add annotations for key points
    for x, y in zip(key_points_x, key_points_y):
        plt.annotate(f'F({x}) = {y:.1f}', 
                    xy=(x, y), xytext=(x+0.5, y+0.1),
                    arrowprops=dict(arrowstyle='->', color='red'),
                    fontsize=10, color='red')
    
    plt.xlabel('x')
    plt.ylabel('F(x) = P(X ≤ x)')
    plt.title('Cumulative Distribution Function (CDF)\nUniform Distribution [0,10]')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xlim(-0.5, 10.5)
    plt.ylim(-0.05, 1.05)
    
    plt.tight_layout()
    plt.show()
    
    return x_theoretical, cdf_theoretical, x_empirical, y_empirical

def analyze_cdf_properties():
    """
    Analyze and explain CDF properties
    """
    print("\n=== CDF Properties Analysis ===")
    
    # Theoretical values
    print("Theoretical CDF values for uniform [0,10]:")
    test_points = [0, 1, 2.5, 5, 7.5, 9, 10]
    for x in test_points:
        if 0 <= x <= 10:
            cdf_value = x / 10
            print(f"F({x:3.1f}) = P(X ≤ {x:3.1f}) = {cdf_value:.3f}")
    
    # Generate sample data for empirical analysis
    np.random.seed(42)
    uniform_data = np.random.uniform(0, 10, 1000)
    
    print(f"\nEmpirical CDF values from sample (n=1000):")
    for x in test_points:
        empirical_cdf = np.mean(uniform_data <= x)
        theoretical_cdf = x / 10 if 0 <= x <= 10 else (0 if x < 0 else 1)
        difference = abs(empirical_cdf - theoretical_cdf)
        print(f"F({x:3.1f}) ≈ {empirical_cdf:.3f} (theoretical: {theoretical_cdf:.3f}, diff: {difference:.3f})")

def explain_cdf_concepts():
    """
    Explain CDF concepts and interpretation
    """
    print("\n=== CDF Concepts Explained ===")
    print("1. DEFINITION:")
    print("   CDF(x) = F(x) = P(X ≤ x)")
    print("   The probability that random variable X is less than or equal to x")
    
    print("\n2. PROPERTIES:")
    print("   - Always non-decreasing: F(x₁) ≤ F(x₂) if x₁ ≤ x₂")
    print("   - Range: 0 ≤ F(x) ≤ 1")
    print("   - F(-∞) = 0, F(+∞) = 1")
    print("   - Right-continuous")
    
    print("\n3. FOR UNIFORM DISTRIBUTION [a,b]:")
    print("   F(x) = 0           if x < a")
    print("   F(x) = (x-a)/(b-a) if a ≤ x ≤ b")
    print("   F(x) = 1           if x > b")
    
    print("\n4. FOR UNIFORM [0,10]:")
    print("   F(x) = 0     if x < 0")
    print("   F(x) = x/10  if 0 ≤ x ≤ 10")
    print("   F(x) = 1     if x > 10")
    
    print("\n5. INTERPRETATION:")
    print("   - F(5) = 0.5 means 50% of values are ≤ 5")
    print("   - F(7.5) = 0.75 means 75% of values are ≤ 7.5")
    print("   - Linear shape indicates uniform distribution")

def demonstrate_cdf_calculations():
    """
    Demonstrate practical CDF calculations
    """
    print("\n=== CDF Calculations Examples ===")
    
    print("Example calculations for uniform [0,10]:")
    
    # Probability calculations using CDF
    examples = [
        ("P(X ≤ 3)", "F(3) = 3/10 = 0.3"),
        ("P(X ≤ 7)", "F(7) = 7/10 = 0.7"),
        ("P(X > 6)", "1 - F(6) = 1 - 6/10 = 0.4"),
        ("P(2 < X ≤ 8)", "F(8) - F(2) = 8/10 - 2/10 = 0.6"),
        ("P(X = 5)", "F(5) - F(5⁻) = 0 (continuous distribution)")
    ]
    
    for description, calculation in examples:
        print(f"{description:15} = {calculation}")
    
    # Verify with sample data
    np.random.seed(42)
    uniform_data = np.random.uniform(0, 10, 10000)
    
    print(f"\nVerification with sample data (n=10,000):")
    print(f"P(X ≤ 3) ≈ {np.mean(uniform_data <= 3):.3f} (theoretical: 0.300)")
    print(f"P(X ≤ 7) ≈ {np.mean(uniform_data <= 7):.3f} (theoretical: 0.700)")
    print(f"P(X > 6) ≈ {np.mean(uniform_data > 6):.3f} (theoretical: 0.400)")
    print(f"P(2 < X ≤ 8) ≈ {np.mean((uniform_data > 2) & (uniform_data <= 8)):.3f} (theoretical: 0.600)")

def compare_distributions_cdf():
    """
    Compare CDF of different distributions
    """
    print("\n=== Comparing CDFs of Different Distributions ===")
    
    np.random.seed(42)
    x = np.linspace(0, 10, 100)
    
    # Uniform CDF
    uniform_cdf = np.where(x < 0, 0, np.where(x > 10, 1, x/10))
    
    # Normal CDF (approximation for comparison)
    normal_cdf = stats.norm.cdf(x, loc=5, scale=2)
    
    # Exponential CDF
    exponential_cdf = 1 - np.exp(-x/3)
    
    plt.figure(figsize=(12, 8))
    
    plt.plot(x, uniform_cdf, 'b-', linewidth=3, label='Uniform [0,10]')
    plt.plot(x, normal_cdf, 'r-', linewidth=3, label='Normal (μ=5, σ=2)')
    plt.plot(x, exponential_cdf, 'g-', linewidth=3, label='Exponential (λ=1/3)')
    
    plt.xlabel('x')
    plt.ylabel('F(x)')
    plt.title('Comparison of CDFs for Different Distributions')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xlim(0, 10)
    plt.ylim(0, 1)
    
    plt.tight_layout()
    plt.show()
    
    print("Observations:")
    print("- Uniform: Linear (straight line)")
    print("- Normal: S-shaped curve (sigmoid)")
    print("- Exponential: Rapid initial rise, then levels off")

def python_code_explanation():
    """
    Explain the Python code for CDF creation
    """
    print("\n=== Python Code Explanation ===")
    print("1. THEORETICAL CDF:")
    print("   x_theoretical = np.linspace(0, 10, 100)")
    print("   cdf_theoretical = x_theoretical / 10")
    print("   Creates smooth theoretical CDF curve")
    
    print("\n2. EMPIRICAL CDF:")
    print("   x_empirical = np.sort(uniform_data)")
    print("   y_empirical = np.arange(1, n+1) / n")
    print("   Creates step function from sample data")
    
    print("\n3. PLOTTING:")
    print("   plt.plot() for both theoretical and empirical")
    print("   Different colors and styles for comparison")
    
    print("\n4. VERIFICATION:")
    print("   np.mean(data <= x) calculates empirical CDF at point x")
    print("   Compare with theoretical value x/10")

def main():
    """
    Main function to demonstrate CDF concepts and calculations
    """
    print("Slide 2e: Cumulative Distribution Function (CDF)")
    print("Lecturer: Dr. Yoram Segal")
    print("=" * 55)
    
    # Create CDF plot
    x_theo, cdf_theo, x_emp, y_emp = create_cdf_plot()
    
    # Analyze properties
    analyze_cdf_properties()
    
    # Explain concepts
    explain_cdf_concepts()
    
    # Demonstrate calculations
    demonstrate_cdf_calculations()
    
    # Compare distributions
    compare_distributions_cdf()
    
    # Explain code
    python_code_explanation()
    
    print("\nSlide 2e demonstration completed")
    print("This slide covers CDF concepts, calculations, and interpretation")
    print("for uniform distribution with practical examples.")

if __name__ == "__main__":
    main()

