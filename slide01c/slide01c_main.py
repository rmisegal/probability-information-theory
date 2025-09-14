#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Slide 1c: Histogram of 1000 Rolls
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
        slide_path = Path(__file__).parent / "slide1c.html"
        if slide_path.exists():
            webbrowser.open(f"file://{slide_path.absolute()}")
            print(f"Slide opened in browser: {slide_path}")
        else:
            print(f"HTML slide not found: {slide_path}")
    except Exception as e:
        print(f"Error opening slide: {e}")

def explain_histogram_concepts():
    """Explain histogram concepts with formulas and code"""
    print("\n=== Histogram Concepts ===")
    
    print("1. HISTOGRAM DEFINITION:")
    print("   A graphical representation of the distribution of numerical data")
    print("   Shows frequency (count) of data points in different intervals (bins)")
    print("   FORMULA: Frequency = Count of values in bin / Total count")
    print("   PYTHON CODE:")
    print("   import matplotlib.pyplot as plt")
    print("   plt.hist(data, bins=number_of_bins)")
    
    print("\n2. BINS:")
    print("   DEFINITION: Intervals that divide the range of data")
    print("   For dice (1-6): bins = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]")
    print("   PYTHON CODE:")
    print("   bins = np.arange(0.5, 7.5, 1)  # [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]")
    print("   # This creates 6 bins, one for each dice outcome")
    
    # Demonstrate with code
    bins = np.arange(0.5, 7.5, 1)
    print(f"   → Bin edges: {bins}")
    print(f"   → Number of bins: {len(bins)-1}")
    
    print("\n3. FREQUENCY vs PROBABILITY:")
    print("   FREQUENCY: Actual count of occurrences")
    print("   PROBABILITY: Frequency divided by total number of trials")
    print("   FORMULA: P(outcome) = Frequency(outcome) / Total_trials")
    print("   PYTHON CODE:")
    print("   counts, bin_edges = np.histogram(data, bins=bins)")
    print("   probabilities = counts / len(data)")
    
    print("\n4. EXPECTED vs OBSERVED:")
    print("   EXPECTED: What theory predicts (1/6 for each outcome)")
    print("   OBSERVED: What actually happens in the experiment")
    print("   FORMULA: Expected_count = Total_trials × Theoretical_probability")
    print("   For 1000 rolls: Expected_count = 1000 × (1/6) ≈ 167 for each outcome")
    
    return bins

def simulate_and_analyze_rolls(n_rolls=1000):
    """Simulate dice rolls and perform statistical analysis"""
    print(f"\n=== Statistical Analysis of {n_rolls} Dice Rolls ===")
    
    # Set seed for reproducible results
    np.random.seed(42)
    
    print("PYTHON CODE FOR SIMULATION:")
    print("import numpy as np")
    print("np.random.seed(42)  # For reproducible results")
    print(f"rolls = np.random.randint(1, 7, {n_rolls})")
    print("unique, counts = np.unique(rolls, return_counts=True)")
    
    # Generate rolls
    rolls = np.random.randint(1, 7, n_rolls)
    unique, counts = np.unique(rolls, return_counts=True)
    
    print(f"\nSIMULATION RESULTS:")
    print("Outcome | Count | Observed Freq | Expected Freq | Deviation")
    print("-" * 60)
    
    expected_count = n_rolls / 6
    expected_freq = 1/6
    
    total_deviation = 0
    for outcome, count in zip(unique, counts):
        observed_freq = count / n_rolls
        deviation = observed_freq - expected_freq
        total_deviation += abs(deviation)
        print(f"   {outcome}    | {count:4d}  |    {observed_freq:.3f}     |    {expected_freq:.3f}     | {deviation:+.3f}")
    
    print(f"\nSTATISTICAL MEASURES:")
    print(f"Mean absolute deviation: {total_deviation/6:.3f}")
    
    # Chi-square test
    print(f"\nCHI-SQUARE GOODNESS OF FIT TEST:")
    print("FORMULA: χ² = Σ[(Observed - Expected)² / Expected]")
    print("PYTHON CODE:")
    print("from scipy import stats")
    print("expected_counts = [n_rolls/6] * 6")
    print("chi2_stat = sum((obs - exp)**2 / exp for obs, exp in zip(counts, expected_counts))")
    
    expected_counts = [n_rolls/6] * 6
    chi2_stat = sum((obs - exp)**2 / exp for obs, exp in zip(counts, expected_counts))
    chi2_critical = 11.07  # Critical value for α=0.05, df=5
    
    print(f"→ Chi-square statistic: {chi2_stat:.3f}")
    print(f"→ Critical value (α=0.05): {chi2_critical:.3f}")
    print(f"→ Result: {'Fair dice' if chi2_stat < chi2_critical else 'Possibly biased dice'}")
    
    return rolls, counts, chi2_stat

