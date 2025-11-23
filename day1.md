📘 Day 1 — Python Foundations: Functions, Arguments & Clean Coding

Welcome to Day 1 of your ML & Python Engineering Foundations journey.
Today focuses on mastering Python functions, which form the core of every ML, MLOps, and backend pipeline.

🔥 What You Learned Today
✅ Python Functions

What functions are

How functions improve code reusability

Return values & multiple returns

🧠 Types of Function Arguments
1. Positional Arguments

Passed in order.

def add(a, b):
    return a + b

2. Keyword Arguments

Order doesn’t matter.

power(base=10, exp=2)

3. Default Arguments

Provide fallback values.

def connect(host="localhost"):
    return host

*4. args — Variable Positional Arguments

Useful when number of inputs is unknown.

def total(*nums):
    return sum(nums)

**5. kwargs — Variable Keyword Arguments

Great for ML hyperparameters.

def config(**settings):
    return settings

🧠 Multiple Return Values

Python can return more than one value at a time — important for ML metrics, preprocessing, and analysis.

def stats(nums):
    return max(nums), min(nums), sum(nums)/len(nums)

🧼 Writing Clean, Professional Functions

You learned to use:

✔ Type hints
✔ Docstrings
✔ Meaningful names
✔ Clean return patterns

Example:

def summarize(text: str) -> tuple[int, int]:
    """
    Returns word count and character count for a given text.
    """
    return len(text.split()), len(text)

🧪 Mini Tasks Completed

Prime number checker

Reverse a string

Count vowels in a sentence

Dictionary statistics function

📦 Day 1 Assignment (Completed in code file)

The file:

day1_python_basics.py


contains:

✔ function with *args
✔ function with **kwargs
✔ function with type hints
✔ function returning multiple values
✔ script section that executes all functions

📁 Folder Suggestion (for your repo)
week1/
    day1/
        day1_python_basics.py
        README.md  ← (this file)
