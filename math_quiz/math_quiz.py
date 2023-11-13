import random


def generate_random_integer(min_limit, max_limit):
    """
    Returns a random integer within the specified maximum and minimum.
    Args:
        min_limit (int): The minimum limit of the range.
        max_limit (int): The maximum limit of the range.
    
    Returns:
        int: A random integer within the specified limits.
    """
    try:
        # Ensuring valid input limits
        if not isinstance(min_limit, int) or not isinstance(max_limit, int):
            raise ValueError("Both lower limit and upper limit must be integers.")

        # Ensuring lower limit less than upper limit
        if min_limit > max_limit:
            raise ValueError("Minimum limit should be less than or equal to the maximum limit.")

        # Generate and return a random integer
        return random.randint(min_limit, max_limit)
    
    except ValueError as input_error:
        # Display the error message
        print(f"Error: {input_error}")
        return None


def random_operation_selector():
    """
    Selects a random math operation from the given operations ('+', '-', '*').

    Args:
        None
    Returns:
        str: A random math operation from the set {'+', '-', '*'}
    """
    # Select and return a math operation at random (+,- or *)
    operator = random.choice(['+', '-', '*'])
    return operator


def math_operation(num1, num2, operator):
    """
    Performs a mathematical operation (+, -, *) on two numbers.

    Args:
        num1 (int): The first operand.
        num2 (int): The second operand.
        operator (str): The operator to apply on the operands (+, -, *).
    Returns:
        tuple: A tuple containing the expression string and the result of the operation.
    """
    try:
        # Ensure the input operands are valid numbers
        if not isinstance(num1, int) or not isinstance(num2, int):
            raise ValueError("Both num1 and num2 must be integer values.")

        # Perform the specified mathematical operation
        if operator == '+': 
            answer = num1 + num2
        elif operator == '-': 
            answer = num1 - num2
        elif operator == '*': 
            answer = num1 * num2
        else:
            raise ValueError("Invalid operator. Select from the set of operators {'+', '-', '*'}.")
        
        # Generate the expression string
        problem = f"{num1} {operator} {num2}"

        # Return the expression string and answer of the math operation
        return problem, answer
    
    except ValueError as input_error:
        print(f"Error: {input_error}")
        return None

def math_quiz(total_questions=3):
    """
    Performs a Math Quiz Game.

    Args:
        total_questions (int): The number of questions in the math_quiz game.
                                (defaults to 3)
    Returns:
        int: The final score in the math_quiz game.
    """
    try:
        # Ensuring valid total number of questions
        if not isinstance(total_questions, int):
            raise ValueError("The number of questions must be integer")
    except ValueError as input_error:
        # Display the error message
        print(f"Error: {input_error}")
        return None
    
    score = 0

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10); 
        num2 = generate_random_integer(1, 5); # Rounded 5.5 to 5 to ensure integer result 
        operator = random_operation_selector()
        problem, answer = math_operation(num1, num2, operator)

        # Print the question and get user's answer as integer
        print(f"\nQuestion: {problem}")
        user_answer = int(input("Your answer: "))
        try:
            if not isinstance(user_answer, int):
                raise ValueError("The solution must be integer")  
        except ValueError as input_error:
            # Display the error message
            print(f"Error: {input_error}")
            return None
        # Increment score by 1 if user gives correct answer
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        
        # Print the correct answer if user's answer is incorrect 
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    # Display the final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")
    return score

if __name__ == "__main__":
    math_quiz()