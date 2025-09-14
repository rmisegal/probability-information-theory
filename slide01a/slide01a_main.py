#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Slide 1a: Basic Probability Concepts
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
        slide_path = Path(__file__).parent / "slide1a.html"
        if slide_path.exists():
            webbrowser.open(f"file://{slide_path.absolute()}")
            print(f"Slide opened in browser: {slide_path}")
        else:
            print(f"HTML slide not found: {slide_path}")
    except Exception as e:
        print(f"Error opening slide: {e}")

def create_dice_probability_chart():
    """Create basic dice probability chart"""
    print("\n=== Dice Probability Calculations ===")
    
    # Calculate theoretical probabilities
    outcomes = [1, 2, 3, 4, 5, 6]
    probabilities = [1/6] * 6  # Each outcome has probability 1/6
    
    print("Theoretical Probabilities:")
    for outcome, prob in zip(outcomes, probabilities):
        print(f"  P(rolling {outcome}) = {prob:.3f}")
    
    # Calculate some combined probabilities
    prob_even = 3/6  # Rolling 2, 4, or 6
    prob_greater_than_4 = 2/6  # Rolling 5 or 6
    prob_not_1 = 5/6  # Not rolling 1
    
    print(f"\nCombined Probabilities:")
    print(f"  P(even number) = {prob_even:.3f}")
    print(f"  P(greater than 4) = {prob_greater_than_4:.3f}")
    print(f"  P(not rolling 1) = {prob_not_1:.3f}")
    
    # Create the visualization
    plt.figure(figsize=(10, 6))
    
    # Create bar chart
    bars = plt.bar(outcomes, probabilities, color='#12377A', alpha=0.8, 
                   edgecolor='#0f2d5f', linewidth=2)
    
    # Add values on bars
    for bar, prob in zip(bars, probabilities):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.005,
                f'{prob:.3f}', ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    # Style the plot
    plt.title('Slide 1a: Fair Dice Roll Probabilities', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Dice Outcome', fontsize=14)
    plt.ylabel('Probability', fontsize=14)
    plt.ylim(0, 0.2)
    plt.grid(axis='y', alpha=0.3)
    
    # Add theoretical line
    plt.axhline(y=1/6, color='red', linestyle='--', alpha=0.7, label='Theoretical Probability (1/6)')
    plt.legend()
    
    # Add text box with key concepts
    textstr = 'Key Concepts:\n• Each outcome equally likely\n• Sum of all probabilities = 1\n• P(event) = favorable/total'
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
    plt.text(0.02, 0.98, textstr, transform=plt.gca().transAxes, fontsize=10,
             verticalalignment='top', bbox=props)
    
    plt.tight_layout()
    
    # Save the plot
    output_path = Path(__file__).parent / "dice_probability_basic.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Chart saved to: {output_path}")
    
    # Show plot if not in test mode
    if matplotlib.get_backend() != 'Agg':
        plt.show()
    
    plt.close()  # Important: close the figure to prevent empty windows
    
    return output_path

