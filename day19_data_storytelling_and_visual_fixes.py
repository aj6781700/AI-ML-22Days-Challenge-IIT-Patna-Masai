"""
DAY 19 — Data Storytelling & Fixing Bad Visuals
i-Hub IIT Patna × Masai School

Goal:
- Turn charts into insights
- Fix bad visuals
- Build business storytelling mindset
"""

import matplotlib.pyplot as plt
import numpy as np

# Dataset (Experience vs Salary)
experience = np.array([1, 3, 5, 7, 10, 12])
salary = np.array([25000, 35000, 45000, 55000, 70000, 90000])

# ---------------------------------------
# ❌ BAD VISUAL — CONFUSING & LOW QUALITY
# ---------------------------------------
plt.figure(figsize=(5, 3))
plt.plot(experience, salary, 'r--x')
plt.title("Salary Graph")
plt.savefig("day19_BAD_visual.png")
plt.close()


# ---------------------------------------
# ✅ FIXED VISUAL — STORY + INSIGHT
# ---------------------------------------
plt.figure(figsize=(8, 5))
plt.plot(experience, salary, color="#0073e6", marker="o", linewidth=4)

plt.title("How Experience Impacts Salary", fontsize=16, fontweight="bold")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary (INR)")

plt.grid(alpha=0.3)
plt.text(7, 83000, "Insight: Salary jumps after 7+ years!", fontsize=10, color="green")

# 🎯 STORY STATEMENT
print("\nSTORY:")
print("As experience increases, salary grows steadily.")
print("The sharp jump after ~7 years highlights the value of long-term expertise.")

plt.savefig("day19_FIXED_visual.png")
plt.show()
