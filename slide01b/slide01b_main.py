#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Slide 1b: Frequencies from Simulation
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
        slide_path = Path(__file__).parent / "slide1b.html"
        if slide_path.exists():
            webbrowser.open(f"file://{slide_path.absolute()}")
            print(f"Slide opened in browser: {slide_path}")
        else:
            print(f"HTML slide not found: {slide_path}")
    except Exception as e:
        print(f"Error opening slide: {e}")

def simulate_dice_frequencies(n_rolls=1000):
    """Simulate dice rolls and show frequencies"""
    print(f"\n=== Simulation of {n_rolls} Dice Rolls ===")
    
    # Run simulation with fixed seed for reproducible results
    np.random.seed(42)
    rolls = np.random.randint(1, 7, n_rolls)
    
    # Calculate frequencies
    unique, counts = np.unique(rolls, return_counts=True)
    frequencies = counts / n_rolls
    
    print("Simulation Results:")
    print("Outcome | Count | Frequency | Theoretical | Difference")
    print("-" * 55)
    for outcome, count, freq in zip(unique, counts, frequencies):
        theoretical = 1/6
        diff = freq - theoretical
        print(f"   {outcome}    | {count:4d}  |  {freq:.3f}   |   {theoretical:.3f}    | {diff:+.3f}")
    
    # Calculate chi-square goodness of fit
    expected_counts = [n_rolls/6] * 6
    chi_square = sum((obs - exp)**2 / exp for obs, exp in zip(counts, expected_counts))
    print(f"\nChi-square statistic: {chi_square:.3f}")
    print(f"Expected for fair dice: ~5.99 (95% confidence)")
    
    return unique, frequencies, counts

def create_frequency_comparison_chart(outcomes, frequencies, counts, n_rolls=1000):
    """Create frequency comparison chart"""
    
    # Create the visualization
    plt.figure(figsize=(12, 6))
    
    # Theoretical probabilities
    theoretical = [1/6] * 6
    
    # Create bar chart comparing simulation vs theoretical
    x = np.arange(len(outcomes))
    width = 0.35
    
    bars1 = plt.bar(x - width/2, frequencies, width, label='Simulation', 
                   color='#059669', alpha=0.8, edgecolor='black')
    bars2 = plt.bar(x + width/2, theoretical, width, label='Theoretical', 
                   color='#DC2626', alpha=0.8, edgecolor='black')
    
    # Add value labels on bars
    for bar, freq in zip(bars1, frequencies):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.005,
                f'{freq:.3f}', ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    for bar, theo in zip(bars2, theoretical):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.005,
                f'{theo:.3f}', ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # Style the plot
    plt.title(f'Slide 1b: Frequencies from Simulation ({n_rolls} rolls)', 
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Dice Outcome', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.xticks(x, outcomes)
    plt.legend(fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    
    # Add horizontal line at theoretical probability
    plt.axhline(y=1/6, color='red', linestyle='--', alpha=0.5, 
                label='Theoretical Line (1/6)')
    
    # Add text box with statistics
    mean_freq = np.mean(frequencies)
    std_freq = np.std(frequencies)
    textstr = f'Statistics:\nMean frequency: {mean_freq:.3f}\nStd deviation: {std_freq:.3f}\nSample size: {n_rolls}'
    props = dict(boxstyle='round', facecolor='lightblue', alpha=0.8)
    plt.text(0.02, 0.98, textstr, transform=plt.gca().transAxes, fontsize=10,
             verticalalignment='top', bbox=props)
    
    plt.tight_layout()
    
    # Save the plot
    output_path = Path(__file__).parent / "dice_frequencies_simulation.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Frequency chart saved to: {output_path}")
    
    # Show plot if not in test mode
    if matplotlib.get_backend() != 'Agg':
        plt.show()
    
    plt.close()  # Important: close the figure to prevent empty windows
    
    return output_path

def analyze_convergence(max_rolls=10000):
    """Analyze how frequencies converge to theoretical probability"""
    print(f"\n=== Law of Large Numbers Demonstration ===")
    
    np.random.seed(42)
    
    # Generate all rolls at once
    all_rolls = np.random.randint(1, 7, max_rolls)
    
    # Calculate running frequencies for outcome 1
    sample_sizes = [10, 50, 100, 500, 1000, 5000, 10000]
    frequencies_of_1 = []
    
    print("Convergence to theoretical probability (1/6 = 0.167):")
    print("Sample Size | Frequency of '1' | Difference from 1/6")
    print("-" * 50)
    
    for n in sample_sizes:
        rolls_subset = all_rolls[:n]
        freq_1 = np.sum(rolls_subset == 1) / n
        frequencies_of_1.append(freq_1)
        diff = freq_1 - (1/6)
        print(f"   {n:5d}    |     {freq_1:.3f}      |    {diff:+.3f}")
    
    return sample_sizes, frequencies_of_1

def explain_law_of_large_numbers():
    """Explain the Law of Large Numbers"""
    print("\n=== Law of Large Numbers ===")
    
    print("DEFINITION:")
    print("As the number of trials increases, the experimental probability")
    print("approaches the theoretical probability.")
    
    print("\nKEY POINTS:")
    print("• Small samples can deviate significantly from theory")
    print("• Large samples tend to be closer to theoretical values")
    print("• This is the foundation of statistical inference")
    print("• It explains why casinos always win in the long run")
    
    print("\nMATHEMATICAL EXPRESSION:")
    print("lim(n→∞) P(|X̄ₙ - μ| > ε) = 0")
    print("Where:")
    print("  X̄ₙ = sample mean after n trials")
    print("  μ = theoretical mean")
    print("  ε = any small positive number")

def main():
    """Main demonstration function"""
    print("Slide 1b: Frequencies from Simulation")
    print("Lecturer: Dr. Yoram Segal")
    print("=" * 50)
    
    # Explain Law of Large Numbers
    explain_law_of_large_numbers()
    
    # Run simulation
    outcomes, frequencies, counts = simulate_dice_frequencies(1000)
    
    # Create visualization
    create_frequency_comparison_chart(outcomes, frequencies, counts, 1000)
    
    # Analyze convergence
    sample_sizes, freq_of_1 = analyze_convergence()
    
    print("\nSlide 1b demonstration completed")
    print("This slide demonstrates how simulation frequencies approach theoretical probabilities.")

if __name__ == "__main__":
    main()