def explain_probability_concepts():
    """Explain basic probability concepts with formulas and code"""
    print("\n=== Basic Probability Concepts ===")
    
    print("1. SAMPLE SPACE (Ω):")
    print("   DEFINITION: The set of all possible outcomes of an experiment")
    print("   FORMULA: Ω = {ω₁, ω₂, ..., ωₙ}")
    print("   For a dice: Ω = {1, 2, 3, 4, 5, 6}")
    print("   PYTHON CODE:")
    print("   sample_space = list(range(1, 7))  # [1, 2, 3, 4, 5, 6]")
    print("   print(f'Sample space size: {len(sample_space)}')")
    
    # Demonstrate with code
    sample_space = list(range(1, 7))
    print(f"   → Sample space size: {len(sample_space)}")
    
    print("\n2. EVENT (E):")
    print("   DEFINITION: A subset of the sample space")
    print("   FORMULA: E ⊆ Ω")
    print("   Example: E = {2, 4, 6} (rolling an even number)")
    print("   PYTHON CODE:")
    print("   even_event = [x for x in sample_space if x % 2 == 0]")
    print("   print(f'Even numbers event: {even_event}')")
    
    # Demonstrate with code
    even_event = [x for x in sample_space if x % 2 == 0]
    print(f"   → Even numbers event: {even_event}")
    
    print("\n3. PROBABILITY (P):")
    print("   DEFINITION: A measure of the likelihood of an event")
    print("   FORMULA: P(E) = |E| / |Ω| (for equally likely outcomes)")
    print("   Where |E| = number of favorable outcomes, |Ω| = total outcomes")
    print("   For fair dice: P(any number) = 1/6 ≈ 0.167")
    print("   PYTHON CODE:")
    print("   def calculate_probability(event, sample_space):")
    print("       return len(event) / len(sample_space)")
    print("   prob_even = calculate_probability(even_event, sample_space)")
    
    # Demonstrate with code
    def calculate_probability(event, sample_space):
        return len(event) / len(sample_space)
    
    prob_even = calculate_probability(even_event, sample_space)
    print(f"   → P(even) = {len(even_event)}/{len(sample_space)} = {prob_even:.3f}")
    
    print("\n4. PROBABILITY AXIOMS (Kolmogorov):")
    print("   AXIOM 1: P(E) ≥ 0 for any event E")
    print("   AXIOM 2: P(Ω) = 1 (certainty)")
    print("   AXIOM 3: P(A ∪ B) = P(A) + P(B) if A ∩ B = ∅ (mutually exclusive)")
    print("   PYTHON CODE:")
    print("   # Verify axioms")
    print("   all_probs = [calculate_probability([i], sample_space) for i in sample_space]")
    print("   print(f'All probabilities ≥ 0: {all(p >= 0 for p in all_probs)}')")
    print("   print(f'Sum of all probabilities: {sum(all_probs)}')")
    
    # Demonstrate with code
    all_probs = [calculate_probability([i], sample_space) for i in sample_space]
    print(f"   → All probabilities ≥ 0: {all(p >= 0 for p in all_probs)}")
    print(f"   → Sum of all probabilities: {sum(all_probs):.3f}")
    
    print("\n5. COMPLEMENT:")
    print("   DEFINITION: The complement of event E contains all outcomes not in E")
    print("   FORMULA: P(Eᶜ) = 1 - P(E)")
    print("   PYTHON CODE:")
    print("   complement_even = [x for x in sample_space if x not in even_event]")
    print("   prob_odd = calculate_probability(complement_even, sample_space)")
    print("   print(f'P(odd) = 1 - P(even) = 1 - {prob_even:.3f} = {1-prob_even:.3f}')")
    
    # Demonstrate with code
    complement_even = [x for x in sample_space if x not in even_event]
    prob_odd = calculate_probability(complement_even, sample_space)
    print(f"   → Odd numbers: {complement_even}")
    print(f"   → P(odd) = 1 - P(even) = 1 - {prob_even:.3f} = {1-prob_even:.3f}")
    
    return sample_space, even_event, all_probs

