#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Slide 5: Poisson Distribution
Based on: Jon Krohn's Machine Learning Foundations series
Lecturer: Dr. Yoram Segal
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import warnings
from pathlib import Path
import webbrowser
from scipy import stats

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
        slide_path = Path(__file__).parent / "slide5.html"
        if slide_path.exists():
            webbrowser.open(f"file://{slide_path.absolute()}")
            print(f"Slide opened in browser: {slide_path}")
        else:
            print(f"HTML slide not found: {slide_path}")
    except Exception as e:
        print(f"Error opening slide: {e}")

def plot_poisson_distribution(lam, title_suffix=""):
    """Plot Poisson distribution"""
    # Generate x values
    x_max = int(lam + 4 * np.sqrt(lam)) + 5
    x = np.arange(0, x_max)
    pmf = stats.poisson.pmf(x, lam)
    
    # Simulation
    simulated = np.random.poisson(lam, 10000)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Plot 1: Theoretical PMF
    ax1.bar(x, pmf, alpha=0.7, color='lightgreen', label='Theoretical PMF')
    ax1.set_xlabel('Number of Events')
    ax1.set_ylabel('Probability')
    ax1.set_title(f'Poisson Distribution (λ = {lam}){title_suffix}')
    ax1.grid(True, alpha=0.3)
    
    # Add mean line
    ax1.axvline(lam, color='red', linestyle='--', linewidth=2, label=f'Mean = λ = {lam}')
    ax1.legend()
    
    # Plot 2: Simulation vs Theoretical
    bins = np.arange(-0.5, x_max + 0.5, 1)
    ax2.hist(simulated, bins=bins, density=True, alpha=0.7, color='lightcoral', 
             label='Simulation (10,000 samples)')
    ax2.bar(x, pmf, alpha=0.7, color='lightgreen', width=0.4, label='Theoretical PMF')
    ax2.set_xlabel('Number of Events')
    ax2.set_ylabel('Probability Density')
    ax2.set_title(f'Simulation vs Theory{title_suffix}')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    
    # Save plot
    save_name = f"poisson_lambda{lam}{title_suffix.lower().replace(' ', '_').replace('(', '').replace(')', '')}.png"
    save_path = Path(__file__).parent / save_name
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Plot saved to: {save_path}")
    
    # Show plot if not in test mode
    if matplotlib.get_backend() != 'Agg':
        plt.show()
    
    plt.close()
    return save_path

def main():
    """Main demonstration function"""
    print("Slide 5: Poisson Distribution")
    print("Lecturer: Dr. Yoram Segal")
    print("=" * 50)
    
    # Example 1: Low rate events
    print("\n=== Example 1: Email arrivals (λ = 2 per hour) ===")
    lam1 = 2
    print(f"Average rate (λ): {lam1} events per hour")
    print(f"Mean: {lam1}")
    print(f"Variance: {lam1}")
    print(f"Standard deviation: {np.sqrt(lam1):.3f}")
    
    # Calculate probabilities
    prob_0 = stats.poisson.pmf(0, lam1)
    prob_1 = stats.poisson.pmf(1, lam1)
    prob_more_than_3 = 1 - stats.poisson.cdf(3, lam1)
    
    print(f"P(exactly 0 emails): {prob_0:.3f}")
    print(f"P(exactly 1 email): {prob_1:.3f}")
    print(f"P(more than 3 emails): {prob_more_than_3:.3f}")
    
    plot_poisson_distribution(lam1, " (Low Rate)")
    
    # Example 2: Higher rate events
    print("\n=== Example 2: Website visits (λ = 8 per minute) ===")
    lam2 = 8
    print(f"Average rate (λ): {lam2} events per minute")
    print(f"Mean: {lam2}")
    print(f"Variance: {lam2}")
    print(f"Standard deviation: {np.sqrt(lam2):.3f}")
    
    plot_poisson_distribution(lam2, " (High Rate)")
    
    # Compare different lambda values
    print("\n=== Comparing Different Rates ===")
    lambdas = [1, 3, 5, 10]
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()
    
    for i, lam in enumerate(lambdas):
        x_max = int(lam + 4 * np.sqrt(lam)) + 5
        x = np.arange(0, x_max)
        pmf = stats.poisson.pmf(x, lam)
        
        axes[i].bar(x, pmf, alpha=0.7, color=plt.cm.viridis(i/len(lambdas)))
        axes[i].set_title(f'Poisson(λ = {lam})')
        axes[i].set_xlabel('Number of Events')
        axes[i].set_ylabel('Probability')
        axes[i].grid(True, alpha=0.3)
        axes[i].axvline(lam, color='red', linestyle='--', linewidth=2, 
                       label=f'Mean = {lam}')
        axes[i].legend()
    
    plt.suptitle('Poisson Distributions with Different Rates', fontsize=14)
    plt.tight_layout()
    
    save_path = Path(__file__).parent / "poisson_comparison.png"
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Comparison plot saved to: {save_path}")
    
    if matplotlib.get_backend() != 'Agg':
        plt.show()
    plt.close()
    
    # Real-world applications
    print("\n=== Real-World Applications ===")
    print("1. Call center: 15 calls per hour")
    print(f"   P(≤10 calls in hour): {stats.poisson.cdf(10, 15):.3f}")
    
    print("2. Manufacturing defects: 0.5 defects per product")
    print(f"   P(no defects): {stats.poisson.pmf(0, 0.5):.3f}")
    
    print("3. Website crashes: 2 per month")
    print(f"   P(≥3 crashes): {1 - stats.poisson.cdf(2, 2):.3f}")
    
    print("\nSlide 5 demonstration completed")

if __name__ == "__main__":
    main()

