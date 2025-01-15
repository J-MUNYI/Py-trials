# A simple Python code demonstrating basic concepts

# 1. Variables
name = "Python Learner"
age = 25

# 2. Function
def greet_user(name):
    return f"Hello, {name}! Welcome to Python learning."

# 3. If-Else Statement
def check_age(age):
    if age < 18:
        return "You are a minor."
    else:
        return "You are an adult."

# 4. Loops
def print_numbers():
    print("Printing numbers from 1 to 5:")
    for i in range(1, 6):
        print(i)

# 5. Main Execution
if __name__ == "__main__":
    # Display greeting message
    print(greet_user(name))

    # Check user's age
    print(check_age(age))

    # Print numbers
    print_numbers()

    # Demonstrate a simple calculation
    number1 = 10
    number2 = 5
    sum_result = number1 + number2
    print(f"The sum of {number1} and {number2} is: {sum_result}")
