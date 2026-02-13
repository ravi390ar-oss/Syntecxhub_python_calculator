import os

# --- 1. Helper Functions (MUST be at the top) ---

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return None  # Handle divide by zero safely
    return x / y

def clear_screen():
    # Clears terminal: 'cls' for Windows, 'clear' for Mac/Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def get_valid_number(prompt):
    while True:
        try:
            user_input = input(prompt)
            return float(user_input)
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

# --- 2. Main Application Loop ---

def calculator_app():
    while True:
        print("\n--- Simple Calculator ---")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Clear Screen")
        print("6. Exit")
        
        choice = input("Enter choice (1/2/3/4/5/6): ")

        # Exit option
        if choice == '6':
            print("Exiting calculator. Goodbye!")
            break
        
        # Clear option
        if choice == '5':
            clear_screen()
            continue

        # Validate operator selection
        if choice not in ('1', '2', '3', '4'):
            print("❌ Invalid choice. Please select 1-6.")
            continue

        # Get numbers using our helper function
        num1 = get_valid_number("Enter first number: ")
        num2 = get_valid_number("Enter second number: ")

        result = 0
        operation_symbol = ""

        # Perform calculation
        if choice == '1':
            result = add(num1, num2)
            operation_symbol = "+"
        elif choice == '2':
            result = subtract(num1, num2)
            operation_symbol = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            operation_symbol = "*"
        elif choice == '4':
            result = divide(num1, num2)
            operation_symbol = "/"
            
            if result is None:
                print("❌ Error: Cannot divide by zero!")
                continue

        # Show result
        print(f"\n✅ Result: {num1} {operation_symbol} {num2} = {result}")

# --- 3. Run the Program ---
if __name__ == "__main__":
    calculator_app()