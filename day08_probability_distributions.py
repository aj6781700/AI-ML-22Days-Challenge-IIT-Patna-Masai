"""
Day 08 — Probability & Data Distributions for ML
------------------------------------------------
Focus:
- Basic probability concepts
- Random variables
- Normal (Gaussian) distribution
- Empirical probability from data
- Why distributions matter in ML
"""

import numpy as np


def basic_probability(event_count: int, total_count: int) -> float:
    """Calculate basic probability."""
    return event_count / total_count


def simulate_dice_rolls(trials: int = 10000) -> None:
    """Simulate dice rolls to estimate probability."""
    dice = np.random.randint(1, 7, size=trials)
    prob_six = np.mean(dice == 6)
    print("Estimated P(dice = 6):", round(prob_six, 4))


def normal_distribution_demo() -> None:
    """Demonstrate normal distribution properties."""
    data = np.random.normal(loc=50, scale=10, size=10000)

    print("\nNormal Distribution Stats:")
    print("Mean :", round(np.mean(data), 2))
    print("Std  :", round(np.std(data), 2))

    # Probability within 1 std (empirical rule)
    within_1_std = np.mean(
        (data >= np.mean(data) - np.std(data)) &
        (data <= np.mean(data) + np.std(data))
    )
    print("P(within 1 std):", round(within_1_std, 4))


if __name__ == "__main__":
    print("Basic Probability Example:")
    p = basic_probability(event_count=1, total_count=6)
    print("P(getting 6 on a dice):", round(p, 4))

    print("\nSimulation using Random Sampling:")
    simulate_dice_rolls()

    normal_distribution_demo()
