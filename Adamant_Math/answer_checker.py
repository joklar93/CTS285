import re

def validate_equation(equation: str) -> bool:
    pattern = r'^\d{1,2}\s*[\+\-\*/]\s*\d{1,2}\s*=\s*\d{1,3}$'
    if not re.match(pattern, equation):
        return False
    
    left, right = equation.split('=')
    try:
        result = eval(left.strip())
        return result == int(right.strip())
    except:
        return False

def evaluate_equation(equation: str) -> str:
    if not validate_equation(equation):
        return "Error: Not acceptable"
    try:
        problem, expected_answer = equation.split('=')
        expected_answer = int(expected_answer.strip())
        
        result = eval(problem.strip())
        
        if result == expected_answer:
            return "Correct!"
        else:
            return "Incorrect"
        
    except Exception as e:
        return f"Error: Calculating error. Not acceptable"

#Testing    
# if __name__ == "__main__":
#     test_equations = [
#         "2 + 2 = 4",
#         "10 - 5 = 5",
#         "3 * 4 = 12",
#         "8 / 2 = 4",
#         "5 + 5 = 11",
#         "2 + 2 = 5",
#         "abc = 123",
#         "1 + 1 = ",
#         "99 + 99 = 198"
#     ]

#     for eq in test_equations:
#         print(f"Equation: {eq}")
#         print(f"Valid: {validate_equation(eq)}")
#         print(f"Evaluation: {evaluate_equation(eq)}")
#         print()