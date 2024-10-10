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
    try:
        problem, expected_answer = equation.split('=')
        expected_answer = int(expected_answer.strip())
        
        result = eval(problem.strip())
        
        if result == expected_answer:
            return "Correct!"
        else:
            return "Incorrect"
        
    except Exception as e:
        return f"Error: {str(e)}"