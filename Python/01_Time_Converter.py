"""
TIME CONVERTER UTILITY
Converts minutes into human-readable "X hours Y minutes" format
with validation and edge case handling.
"""

def convert_minutes(minutes):
    """
    Convert minutes to 'X hrs Y minutes' format.
    
    Args:
        minutes (int): Total number of minutes to convert
        
    Returns:
        str: Formatted string like "2 hrs 10 minutes"
        
    Raises:
        TypeError: If minutes is not an integer
        ValueError: If minutes is negative
    """
    # Input validation
    if not isinstance(minutes, int):
        raise TypeError(f"Expected int, got {type(minutes).__name__}")
    
    if minutes < 0:
        raise ValueError("Minutes cannot be negative")
    
    # Handle edge case: 0 minutes
    if minutes == 0:
        return "0 minutes"
    
    # Calculate hours and remaining minutes
    hours = minutes // 60
    remaining_minutes = minutes % 60
    
    # Format output
    if hours == 0:
        return f"{remaining_minutes} minutes"
    elif remaining_minutes == 0:
        return f"{hours} hrs" if hours > 1 else f"{hours} hr"
    else:
        return f"{hours} hrs {remaining_minutes} minutes"


# ============================================================================
# TEST CASES
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("TIME CONVERTER - TEST CASES")
    print("=" * 60)
    
    test_cases = [
        (0, "0 minutes"),
        (45, "45 minutes"),
        (60, "1 hr"),
        (61, "1 hrs 1 minutes"),
        (90, "1 hrs 30 minutes"),
        (130, "2 hrs 10 minutes"),
        (180, "3 hrs"),
        (245, "4 hrs 5 minutes"),
        (1440, "24 hrs"),
    ]
    
    print("\nBasic Test Cases:")
    for minutes, expected in test_cases:
        result = convert_minutes(minutes)
        status = "✓" if result == expected else "✗"
        print(f"{status} convert_minutes({minutes:4d}) = '{result}'")
    
    print("\n" + "=" * 60)
    print("Error Handling Tests:")
    print("=" * 60)
    
    # Test error cases
    error_cases = [
        ("130", "TypeError (string instead of int)"),
        (-50, "ValueError (negative number)"),
        (3.5, "TypeError (float instead of int)"),
    ]
    
    for test_input, description in error_cases:
        try:
            convert_minutes(test_input)
            print(f"✗ {description}: No error raised!")
        except (TypeError, ValueError) as e:
            print(f"✓ {description}: {type(e).__name__} - {e}")
    
    print("\n" + "=" * 60)
    print("Real-world Examples:")
    print("=" * 60)
    print(f"Movie duration (130 min): {convert_minutes(130)}")
    print(f"Meeting time (45 min):    {convert_minutes(45)}")
    print(f"Travel time (195 min):    {convert_minutes(195)}")
