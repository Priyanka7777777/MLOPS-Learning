Sure! Here is your **Day-1 content in clean Markdown format**, ready to copy into a file like
`DAY_1_Python_Basics.md` for your GitHub repo.

---

# 📘 **Day 1 — Python Foundations: Functions, Arguments & Modules**

Welcome to **Week 1, Day 1** of your ML & Python Engineering journey.
Today you will learn and practice the essential Python fundamentals used in real engineering and MLOps systems.

---

## 🔥 **Topics Covered**

* Python Functions (deep explanation)
* Argument Types

  * positional
  * keyword
  * default
  * *args
  * **kwargs
* Multiple return values
* Writing clean professional functions
* Day-1 Coding Exercises
* Day-1 Assignment (to push on GitHub)

---

# 🧠 **1. What is a Function?**

A function is a reusable block of code that performs a specific task.

### **Function Structure**

```python
def function_name(parameters):
    # logic
    return result
```

### **Example**

```python
def greet(name):
    return f"Hello, {name}!"
```

---

# 🧠 **2. Types of Python Arguments**

## **A) Positional Arguments**

Passed in correct order.

```python
def add(a, b):
    return a + b

add(5, 10)
```

---

## **B) Keyword Arguments**

Order doesn’t matter.

```python
def power(base, exp):
    return base ** exp

power(exp=3, base=2)
```

---

## **C) Default Arguments**

Provide default values.

```python
def connect(host="localhost"):
    return f"Connected to {host}"
```

---

## **D) *args (Variable Positional Arguments)**

Useful when number of inputs is unknown.

```python
def total(*nums):
    return sum(nums)
```

---

## **E) **kwargs (Variable Keyword Arguments)**

Used for configuration-heavy code such as ML hyperparameters.

```python
def config(**settings):
    return settings

config(learning_rate=0.01, batch_size=32)
```

---

# 🧠 **3. Multiple Return Values**

Python allows returning multiple outputs.

```python
def stats(nums):
    mx = max(nums)
    mn = min(nums)
    avg = sum(nums) / len(nums)
    return mx, mn, avg
```

---

# 🧠 **4. Writing Clean, Professional Functions**

Follow best practices:

✔ type hints
✔ docstrings
✔ meaningful names
✔ return values

```python
def preprocess_text(text: str) -> tuple[int, int]:
    """
    Returns word count and character count of text.
    """
    words = len(text.split())
    chars = len(text)
    return words, chars
```

---

# 🧪 **5. Day-1 Coding Tasks**

Write Python functions for:

### **1️⃣ Check if a number is prime**

### **2️⃣ Reverse a string**

### **3️⃣ Count vowels in a sentence**

### **4️⃣ Return: max_key, min_key, average_value from a dictionary**


---

# 📝 **6. Day-1 Assignment (Your Deliverable)**

Create a file named:

```
day1_python_basics.py
```

It must include:

* A function using `*args`
* A function using `**kwargs`
* A function with **type hints**
* A function returning **multiple values**
* A script section that **calls all functions**

### **Example Outline**

```python
def add_numbers(*args):
    return sum(args)

def configure_model(**kwargs):
    return kwargs

def text_summary(text: str) -> tuple[int, int]:
    words = len(text.split())
    chars = len(text)
    return words, chars

def calc_stats(nums: list[int]) -> tuple[int, int, float]:
    return max(nums), min(nums), sum(nums)/len(nums)

# Script section
if __name__ == "__main__":
    print(add_numbers(1, 2, 3))
    print(configure_model(lr=0.001, batch_size=32))
    print(text_summary("Hello world"))
    print(calc_stats([5, 10, 15]))
```

---

# ✅ **End of Day 1**

Tomorrow you will begin **Modules & Packages (Day-2)** and start building our first Python package.


