"""
Day 14 — Efficient Image Operations & Data Storytelling
------------------------------------------------------
Focus:
- Efficient image operations using NumPy
- Vectorized transformations
- Preparing image data for ML
- Understanding how results are communicated
"""

import numpy as np


def efficient_image_operations():
    """
    Simulate an image and apply efficient operations.
    """
    # Simulated grayscale image (5x5)
    image = np.array([
        [20, 50, 80, 120, 200],
        [30, 60, 90, 130, 210],
        [40, 70, 100, 140, 220],
        [50, 80, 110, 150, 230],
        [60, 90, 120, 160, 240]
    ])

    print("Original Image:\n", image)

    # 🔹 Normalization (ML-ready)
    normalized = image / 255.0
    print("\nNormalized Image:\n", normalized)

    # 🔹 Contrast scaling (efficient & vectorized)
    contrast_scaled = np.clip((image - 50) * 1.2, 0, 255)
    print("\nContrast Scaled Image:\n", contrast_scaled)

    return normalized, contrast_scaled


def storytelling_summary():
    """
    Data storytelling summary (conceptual).
    """
    print("\n--- DATA STORYTELLING INSIGHTS ---")
    print("• Raw numbers don’t drive decisions — insights do")
    print("• Efficient preprocessing improves ML performance")
    print("• Clear visuals beat complex visuals")
    print("• Storytelling bridges data and stakeholders")
    print("• ML success = correct model + correct story")


if __name__ == "__main__":
    efficient_image_operations()
    storytelling_summary()
