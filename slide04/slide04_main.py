#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Slide 4: Binomial Distribution
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
        slide_path = Path(__file__).parent / "slide4.html"
        if slide_path.exists():
            webbrowser.open(f"file://{slide_path.absolute()}")
            print(f"Slide opened in browser: {slide_path}")
        else:
            print(f"HTML slide not found: {slide_path}")
    except Exception as e:
        print(f"Error opening slide: {e}")

def simulate_coin_flips(n_trials, p_success, n_experiments=1000):
    """Simulate binomial experiments"""
    results = []
    for _ in range(n_experiments):
        # Simulate n_trials coin flips
        flips = np.random.random(n_trials) < p_success
        successes = np.sum(flips)
        results.append(successes)
    return np.array(results)

def plot_binomial_distribution(n, p, title_suffix=""):
    """Plot binomial distribution"""
    # Theoretical probabilities
    x = np.arange(0, n + 1)
    pmf = stats.binom.pmf(x, n, p)
    
    # Simulation
    simulated = simulate_coin_flips(n, p, 10000)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Plot 1: Theoretical PMF
    ax1.bar(x, pmf, alpha=0.7, color='skyblue', label='Theoretical PMF')
    ax1.set_xlabel('Number of Successes')
    ax1.set_ylabel('Probability')
    ax1.set_title(f'Binomial Distribution B({n}, {p}){title_suffix}')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # Add mean and std lines
    mean = n * p
    std = np.sqrt(n * p * (1 - p))
    ax1.axvline(mean, color='red', linestyle='--', linewidth=2, label=f'Mean = {mean:.1f}')
    ax1.axvline(mean - std, color='orange', linestyle=':', alpha=0.7, label=f'±1 Std = {std:.1f}')
    ax1.axvline(mean + std, color='orange', linestyle=':', alpha=0.7)
    ax1.legend()
    
    # Plot 2: Simulation vs Theoretical
    bins = np.arange(-0.5, n + 1.5, 1)
    ax2.hist(simulated, bins=bins, density=True, alpha=0.7, color='lightcoral', 
             label='Simulation (10,000 experiments)')
    ax2.bar(x, pmf, alpha=0.7, color='skyblue', width=0.4, label='Theoretical PMF')
    ax2.set_xlabel('Number of Successes')
    ax2.set_ylabel('Probability Density')
    ax2.set_title(f'Simulation vs Theory{title_suffix}')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    
    # Save plot
    save_name = f"binomial_n{n}_p{p:.1f}{title_suffix.lower().replace(' ', '_').replace('(', '').replace(')', '')}.png"
    save_path = Path(__file__).parent / save_name
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Plot saved to: {save_path}")
    
    # Show plot if not in test mode
    if matplotlib.get_backend() != 'Agg':
        plt.show()
    
    plt.close()
    return save_path

def calculate_binomial_properties(n, p):
    """Calculate binomial distribution properties"""
    mean = n * p
    variance = n * p * (1 - p)
    std = np.sqrt(variance)
    
    # Calculate some probabilities
    prob_exact_mean = stats.binom.pmf(int(mean), n, p)
    prob_at_least_half = 1 - stats.binom.cdf(n//2 - 1, n, p)
    prob_all_success = stats.binom.pmf(n, n, p)
    prob_no_success = stats.binom.pmf(0, n, p)
    
    return {
        'mean': mean,
        'variance': variance,
        'std': std,
        'prob_exact_mean': prob_exact_mean,
        'prob_at_least_half': prob_at_least_half,
        'prob_all_success': prob_all_success,
        'prob_no_success': prob_no_success
    }

def compare_different_p_values():
    """Compare binomial distributions with different p values"""
    n = 20
    p_values = [0.1, 0.3, 0.5, 0.7, 0.9]
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()
    
    for i, p in enumerate(p_values):
        x = np.arange(0, n + 1)
        pmf = stats.binom.pmf(x, n, p)
        
        axes[i].bar(x, pmf, alpha=0.7, color=plt.cm.viridis(i/len(p_values)))
        axes[i].set_title(f'B({n}, {p})')
        axes[i].set_xlabel('Number of Successes')
        axes[i].set_ylabel('Probability')
        axes[i].grid(True, alpha=0.3)
        
        # Add mean line
        mean = n * p
        axes[i].axvline(mean, color='red', linestyle='--', linewidth=2, 
                       label=f'Mean = {mean:.1f}')
        axes[i].legend()
    
    # Remove empty subplot
    axes[-1].remove()
    
    plt.suptitle('Binomial Distributions with Different Success Probabilities', fontsize=14)
    plt.tight_layout()
    
    # Save plot
    save_path = Path(__file__).parent / "binomial_comparison.png"
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Comparison plot saved to: {save_path}")
    
    # Show plot if not in test mode
    if matplotlib.get_backend() != 'Agg':
        plt.show()
    
    plt.close()
    return save_path

def main():
    """Main demonstration function"""
    print("Slide 4: Binomial Distribution")
    print("Lecturer: Dr. Yoram Segal")
    print("=" * 50)
    
    # Fair coin example
    print("\n=== Fair Coin Example: 10 flips ===")
    n1, p1 = 10, 0.5
    props1 = calculate_binomial_properties(n1, p1)
    
    print(f"Number of trials (n): {n1}")
    print(f"Success probability (p): {p1}")
    print(f"Expected successes: {props1['mean']:.1f}")
    print(f"Standard deviation: {props1['std']:.3f}")
    print(f"Probability of exactly {int(props1['mean'])} successes: {props1['prob_exact_mean']:.3f}")
    print(f"Probability of at least {n1//2} successes: {props1['prob_at_least_half']:.3f}")
    print(f"Probability of all successes: {props1['prob_all_success']:.6f}")
    print(f"Probability of no successes: {props1['prob_no_success']:.6f}")
    
    plot_binomial_distribution(n1, p1, " (Fair Coin)")
    
    # Weighted coin example
    print("\n=== Weighted Coin Example: 20 flips, p=0.8 ===")
    n2, p2 = 20, 0.8
    props2 = calculate_binomial_properties(n2, p2)
    
    print(f"Number of trials (n): {n2}")
    print(f"Success probability (p): {p2}")
    print(f"Expected successes: {props2['mean']:.1f}")
    print(f"Standard deviation: {props2['std']:.3f}")
    print(f"Probability of exactly {int(props2['mean'])} successes: {props2['prob_exact_mean']:.3f}")
    print(f"Probability of at least {n2//2} successes: {props2['prob_at_least_half']:.3f}")
    
    plot_binomial_distribution(n2, p2, " (Weighted Coin)")
    
    # Compare different p values
    print("\n=== Comparing Different Success Probabilities ===")
    compare_different_p_values()
    
    # Real-world applications
    print("\n=== Real-World Applications ===")
    print("1. Quality Control: Testing 100 products, 5% defect rate")
    n3, p3 = 100, 0.05
    props3 = calculate_binomial_properties(n3, p3)
    print(f"   Expected defects: {props3['mean']:.1f}")
    print(f"   Probability of ≤3 defects: {stats.binom.cdf(3, n3, p3):.3f}")
    
    print("\n2. Medical Testing: 50 patients, 80% cure rate")
    n4, p4 = 50, 0.8
    props4 = calculate_binomial_properties(n4, p4)
    print(f"   Expected cures: {props4['mean']:.1f}")
    print(f"   Probability of ≥40 cures: {1 - stats.binom.cdf(39, n4, p4):.3f}")
    
    print("\nSlide 4 demonstration completed")

if __name__ == "__main__":
    main()

