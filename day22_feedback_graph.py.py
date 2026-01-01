"""
DAY 22 — FEEDBACK SHOWCASE (PRO VERSION)
22-Day AI/ML Learning Journey Feedback Graph
i-Hub IIT Patna × Masai School
"""

import matplotlib.pyplot as plt

# Rating bars
ratings = [1, 2, 3, 4, 5]
counts = [10, 20, 40, 70, 120]  # placeholder audience count, graph frame only

fig, ax = plt.subplots(figsize=(13, 7))
bars = ax.bar(ratings, counts, width=0.6, color="#5AB3E8", edgecolor="black")

# Title
ax.set_title("22-Day AI/ML Learning Journey — How Did I Do?", fontsize=20, weight='bold', pad=15)

# Axis labels
ax.set_xlabel("Rate My 22-Day Program (1 = Poor, 5 = Outstanding)", fontsize=12)
ax.set_ylabel("Audience Support", fontsize=12)

# Remove Y ticks for cleaner look
ax.set_yticks([])

# Add bar labels
for i, v in enumerate(counts):
    ax.text(ratings[i], v + 5, f"{ratings[i]}★", ha='center', fontsize=12, weight='bold')

# Add a professional feedback box on right side
text_msg = (
    "📌 I completed a 22-Day AI/ML Learning Challenge!\n\n"
    "📍 Platforms: i-Hub IIT Patna × Masai School\n"
    "🎯 Topics Covered:\n"
    " - Python, Numpy, Pandas, Matplotlib\n"
    " - Data Cleaning & EDA\n"
    " - Regression & ML Models\n"
    " - AI Lifecycle & Modern Stack\n\n"
    "💡 Please Rate My Performance from 1 to 5!\n"
    "👀 Drop your rating in the comments 👇\n"
    "Your feedback helps me improve! 🙌"
)

props = dict(boxstyle="round,pad=0.8", facecolor="#F7F7F7", edgecolor="black")
plt.text(1.12, 0.5, text_msg, transform=ax.transAxes, fontsize=12,
         verticalalignment='center', bbox=props)

# Footer signature
plt.figtext(0.5, 0.01,
            "Created by: Adarsh Kumar jha — Thanks for supporting my journey!",
            ha="center", fontsize=11, color="black")

plt.tight_layout()
plt.show()
plt.savefig("day22_feedback_graph.png", dpi=300)            
for role in roles:
    print("- " + role)