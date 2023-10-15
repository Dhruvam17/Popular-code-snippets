import math

def main():
    print("Welcome to the Python Calculator!")
    print("Available operations: +, -, *, /, ^ (for power), sqrt (for square root)")
    print("Enter 'exit' to quit.")

    while True:
        expression = input("Enter a mathematical expression: ")
        
        if expression.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            result = evaluate_expression(expression)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

def evaluate_expression(expression):
    # Replace the caret (^) with '**' to handle power operations
    expression = expression.replace('^', '**')
    
    # Check for 'sqrt' and replace it with 'math.sqrt'
    if 'sqrt' in expression:
        expression = expression.replace('sqrt', 'math.sqrt')

    # Use eval to evaluate the expression
    return eval(expression)

if __name__ == "__main__":
    main()
