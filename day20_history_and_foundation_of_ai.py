"""
DAY 20 — History & Foundations of Artificial Intelligence
i-Hub IIT Patna × Masai School

Compatible with Windows CMD / VS Code (no unicode issues)
"""

def print_section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60 + "\n")


# --- WHAT IS AI ---
print_section("WHAT IS AI?")
print("AI is the science of building systems that learn and take decisions like humans.")
print("Formula: AI = Data + Math + Programming + Logic\n")


# --- HISTORY TIMELINE ---
print_section("AI HISTORY TIMELINE")

timeline = [
    "1950 - Alan Turing proposes 'Can machines think?'",
    "1956 - Name 'Artificial Intelligence' introduced (Dartmouth)",
    "1980s - Expert systems (Rule-based AI)",
    "1997 - IBM Deep Blue beats world chess champion",
    "2012 - Deep Learning breakthrough (ImageNet, AlexNet)",
    "2020 and beyond - GPT, Transformers, modern multimodal AI"
]

for event in timeline:
    print(" - " + event)


# --- FOUNDATIONAL COMPONENTS ---
print_section("FOUNDATIONAL COMPONENTS OF AI")

foundations = [
    "Data (Fuel of AI)",
    "Mathematics (Algebra, Calculus, Probability)",
    "Programming (Python)",
    "ML Algorithms",
    "Deep Learning (Neural Networks)",
    "Deployment for real-world usage"
]

for item in foundations:
    print(" - " + item)


# --- WHY AI IS IMPORTANT TODAY ---
print_section("WHY AI IS IMPORTANT TODAY")

importance_points = [
    "Automation and productivity",
    "Data-driven decision making",
    "Real-time recommendations (Ads, Streaming)",
    "Voice / Language models (ChatGPT, Alexa)",
    "Autonomous Systems (Vision, Self Driving)"
]

for point in importance_points:
    print(" - " + point)


# --- SUMMARY ---
print_section("FINAL TAKEAWAY")
print("Modern AI works because of: Data + Compute Power + Mathematics + Human Design")
print("AI is not magic, it is engineered logic built on patterns.")
print("DAY 20 COMPLETED")

