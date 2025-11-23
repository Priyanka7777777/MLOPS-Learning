
DAY_2_Modules_and_Packages.md
```

---

# 📘 **Day 2 — Python Modules & Packages (MLOps Foundations)**

Welcome to **Day 2** of your Python Engineering journey.
Today you will learn how real ML/MLOps projects are structured using **modules, packages, and project directories**.

---

# 🎯 **Learning Objectives**

By the end of today, you will understand:

* What modules are
* What packages are
* How Python imports work
* How to create reusable utilities
* Project folder structures used in production
* How MLOps pipelines organize code

---

# 🧠 **1. What Is a Module?**

A **module** is simply a `.py` file.

Example:

```
math_utils.py
```

Inside:

```python
def square(x):
    return x * x
```

### Importing a module:

```python
import math_utils
print(math_utils.square(5))
```

### Import specific functions:

```python
from math_utils import square
```

---

# 🧠 **2. What Is a Package?**

A **package** is a folder containing multiple modules **plus** a special file:

```
__init__.py
```

Example:

```
mylib/
    __init__.py
    algebra.py
    geometry.py
    string_utils.py
```

### Importing from packages:

```python
from mylib.algebra import add
from mylib.geometry import area_circle
```

---

# 🧠 **3. Why Packages Matter in MLOps**

MLOps projects need:

✔ clean folder structure
✔ reusable components
✔ scalable pipeline design
✔ modular code for deployment

Packages solve these problems.

Typical MLOps repo:

```
src/
    data/
    features/
    models/
    utils/
    pipelines/
```

Every folder is a **package**.

---

# 🧠 **4. Creating Your Own Package**

### Step 1 — Create folder

```
text_analyzer/
```

### Step 2 — Add modules

```
text_analyzer/
    __init__.py
    analyzer.py
    utils.py
```

### Step 3 — Write code

**analyzer.py**

```python
class TextAnalyzer:
    def __init__(self, text):
        self.text = text

    def word_count(self):
        return len(self.text.split())

    def char_count(self):
        return len(self.text)
```

**utils.py**

```python
def clean_text(text):
    return text.lower().strip()
```

---

# 🧠 **5. Importing From Your Package**

```python
from text_analyzer.analyzer import TextAnalyzer
from text_analyzer.utils import clean_text
```

---

# 🧠 **6. Absolute vs. Relative Imports**

### Absolute import:

```python
from text_analyzer.utils import clean_text
```

### Relative import (within package):

```python
from .utils import clean_text
```

Relative imports are common in large ML repos.

---

# 🧩 **7. Example Project Structure for Today**

This is the structure you will create today:

```
DAY2/
    text_analyzer/
        __init__.py
        analyzer.py
        utils.py
    main.py
```

**main.py**

```python
from text_analyzer.analyzer import TextAnalyzer
from text_analyzer.utils import clean_text

text = "Hello WORLD this is Day 2"
cleaned = clean_text(text)
analyzer = TextAnalyzer(cleaned)

print("Words:", analyzer.word_count())
print("Chars:", analyzer.char_count())
```

---

# 🧪 **8. Day-2 Exercises**

### ✔ Exercise 1

Create a package named `math_ops` with:

* `add.py`
* `multiply.py`
* `stats.py`

### ✔ Exercise 2

Write a module `file_utils.py`:

* function to read a file
* function to count lines

### ✔ Exercise 3

Inside a package, use **relative import** to reuse functions.

---

# 📝 **9. Day-2 Assignment (Your Deliverable)**

Create:

```
day2_modules_and_packages/
    text_analyzer/
        __init__.py
        analyzer.py
        utils.py
    run.py
```

### Requirements:

✔ `TextAnalyzer` with

* word_count()
* char_count()
* top_n_words(n)

✔ `utils.py` with

* clean_text()
* remove_punctuation()

✔ `run.py` calling everything

# 🎉 **End of Day 2**


