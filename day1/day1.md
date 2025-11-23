📘 Day 1 — Python Foundations: Functions, Arguments & Clean Coding

Welcome to Day 1 of your ML & Python Engineering Foundations journey.
Today’s focus is on mastering Python functions — the building block of all ML, AI, and MLOps systems.

🔥 What You Learned Today

What functions are

How they improve reusability and structure

Return values (single & multiple)

Clean coding practices

Different types of function arguments

🧠 Types of Function Arguments
### 1. Positional Arguments
def add(a, b):
    return a + b

2. Keyword Arguments
power(base=10, exp=2)

3. Default Arguments
def connect(host="localhost"):
    return host

4. *args — Variable Positional Arguments
def total(*nums):
    return sum(nums)

5. **kwargs — Variable Keyword Arguments
def config(**settings):
    return settings

🧠 Multiple Return Values
def stats(nums):
    return max(nums), min(nums), sum(nums)/len(nums)

🧼 Writing Clean, Professional Functions
def summarize(text: str) -> tuple[int, int]:
    """
    Returns word count and character count for a given text.
    """
    return len(text.split()), len(text)

🧪 Mini Tasks You Completed

Prime number checker

Reverse a string

Count vowels

Dictionary statistics (max, min, average)

📦 Day 1 Assignment (Included in code file)

Your file:

day1_python_basics.py


Includes:

✔ function with *args

✔ function with **kwargs

✔ function with type hints

✔ function returning multiple values

✔ a script calling all the above