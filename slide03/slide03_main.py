#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Slide 3: Normal Distribution
Based on: Jon Krohn's Machine Learning Foundations series
Lecturer: Dr. Yoram Segal
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import warnings
from pathlib import Path
import webbrowser
import os

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
        slide_path = Path(__file__).parent / "slide3.html"
        if slide_path.exists():
            webbrowser.open(f"file://{slide_path.absolute()}")
            print(f"Slide opened in browser: {slide_path}")
        else:
            print(f"HTML slide not found: {slide_path}")
    except Exception as e:
        print(f"Error opening slide: {e}")

def generate_normal_samples(mean=0, std=1, size=1000):
    """Generate samples from normal distribution"""
    samples = np.random.normal(mean, std, size)
    return samples

def plot_normal_distribution(mean=0, std=1, samples=None):
    """Plot normal distribution with samples"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot 1: Theoretical vs Empirical
    if samples is not None:
        ax1.hist(samples, bins=30, density=True, alpha=0.7, color='skyblue', 
                label=f'Empirical (n={len(samples)})')
    
    # Theoretical curve
    x = np.linspace(mean - 4*std, mean + 4*std, 100)
    y = (1/(std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std) ** 2)
    ax1.plot(x, y, 'r-', linewidth=2, label=f'Theoretical N({mean}, {std}²)')
    
    ax1.set_xlabel('Value')
    ax1.set_ylabel('Density')
    ax1.set_title('Normal Distribution: Theoretical vs Empirical')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Different normal distributions
    x_range = np.linspace(-6, 6, 100)
    
    # Standard normal
    y1 = (1/np.sqrt(2 * np.pi)) * np.exp(-0.5 * x_range**2)
    ax2.plot(x_range, y1, 'b-', linewidth=2, label='N(0, 1) - Standard')
    
    # Different means
    y2 = (1/np.sqrt(2 * np.pi)) * np.exp(-0.5 * (x_range - 2)**2)
    ax2.plot(x_range, y2, 'g-', linewidth=2, label='N(2, 1)')
    
    # Different standard deviations
    y3 = (1/(0.5 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * (x_range / 0.5)**2)
    ax2.plot(x_range, y3, 'r-', linewidth=2, label='N(0, 0.5²)')
    
    ax2.set_xlabel('Value')
    ax2.set_ylabel('Density')
    ax2.set_title('Normal Distributions with Different Parameters')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Save plot
    save_path = Path(__file__).parent / "normal_distribution.png"
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Plot saved to: {save_path}")
    
    # Show plot if not in test mode
    if matplotlib.get_backend() != 'Agg':
        plt.show()
    
    plt.close()
    return save_path

def calculate_normal_properties(samples):
    """Calculate properties of normal distribution"""
    mean = np.mean(samples)
    std = np.std(samples, ddof=1)  # Sample standard deviation
    variance = np.var(samples, ddof=1)
    
    # Calculate percentiles
    percentiles = [5, 25, 50, 75, 95]
    perc_values = np.percentile(samples, percentiles)
    
    return {
        'mean': mean,
        'std': std,
        'variance': variance,
        'percentiles': dict(zip(percentiles, perc_values))
    }

def demonstrate_central_limit_theorem():
    """Demonstrate Central Limit Theorem"""
    print("\n=== Central Limit Theorem Demonstration ===")
    
    # Sample from uniform distribution (not normal)
    sample_sizes = [1, 5, 10, 30]
    n_samples = 1000
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()
    
    for i, n in enumerate(sample_sizes):
        # Generate sample means
        sample_means = []
        for _ in range(n_samples):
            # Sample from uniform distribution [0, 1]
            uniform_samples = np.random.uniform(0, 1, n)
            sample_means.append(np.mean(uniform_samples))
        
        # Plot histogram of sample means
        axes[i].hist(sample_means, bins=30, density=True, alpha=0.7, color='lightcoral')
        
        # Theoretical normal curve (CLT prediction)
        theoretical_mean = 0.5  # Mean of uniform [0,1]
        theoretical_std = np.sqrt(1/12) / np.sqrt(n)  # Std of sample mean
        
        x = np.linspace(min(sample_means), max(sample_means), 100)
        y = (1/(theoretical_std * np.sqrt(2 * np.pi))) * \
            np.exp(-0.5 * ((x - theoretical_mean) / theoretical_std) ** 2)
        axes[i].plot(x, y, 'b-', linewidth=2, label='Theoretical Normal')
        
        axes[i].set_title(f'Sample Size n = {n}')
        axes[i].set_xlabel('Sample Mean')
        axes[i].set_ylabel('Density')
        axes[i].legend()
        axes[i].grid(True, alpha=0.3)
    
    plt.suptitle('Central Limit Theorem: Distribution of Sample Means', fontsize=14)
    plt.tight_layout()
    
    # Save plot
    save_path = Path(__file__).parent / "central_limit_theorem.png"
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"CLT demonstration saved to: {save_path}")
    
    # Show plot if not in test mode
    if matplotlib.get_backend() != 'Agg':
        plt.show()
    
    plt.close()
    return save_path

def main():
    """Main demonstration function"""
    print("Slide 3: Normal Distribution")
    print("Lecturer: Dr. Yoram Segal")
    print("=" * 50)
    
    # Generate normal samples
    print("\n=== Generating 1000 samples from Normal Distribution N(0, 1) ===")
    samples = generate_normal_samples(mean=0, std=1, size=1000)
    
    # Calculate properties
    props = calculate_normal_properties(samples)
    
    print(f"Theoretical mean: 0.000")
    print(f"Empirical mean: {props['mean']:.3f}")
    print(f"Theoretical std: 1.000")
    print(f"Empirical std: {props['std']:.3f}")
    print(f"Empirical variance: {props['variance']:.3f}")
    
    print("\nPercentiles:")
    for perc, value in props['percentiles'].items():
        print(f"  {perc}th percentile: {value:.3f}")
    
    # Plot normal distribution
    plot_normal_distribution(mean=0, std=1, samples=samples)
    
    # Demonstrate Central Limit Theorem
    demonstrate_central_limit_theorem()
    
    # 68-95-99.7 rule
    print("\n=== 68-95-99.7 Rule (Empirical Rule) ===")
    within_1_std = np.sum(np.abs(samples) <= 1) / len(samples)
    within_2_std = np.sum(np.abs(samples) <= 2) / len(samples)
    within_3_std = np.sum(np.abs(samples) <= 3) / len(samples)
    
    print(f"Within 1 std dev: {within_1_std:.3f} (theoretical: 0.683)")
    print(f"Within 2 std dev: {within_2_std:.3f} (theoretical: 0.954)")
    print(f"Within 3 std dev: {within_3_std:.3f} (theoretical: 0.997)")
    
    print("\nSlide 3 demonstration completed")

if __name__ == "__main__":
    main()