def create_detailed_histogram(rolls, n_rolls=1000):
    """Create detailed histogram with statistical annotations"""
    
    # Create the histogram
    plt.figure(figsize=(14, 8))
    
    # Define bins
    bins = np.arange(0.5, 7.5, 1)
    
    # Create histogram
    counts, bin_edges, patches = plt.hist(rolls, bins=bins, color='#2E86AB', alpha=0.8, 
                                         edgecolor='black', linewidth=1.5)
    
    # Add expected line
    expected_count = n_rolls / 6
    plt.axhline(y=expected_count, color='red', linestyle='--', linewidth=2, 
                label=f'Expected count = {expected_count:.1f}')
    
    # Add count labels on bars
    for i, (count, patch) in enumerate(zip(counts, patches)):
        height = patch.get_height()
        plt.text(patch.get_x() + patch.get_width()/2., height + 5,
                f'{int(count)}', ha='center', va='bottom', fontsize=12, fontweight='bold')
        
        # Color bars based on deviation from expected
        deviation = abs(count - expected_count)
        if deviation > 20:  # Significant deviation
            patch.set_color('#E74C3C')  # Red
        elif deviation > 10:  # Moderate deviation
            patch.set_color('#F39C12')  # Orange
        else:  # Close to expected
            patch.set_color('#27AE60')  # Green
    
    # Styling
    plt.title(f'Slide 1c: Histogram of {n_rolls} Dice Rolls\nColor coding: Green=Close to expected, Orange=Moderate deviation, Red=High deviation', 
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Dice Outcome', fontsize=14)
    plt.ylabel('Frequency (Count)', fontsize=14)
    plt.xticks(range(1, 7))
    plt.grid(axis='y', alpha=0.3)
    plt.legend(fontsize=12)
    
    # Add statistical information box
    mean_roll = np.mean(rolls)
    std_roll = np.std(rolls)
    median_roll = np.median(rolls)
    
    stats_text = f'''Statistical Summary:
Mean: {mean_roll:.2f} (Expected: 3.5)
Std Dev: {std_roll:.2f} (Expected: 1.71)
Median: {median_roll:.1f}
Range: {np.min(rolls)} - {np.max(rolls)}
Sample Size: {n_rolls}'''
    
    props = dict(boxstyle='round', facecolor='lightgray', alpha=0.8)
    plt.text(0.02, 0.98, stats_text, transform=plt.gca().transAxes, fontsize=10,
             verticalalignment='top', bbox=props)
    
    # Add formula box
    formula_text = '''Key Formulas:
Frequency = Count / Total
Expected = n × P(outcome)
χ² = Σ[(Obs-Exp)²/Exp]
Mean = Σ(x × P(x))'''
    
    props2 = dict(boxstyle='round', facecolor='lightyellow', alpha=0.8)
    plt.text(0.98, 0.98, formula_text, transform=plt.gca().transAxes, fontsize=10,
             verticalalignment='top', horizontalalignment='right', bbox=props2)
    
    plt.tight_layout()
    
    # Save the plot
    output_path = Path(__file__).parent / "histogram_1000_rolls.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Histogram saved to: {output_path}")
    
    # Show plot if not in test mode
    if matplotlib.get_backend() != 'Agg':
        plt.show()
    
    plt.close()  # Important: close the figure to prevent empty windows
    
    return output_path

def demonstrate_sampling_distribution():
    """Demonstrate sampling distribution concept"""
    print(f"\n=== Sampling Distribution Concept ===")
    
    print("DEFINITION:")
    print("The distribution of a statistic (like mean) calculated from many samples")
    print("EXAMPLE: Take 100 samples of 1000 rolls each, calculate mean of each sample")
    
    print("\nPYTHON CODE:")
    print("n_samples = 100")
    print("sample_size = 1000")
    print("sample_means = []")
    print("for i in range(n_samples):")
    print("    sample = np.random.randint(1, 7, sample_size)")
    print("    sample_means.append(np.mean(sample))")
    
    # Demonstrate with smaller numbers for speed
    n_samples = 50
    sample_size = 100
    sample_means = []
    
    np.random.seed(42)
    for i in range(n_samples):
        sample = np.random.randint(1, 7, sample_size)
        sample_means.append(np.mean(sample))
    
    mean_of_means = np.mean(sample_means)
    std_of_means = np.std(sample_means)
    
    print(f"\nRESULTS ({n_samples} samples of {sample_size} rolls each):")
    print(f"Mean of sample means: {mean_of_means:.3f} (Expected: 3.5)")
    print(f"Std of sample means: {std_of_means:.3f}")
    print(f"Theoretical std: {1.71/np.sqrt(sample_size):.3f}")  # σ/√n
    
    print("\nCENTRAL LIMIT THEOREM:")
    print("As sample size increases, the sampling distribution of the mean")
    print("approaches a normal distribution, regardless of the original distribution")
    print("FORMULA: σ_x̄ = σ / √n")
    print("Where σ_x̄ = standard error of the mean")
    
    return sample_means

def main():
    """Main demonstration function"""
    print("Slide 1c: Histogram of 1000 Rolls")
    print("Lecturer: Dr. Yoram Segal")
    print("=" * 50)
    
    # Explain histogram concepts
    bins = explain_histogram_concepts()
    
    # Simulate and analyze
    rolls, counts, chi2_stat = simulate_and_analyze_rolls(1000)
    
    # Create detailed histogram
    create_detailed_histogram(rolls, 1000)
    
    # Demonstrate sampling distribution
    sample_means = demonstrate_sampling_distribution()
    
    print("\nSlide 1c demonstration completed")
    print("This slide shows how histograms reveal the distribution of data")
    print("and how statistical tests can verify if dice are fair.")

if __name__ == "__main__":
    main()

