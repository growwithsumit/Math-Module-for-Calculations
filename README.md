# Python Mathematical Scripts: Factorials & Advanced Calculations

## 📖 Overview

This repository contains a collection of fundamental Python scripts designed to perform various mathematical calculations. The projects demonstrate the use of recursive functions for calculating factorials and leveraging Python's built-in `math` module for advanced operations like square roots, natural logarithms, and trigonometric functions. These scripts are excellent examples for learning about core programming concepts and mathematical computation in Python.

---

## 🚀 Projects Included

This repository features two main Python scripts:

### 1. Recursive Factorial Calculator (`Calculate Factorial Using a Function.py`)

This program calculates the factorial of a non-negative integer provided by the user. It uses a recursive function, which is a function that calls itself to solve the problem.

* **Features:**
    * Accepts a single integer input from the user.
    * Uses a recursive function to calculate the factorial (`n!`).
    * Includes a base case (`n <= 1`) to stop the recursion.
    * Displays the final calculated factorial.
* **Concepts Demonstrated:**
    * **Functions:** Defining and calling a custom function.
    * **Recursion:** A function calling itself to break a problem into smaller parts.
    * **Base Case:** The condition that stops the recursion.
    * **User Input:** Taking and converting user input with `int(input())`.
* **Example Usage & Output:**
    ```
    Enter a number: 5
    Factorial of 5 is:  120
    ```

### 2. Advanced Math Module Calculator (`Using the Math Module for Calculations.py`)

This script showcases the power of Python's `math` module to perform several advanced mathematical operations on a number provided by the user.

* **Features:**
    * Calculates the **square root** of the number.
    * Calculates the **natural logarithm (log base e)** of the number.
    * Calculates the **sine** of the number (assuming the input is in radians).
    * Includes conditional logic to handle mathematical constraints (e.g., you can't take the square root or logarithm of a negative number).
* **Concepts Demonstrated:**
    * **`math` Module:** Importing and using library functions like `math.sqrt()`, `math.log()`, and `math.sin()`.
    * **Conditional Logic:** Using `if-else` statements to handle different scenarios based on the input number.
    * **Mathematical Constraints:** Programming respectfully of mathematical rules.
* **Example Usage & Output:**
    ```
    Enter a number: 9
    Square root:  3.0
    Logarithm:  2.1972245773362196
    Sine:  0.4121184852417566
    ```
    ```
    Enter a number: -4
    Square root is not defined for negative numbers.
    Natural log is not defined for zero or negative numbers.
    Sine:  0.7568024953079282
    ```
