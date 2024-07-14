def safe_divide(numerator, denominator):
    try:
        
        num = float(numerator)
        denom = float(denominator)
        
        
        result = num / denom
        return f"The result of the division is {result}"
    
    except ValueError:
        return "Error: Please enter numeric values only."
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

if __name__ == "__main__":
    # Simple test cases for direct script execution (optional)
    print(safe_divide("10", "2"))  # Should return "The result of the division is 5.0"
    print(safe_divide("10", "0"))  # Should return "Error: Cannot divide by zero."
    print(safe_divide("ten", "2"))  # Should return "Error: Please enter numeric values only."
