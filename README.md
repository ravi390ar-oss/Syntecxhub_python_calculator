# 🧮 Simple Command-Line Calculator

A robust, menu-driven command-line calculator built with Python. This project was developed as part of my internship to demonstrate mastery of Python fundamentals, including control flow, error handling, and modular programming.

## 🚀 Features

* **Basic Arithmetic:** Supports Addition (`+`), Subtraction (`-`), Multiplication (`*`), and Division (`/`).
* **Input Validation:** Robust error handling that prevents the program from crashing if non-numeric input is entered.
* **Safe Division:** specific checks to handle "divide by zero" errors gracefully.
* **Modular Design:** Calculation logic is separated into distinct functions for better readability and testability.
* **Interactive Menu:** A clean loop allowing users to perform multiple calculations, clear the screen, or exit easily.

## 🛠️ Technologies Used

* **Language:** Python 3.x
* **Modules:** `os` (for clearing the screen)

## 💻 How to Run

1.  **Clone the repository** (or download the files):
    ```bash
    git clone [https://github.com/your-username/simple-calculator.git](https://github.com/your-username/simple-calculator.git)
    ```
2.  **Navigate to the directory:**
    ```bash
    cd simple-calculator
    ```
3.  **Run the script:**
    ```bash
    python calculator.py
    ```

## 📸 Usage Example

```text
--- Simple Calculator ---
1. Add (+)
2. Subtract (-)
3. Multiply (*)
4. Divide (/)
5. Clear Screen
6. Exit

Enter choice (1/2/3/4/5/6): 1
Enter first number: 10
Enter second number: 5

✅ Result: 10.0 + 5.0 = 15.0
