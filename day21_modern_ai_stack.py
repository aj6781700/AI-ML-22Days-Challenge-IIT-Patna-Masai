"""
DAY 21 — Modern AI Stack & AI Lifecycle
i-Hub IIT Patna × Masai School

This file prints an industry AI workflow and stack overview.
ASCII only (Windows-friendly)
"""

def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70 + "\n")


# 1️⃣ Modern AI Lifecycle
section("1. MODERN AI LIFECYCLE (END-TO-END)")

lifecycle = [
    "1. Problem Understanding",
    "2. Data Collection",
    "3. Data Cleaning & Preprocessing",
    "4. Feature Engineering",
    "5. Model Selection & Training",
    "6. Evaluation & Optimization",
    "7. Deployment (API / App / Cloud)",
    "8. Monitoring & Improvement"
]

for step in lifecycle:
    print("- " + step)


# 2️⃣ AI TECH STACK (TOOLS USED IN INDUSTRY)
section("2. MODERN AI TECH STACK (TOOLS)")

stack = {
    "Data Collection": "Python, APIs, Web Scraping, SQL",
    "Data Processing": "Pandas, NumPy, Polars",
    "Model Building": "Scikit-Learn, TensorFlow, PyTorch",
    "Experiment Tracking": "MLflow, Weights & Biases",
    "Deployment": "FastAPI, Flask, Streamlit, ONNX",
    "Cloud/Compute": "AWS, GCP, Azure, HuggingFace Spaces",
    "Monitoring": "Grafana, Prometheus, logging systems"
}

for k, v in stack.items():
    print(f"- {k}: {v}")


# 3️⃣ AI JOB ROLES & RESPONSIBILITIES
section("3. AI ROLES IN INDUSTRY")

roles = [
    "Machine Learning Engineer - Builds & deploys ML models",
    "Data Scientist - Data exploration, modeling, insights",
    "MLOps Engineer - Automates pipelines & deployment",
    "AI Researcher - Designs new algorithms & architectures",
    "Prompt Engineer - Optimizes prompts for LLMs"
]

for r in roles:
    print("- " + r)


# 4️⃣ MODEL DEVELOPMENT FLOW IN CODE FORM
section("4. PRACTICAL MODEL DEVELOPMENT FLOW (SIMPLE CODE PLAN)")

code_plan = [
    "load_data()",
    "clean_data()",
    "create_features()",
    "train_model()",
    "evaluate()",
    "save_model()",
    "deploy_model()"
]

for step in code_plan:
    print("-> " + step)


# 5️⃣ FINAL TAKEAWAY
section("FINAL TAKEAWAY")
print("A model is not enough. Real AI systems need:")
print("- Data pipelines")
print("- Deployment strategy")
print("- Monitoring & Improvement")
print("- Business understanding")
print("\nConclusion: AI is 10% model, 90% system design.\n")

