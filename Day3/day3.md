

# 📘 **Day 3 — Object-Oriented Programming (OOP) for ML & MLOps**

Today you will learn the fundamentals of OOP and how it applies to real machine learning and MLOps systems.

---

# 🎯 **Learning Objectives**

By the end of Day 3, you will understand:

✔ Classes
✔ Objects
✔ Constructor (`__init__`)
✔ Encapsulation
✔ Inheritance
✔ Polymorphism
✔ Why OOP is essential in ML & MLOps
✔ Building a real mini project using OOP

---

# 🧠 **1. What Is OOP?**

OOP is a programming paradigm where code is organized into **objects**, not just functions.
This helps with:

* clean code
* scalability
* large project organization
* maintainability
* reusability

---

# 🧠 **2. Class & Object Basics**

### **Class = Blueprint**

### **Object = Instance created from the class**

Example:

```python
class Car:
    def __init__(self, brand, mileage):
        self.brand = brand
        self.mileage = mileage

car1 = Car("Toyota", 18)
```

---

# 🧠 **3. The `__init__` Constructor**

Runs automatically when an object is created.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

# 🧠 **4. Encapsulation (Data Protection)**

Encapsulation = Hiding internal details.

Use **private variables** with `__`.

```python
class Bank:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amt):
        self.__balance += amt

    def get_balance(self):
        return self.__balance
```

---

# 🧠 **5. Inheritance (Code Reuse)**

Child class inherits from parent class.

```python
class Animal:
    def speak(self):
        return "Sound"

class Dog(Animal):
    def speak(self):
        return "Bark"
```

---

# 🧠 **6. Polymorphism (Same Method, Different Behavior)**

```python
for animal in [Dog(), Cat()]:
    print(animal.speak())
```

---

# 🧠 **7. Why OOP Is Crucial in MLOps**

MLOps pipelines use OOP to structure:

* model training classes
* dataset loaders
* preprocessing pipelines
* monitoring & logging components
* deployment handlers
* API wrappers

Example (real-world style):

```python
class ModelTrainer:
    def train(self, data):
        pass
    
    def evaluate(self, data):
        pass
```

---

# 🧩 **8. OOP Mini Project: Text Analyzer (Advanced)**

You will expand the Day-2 project into an OOP-based tool.

### **Folder Structure**

```
DAY3/
    text_analyzer/
        __init__.py
        analyzer.py
        utils.py
    run.py
```

---

# 📝 **analyzer.py**

```python
class TextAnalyzer:
    def __init__(self, text):
        self.text = text

    def word_count(self):
        return len(self.text.split())

    def char_count(self):
        return len(self.text)

    def top_n_words(self, n=3):
        words = self.text.split()
        freq = {}

        for w in words:
            freq[w] = freq.get(w, 0) + 1

        sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return sorted_words[:n]
```

---

# 📝 **utils.py**

```python
import string

def clean_text(text):
    return text.lower().strip()

def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))
```

---

# 📝 **run.py**

```python
from text_analyzer.analyzer import TextAnalyzer
from text_analyzer.utils import clean_text, remove_punctuation

text = "Hello, world! This is my Day-3 OOP practice. Hello again!"

cleaned = remove_punctuation(clean_text(text))
analyzer = TextAnalyzer(cleaned)

print("Words:", analyzer.word_count())
print("Chars:", analyzer.char_count())
print("Top words:", analyzer.top_n_words(3))
```

---

# 🧪 **9. Day-3 Exercises**

### ✔ Exercise 1

Create a class `Calculator` with:

* add
* subtract
* multiply
* divide

### ✔ Exercise 2

Create a class `FileReader` with:

* read file
* count lines
* count words

### ✔ Exercise 3

Use **inheritance** to create:

```
Vehicle → Car, Bike
```

### ✔ Exercise 4 (MLOps-focused)

Create a class `MLModel` with:

* train()
* predict()
* evaluate()

---

# 📝 **10. Day-3 Assignment**

Create:

```
day3_oop_assignment/
    ml_pipeline/
        __init__.py
        preprocess.py
        trainer.py
        evaluator.py
    run_pipeline.py
```

### Requirements:

### 🔹 preprocess.py

Class `Preprocessor`

* clean_text
* remove_stopwords

### 🔹 trainer.py

Class `Trainer`

* train()
* save_model()

### 🔹 evaluator.py

Class `Evaluator`

* accuracy
* confusion_matrix

### 🔹 run_pipeline.py

Create objects for all classes and run a mock ML pipeline.

---

# 🎉 End of Day 3


