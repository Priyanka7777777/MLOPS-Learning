

# ✅ **Step 1 — Base Class: Vehicle**

```python
class Vehicle():
```

This defines a class named **Vehicle** — the parent (base) class.

---

## 🔹 Constructor of Vehicle

```python
def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
```

* `__init__` runs automatically when you create a Vehicle.
* It receives 3 values: make, model, year.
* It stores them as object attributes:

  * `self.make`
  * `self.model`
  * `self.year`

So, `Vehicle("Toyota", "Camry", 2020)` will store those values inside the object.

---

## 🔹 Method of Vehicle

```python
def display_info(self):
    return f"{self.year} {self.make} {self.model}"
```

* Returns a formatted string like:
  `"2020 Toyota Camry"`

---

# ✅ **Step 2 — Child Class: Car inherits from Vehicle**

```python
class Car(Vehicle):
```

Car **inherits** all attributes & methods of Vehicle.

---

## 🔹 Car’s constructor

```python
def __init__(self, make, model, year, doors):
    super().__init__(make, model, year)
    self.doors = doors
```

### ✔ What happens here?

### **1️⃣ `super().__init__(make, model, year)`**

* `super()` means: **call the parent class (Vehicle)**
* So this line calls:

```python
Vehicle.__init__(self, make, model, year)
```

This automatically sets:

```
self.make = make
self.model = model
self.year = year
```

👉 **WITHOUT rewriting Vehicle’s code again.**

### **2️⃣ `self.doors = doors`**

Adds a new attribute that only Car objects have.

---

## 🔹 Car’s display_info()

```python
def display_info(self):
    base_info = super().display_info()
    return f"{base_info}, Doors: {self.doors}"
```

* `super().display_info()` calls the Vehicle version of the method.
* Example: `"2020 Toyota Camry"`
* Then Car adds door information:
  `"2020 Toyota Camry, Doors: 4"`

---

# ✅ **Step 3 — Child Class: Bike**

```python
class Bike(Vehicle):
```

Same idea: Bike inherits from Vehicle.

---

## 🔹 Bike’s constructor

```python
def __init__(self, make, model, year, type):
    super().__init__(make, model, year)
    self.type = type
```

* Calls the parent Vehicle initializer
* Adds a new property: `type` (sport, cruiser, etc.)

---

## 🔹 Bike’s display_info()

```python
def display_info(self):
    base_info = super().display_info()
    return f"{base_info}, Type: {self.type}"
```

Again, takes the base info and adds bike type.

---

# 🚗 **Example usage**

```python
car = Car("Toyota", "Camry", 2020, 4)
bike = Bike("Yamaha", "MT-07", 2021, "Sport")
```

* Creates Car and Bike objects with their respective attributes.

---

## Printing:

```python
print(car.display_info())
print(bike.display_info())
```

Output:

```
2020 Toyota Camry, Doors: 4
2021 Yamaha MT-07, Type: Sport
```

---

# ⭐ MOST IMPORTANT: What exactly does `super()` do?

`super()` allows a child class to:

### ✔ Reuse parent code

Instead of writing the same `__init__` code in Car and Bike, we just call Vehicle’s version.

### ✔ Prevent duplication

Avoids repeating:

```python
self.make = make
self.model = model
self.year = year
```

### ✔ Ensure proper method order in multiple inheritance

`super()` makes Python follow method resolution order (MRO).

### ✔ Let child override parent AND still use parent logic

Example:

```python
base = super().display_info()
```

Car & Bike modify the result but still use the parent's version.

---

# 🎉 Summary (Easy to Remember)

| What                             | Why                                   |
| -------------------------------- | ------------------------------------- |
| `class Car(Vehicle)`             | Car inherits properties from Vehicle  |
| `super().__init__()`             | Calls parent class constructor        |
| `super().display_info()`         | Calls parent class method             |
| Child classes add new attributes | doors for Car, type for Bike          |
| Polymorphism                     | Same method name, different behaviors |

