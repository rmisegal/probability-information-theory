#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Slide 1: Introduction to Probability

Based on: Jon Krohn's Machine Learning Foundations series
Lecturer: Dr. Yoram Segal

Python code for basic probability calculations and dice roll visualization
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import webbrowser
import os
import sys
from pathlib import Path

# Suppress matplotlib warnings including font warnings
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module="matplotlib")
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
warnings.filterwarnings("ignore", message="findfont: Font family.*not found")

# Set font support - use only default available fonts
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['axes.unicode_minus'] = False

def show_slide():
    """Display HTML slide"""
    slide_path = Path(__file__).parent / "slide1.html"
    if slide_path.exists():
        try:
            # Try to open with default browser
            webbrowser.open(f"file://{slide_path.absolute()}")
            print(f"Slide opened in browser: {slide_path}")
        except Exception as e:
            print(f"Could not open slide automatically: {e}")
            print(f"Please open manually: {slide_path.absolute()}")
    else:
        print(f"Slide file not found: {slide_path}")
        print("Available files in directory:")
        for file in Path(__file__).parent.glob("*.html"):
            print(f"  - {file.name}")

def calculate_dice_probabilities():
    """Calculate probabilities for fair dice roll"""
    print("=== Dice Probability Calculations ===")
    
    # Define possible outcomes
    outcomes = ['1', '2', '3', '4', '5', '6']
    
    # Calculate probability for each outcome
    probability = 1 / len(outcomes)
    print(f"Probability for each outcome: {probability:.3f}")
    
    # Probability of getting even number
    even_outcomes = ['2', '4', '6']
    prob_even = len(even_outcomes) / len(outcomes)
    print(f"Probability of even number: {prob_even:.3f}")
    
    # Probability of getting odd number
    odd_outcomes = ['1', '3', '5']
    prob_odd = len(odd_outcomes) / len(outcomes)
    print(f"Probability of odd number: {prob_odd:.3f}")
    
    # Probability of getting number greater than 4
    high_outcomes = ['5', '6']
    prob_high = len(high_outcomes) / len(outcomes)
    print(f"Probability of number > 4: {prob_high:.3f}")
    
    return outcomes, [probability] * len(outcomes)

def create_dice_visualization():
    """Create visualization of dice probabilities"""
    outcomes, probabilities = calculate_dice_probabilities()
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    bars = plt.bar(outcomes, probabilities, color='#12377A', alpha=0.8, 
                   edgecolor='#0f2d5f', linewidth=2)
    
    # Add values on bars
    for bar, prob in zip(bars, probabilities):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.005,
                f'{prob:.3f}', ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    # Style the plot
    plt.title('Fair Dice Roll Probabilities', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Dice Outcome', fontsize=14)
    plt.ylabel('Probability', fontsize=14)
    plt.ylim(0, 0.2)
    plt.grid(axis='y', alpha=0.3)
    
    # Add theoretical line
    plt.axhline(y=1/6, color='red', linestyle='--', alpha=0.7, label='Theoretical Probability')
    plt.legend()
    
    plt.tight_layout()
    
    # Save the plot
    output_path = Path(__file__).parent / "dice_probability_chart.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Chart saved to: {output_path}")
    
    plt.show()
    
    return plt.gcf()

def simulate_dice_rolls(n_rolls=1000):
    """Simulate dice rolls"""
    print(f"\n=== Simulation of {n_rolls} Dice Rolls ===")
    
    # Run simulation
    np.random.seed(42)  # For consistent results
    rolls = np.random.randint(1, 7, n_rolls)
    
    # Calculate frequencies
    unique, counts = np.unique(rolls, return_counts=True)
    frequencies = counts / n_rolls
    
    print("Simulation Results:")
    for outcome, freq in zip(unique, frequencies):
        print(f"  {outcome}: {freq:.3f} (theoretical: 0.167)")
    
    # Create visual comparison
    plt.figure(figsize=(12, 5))
    
    # Plot 1: Frequencies from simulation
    plt.subplot(1, 2, 1)
    plt.bar(unique, frequencies, color='#059669', alpha=0.8, label='Simulation')
    plt.axhline(y=1/6, color='red', linestyle='--', alpha=0.7, label='Theoretical')
    plt.title('Frequencies from Simulation')
    plt.xlabel('Dice Outcome')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    
    # Plot 2: Histogram of all rolls
    plt.subplot(1, 2, 2)
    plt.hist(rolls, bins=np.arange(0.5, 7.5, 1), color='#DC2626', alpha=0.7, edgecolor='black')
    plt.title(f'Histogram of {n_rolls} Rolls')
    plt.xlabel('Dice Outcome')
    plt.ylabel('Number of Rolls')
    plt.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    
    # Save the plot
    output_path = Path(__file__).parent / "dice_simulation.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Simulation plot saved to: {output_path}")
    
    plt.show()
    
    return rolls, frequencies

def probability_rules_examples():
    """Examples of probability rules"""
    print("\n=== Basic Probability Rules ===")
    
    # Addition rule (mutually exclusive events)
    prob_even = 3/6  # Even
    prob_odd = 3/6   # Odd
    prob_all = prob_even + prob_odd
    print(f"P(even) + P(odd) = {prob_even:.3f} + {prob_odd:.3f} = {prob_all:.3f}")
    
    # Complement probability
    prob_not_six = 1 - (1/6)
    print(f"P(not 6) = 1 - P(6) = 1 - {1/6:.3f} = {prob_not_six:.3f}")
    
    # Conditional probability (given the outcome is even)
    prob_six_given_even = 1/3  # Out of 3 even numbers, one is 6
    print(f"P(6|even) = {prob_six_given_even:.3f}")

def interactive_menu():
    """Interactive menu"""
    while True:
        print("\n" + "="*50)
        print("Slide 1: Introduction to Probability")
        print("="*50)
        print("1. Show HTML slide")
        print("2. Calculate basic probabilities")
        print("3. Create visualization")
        print("4. Run simulation")
        print("5. Probability rules examples")
        print("6. Run all")
        print("0. Exit")
        
        choice = input("\nChoose option (0-6): ").strip()
        
        if choice == '0':
            print("Exiting...")
            break
        elif choice == '1':
            show_slide()
        elif choice == '2':
            calculate_dice_probabilities()
        elif choice == '3':
            create_dice_visualization()
        elif choice == '4':
            simulate_dice_rolls(1000)
        elif choice == '5':
            probability_rules_examples()
        elif choice == '6':
            main()
        else:
            print("Invalid choice. Please try again.")

def main():
    """Main function"""
    print("Slide 1: Introduction to Probability")
    print("Based on: Jon Krohn's Machine Learning Foundations series")
    print("Lecturer: Dr. Yoram Segal")
    print("=" * 60)
    
    # Calculate basic probabilities
    calculate_dice_probabilities()
    
    # Create visualization
    create_dice_visualization()
    
    # Run simulation
    simulate_dice_rolls(1000)
    
    # Probability rules examples
    probability_rules_examples()
    
    print("\nSlide 1 demonstration completed")

if __name__ == "__main__":
    # Check if running directly or through main.py
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        interactive_menu()
    else:
        main()

