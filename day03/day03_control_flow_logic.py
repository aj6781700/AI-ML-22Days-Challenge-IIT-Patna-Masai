"""
Day 03 — Control Flow, Logical Thinking & Code Discipline
---------------------------------------------------------
Focus:
- if / elif / else decision making
- looping with conditions
- clean logical structure
"""

def classify_number(num: int) -> str:
    """
    Classify a number based on value.
    This simulates decision logic used in ML rule-based systems.
    """
    if num < 0:
        return "Negative number"
    elif num == 0:
        return "Zero"
    elif 0 < num <= 10:
        return "Small positive number"
    else:
        return "Large positive number"


def analyze_dataset(numbers: list[int]) -> None:
    """
    Analyze a list of numbers using control flow.
    """
    print("Analyzing dataset...\n")

    for n in numbers:
        result = classify_number(n)
        print(f"Value: {n} --> Category: {result}")


if __name__ == "__main__":
    sample_data = [-5, 0, 3, 8, 15, 42]
    analyze_dataset(sample_data)