def demonstrate_probability_rules():
    """Demonstrate probability rules with dice examples, formulas and code"""
    print("\n=== Probability Rules with Dice Examples ===")
    
    # Rule 1: Addition for mutually exclusive events
    print("1. ADDITION RULE (Mutually Exclusive Events):")
    print("   DEFINITION: Events that cannot occur simultaneously")
    print("   FORMULA: P(A ∪ B) = P(A) + P(B) if A ∩ B = ∅")
    print("   EXAMPLE: Rolling 1 OR rolling 2 (mutually exclusive)")
    print("   PYTHON CODE:")
    print("   event_1 = [1]")
    print("   event_2 = [2]")
    print("   prob_1 = len(event_1) / 6")
    print("   prob_2 = len(event_2) / 6")
    print("   prob_1_or_2 = prob_1 + prob_2  # Addition rule")
    
    # Demonstrate with code
    event_1 = [1]
    event_2 = [2]
    prob_1 = len(event_1) / 6
    prob_2 = len(event_2) / 6
    prob_1_or_2 = prob_1 + prob_2
    print(f"   → P(rolling 1 or 2) = P(1) + P(2) = {prob_1:.3f} + {prob_2:.3f} = {prob_1_or_2:.3f}")
    
    # Rule 2: Complement
    print("\n2. COMPLEMENT RULE:")
    print("   DEFINITION: The probability of an event NOT occurring")
    print("   FORMULA: P(Aᶜ) = 1 - P(A)")
    print("   EXAMPLE: NOT rolling a 6")
    print("   PYTHON CODE:")
    print("   event_6 = [6]")
    print("   prob_6 = len(event_6) / 6")
    print("   prob_not_6 = 1 - prob_6  # Complement rule")
    print("   # Alternative: count non-6 outcomes")
    print("   event_not_6 = [1, 2, 3, 4, 5]")
    print("   prob_not_6_alt = len(event_not_6) / 6")
    
    # Demonstrate with code
    event_6 = [6]
    prob_6 = len(event_6) / 6
    prob_not_6 = 1 - prob_6
    event_not_6 = [1, 2, 3, 4, 5]
    prob_not_6_alt = len(event_not_6) / 6
    print(f"   → P(not rolling 6) = 1 - P(6) = 1 - {prob_6:.3f} = {prob_not_6:.3f}")
    print(f"   → Verification: P(not 6) = {len(event_not_6)}/6 = {prob_not_6_alt:.3f}")
    
    # Rule 3: Total probability
    print("\n3. TOTAL PROBABILITY RULE:")
    print("   DEFINITION: Sum of probabilities of all possible outcomes equals 1")
    print("   FORMULA: Σ P(ωᵢ) = 1 for all ωᵢ ∈ Ω")
    print("   PYTHON CODE:")
    print("   all_outcomes = list(range(1, 7))")
    print("   individual_probs = [1/6 for _ in all_outcomes]")
    print("   total_prob = sum(individual_probs)")
    
    # Demonstrate with code
    all_outcomes = list(range(1, 7))
    individual_probs = [1/6 for _ in all_outcomes]
    total_prob = sum(individual_probs)
    print(f"   → P(1) + P(2) + P(3) + P(4) + P(5) + P(6) = {total_prob:.3f}")
    
    # Rule 4: Conditional probability
    print("\n4. CONDITIONAL PROBABILITY:")
    print("   DEFINITION: Probability of A given that B has occurred")
    print("   FORMULA: P(A|B) = P(A ∩ B) / P(B)")
    print("   EXAMPLE: P(rolling 6 | rolling even number)")
    print("   PYTHON CODE:")
    print("   event_even = [2, 4, 6]")
    print("   event_6_and_even = [6]  # Intersection")
    print("   prob_even = len(event_even) / 6")
    print("   prob_6_and_even = len(event_6_and_even) / 6")
    print("   prob_6_given_even = prob_6_and_even / prob_even")
    
    # Demonstrate with code
    event_even = [2, 4, 6]
    event_6_and_even = [6]  # 6 is the only number that is both 6 AND even
    prob_even = len(event_even) / 6
    prob_6_and_even = len(event_6_and_even) / 6
    prob_6_given_even = prob_6_and_even / prob_even
    print(f"   → P(6|even) = P(6 ∩ even) / P(even)")
    print(f"   → = {prob_6_and_even:.3f} / {prob_even:.3f} = {prob_6_given_even:.3f}")
    print(f"   → Interpretation: Out of 3 even numbers, 1 is a 6, so 1/3 = 0.333")
    
    # Rule 5: Independence
    print("\n5. INDEPENDENCE:")
    print("   DEFINITION: Two events are independent if one doesn't affect the other")
    print("   FORMULA: P(A ∩ B) = P(A) × P(B) if A and B are independent")
    print("   EXAMPLE: Two dice rolls are independent")
    print("   PYTHON CODE:")
    print("   # Rolling 6 on first die AND 6 on second die")
    print("   prob_6_first = 1/6")
    print("   prob_6_second = 1/6")
    print("   prob_both_6 = prob_6_first * prob_6_second  # Independence")
    
    # Demonstrate with code
    prob_6_first = 1/6
    prob_6_second = 1/6
    prob_both_6 = prob_6_first * prob_6_second
    print(f"   → P(6 on die 1 AND 6 on die 2) = {prob_6_first:.3f} × {prob_6_second:.3f} = {prob_both_6:.3f}")
    
    return {
        'addition_rule': prob_1_or_2,
        'complement_rule': prob_not_6,
        'total_probability': total_prob,
        'conditional_probability': prob_6_given_even,
        'independence': prob_both_6
    }

def main():
    """Main demonstration function"""
    print("Slide 1a: Basic Probability Concepts")
    print("Lecturer: Dr. Yoram Segal")
    print("=" * 50)
    
    # Explain basic concepts
    explain_probability_concepts()
    
    # Create visualization
    create_dice_probability_chart()
    
    # Demonstrate rules
    demonstrate_probability_rules()
    
    print("\nSlide 1a demonstration completed")
    print("This slide covers the fundamental concepts of probability theory.")

if __name__ == "__main__":
    main()

