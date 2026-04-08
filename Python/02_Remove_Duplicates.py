"""
DUPLICATE REMOVAL UTILITY
Removes duplicate characters from a string while preserving original order.
Includes multiple implementations with performance comparison.
"""

def remove_duplicates_simple(text):
    """
    Remove duplicate characters while preserving order (simple approach).
    
    Approach: Iterate through each character and add to result if not seen before.
    Time Complexity: O(n) where n is length of text
    Space Complexity: O(n) for the result string
    
    Args:
        text (str): Input string to remove duplicates from
        
    Returns:
        str: String with duplicates removed, order preserved
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected str, got {type(text).__name__}")
    
    result = ""
    for char in text:
        if char not in result:
            result += char
    
    return result


def remove_duplicates_set_tracking(text):
    """
    Remove duplicate characters using set for O(1) lookup (optimized approach).
    
    Approach: Use a set to track seen characters for constant-time lookup,
    much faster than checking "in result" string.
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        text (str): Input string to remove duplicates from
        
    Returns:
        str: String with duplicates removed, order preserved
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected str, got {type(text).__name__}")
    
    seen = set()
    result = ""
    
    for char in text:
        if char not in seen:
            seen.add(char)
            result += char
    
    return result


def remove_duplicates_dict_order(text):
    """
    Remove duplicate characters using dict (Python 3.7+ preserves insertion order).
    
    Approach: Use dict.fromkeys() which preserves order and removes duplicates.
    This is the most Pythonic and efficient approach.
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        text (str): Input string to remove duplicates from
        
    Returns:
        str: String with duplicates removed, order preserved
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected str, got {type(text).__name__}")
    
    return "".join(dict.fromkeys(text))


# ============================================================================
# TEST CASES
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("DUPLICATE REMOVAL UTILITY - TEST CASES")
    print("=" * 70)
    
    test_cases = [
        ("", ""),
        ("a", "a"),
        ("aa", "a"),
        ("programming", "progamin"),
        ("hello", "helo"),
        ("aabbcc", "abc"),
        ("mississippi", "misp"),
        ("AaBbCc", "AaBbCc"),  # Case-sensitive
        ("abcabc", "abc"),
        ("xyz", "xyz"),
        ("aaaaaa", "a"),
        ("the quick brown fox", "the quickbrownfx"),
    ]
    
    print("\nTesting all three implementations:")
    print("-" * 70)
    
    implementations = [
        ("Simple (O(n²))", remove_duplicates_simple),
        ("Set Tracking (O(n))", remove_duplicates_set_tracking),
        ("Dict Order (O(n))", remove_duplicates_dict_order),
    ]
    
    for impl_name, impl_func in implementations:
        print(f"\n{impl_name}:")
        print("-" * 70)
        
        all_pass = True
        for input_text, expected in test_cases:
            result = impl_func(input_text)
            status = "✓" if result == expected else "✗"
            
            if result != expected:
                all_pass = False
            
            # Display with sensible max length
            display_input = input_text[:20] + "..." if len(input_text) > 20 else input_text
            display_result = result[:20] + "..." if len(result) > 20 else result
            
            print(f"{status} Input: '{display_input}' → Output: '{display_result}'")
        
        print(f"Status: {'ALL TESTS PASSED' if all_pass else 'SOME TESTS FAILED'}")
    
    print("\n" + "=" * 70)
    print("PERFORMANCE COMPARISON")
    print("=" * 70)
    
    import timeit
    
    test_string = "programming" * 10  # Longer string for timing
    
    time_simple = timeit.timeit(
        f"remove_duplicates_simple('{test_string}')",
        setup="from __main__ import remove_duplicates_simple",
        number=10000
    )
    
    time_set = timeit.timeit(
        f"remove_duplicates_set_tracking('{test_string}')",
        setup="from __main__ import remove_duplicates_set_tracking",
        number=10000
    )
    
    time_dict = timeit.timeit(
        f"remove_duplicates_dict_order('{test_string}')",
        setup="from __main__ import remove_duplicates_dict_order",
        number=10000
    )
    
    print(f"\nTest string length: {len(test_string)} characters")
    print(f"Iterations: 10,000")
    print("-" * 70)
    print(f"Simple (O(n²)):      {time_simple:.4f} seconds")
    print(f"Set Tracking (O(n)): {time_set:.4f} seconds")
    print(f"Dict Order (O(n)):   {time_dict:.4f} seconds")
    print(f"\nFastest approach: {min([('Simple', time_simple), ('Set', time_set), ('Dict', time_dict)], key=lambda x: x[1])[0]}")
    
    print("\n" + "=" * 70)
    print("ERROR HANDLING TESTS")
    print("=" * 70)
    
    error_cases = [
        (123, "TypeError (int instead of str)"),
        (None, "TypeError (None instead of str)"),
        (12.34, "TypeError (float instead of str)"),
    ]
    
    for test_input, description in error_cases:
        try:
            remove_duplicates_dict_order(test_input)
            print(f"✗ {description}: No error raised!")
        except TypeError as e:
            print(f"✓ {description}: {type(e).__name__}")
    
    print("\n" + "=" * 70)
    print("REAL-WORLD EXAMPLES")
    print("=" * 70)
    print(f"Programming: {remove_duplicates_dict_order('programming')}")
    print(f"Mississippi: {remove_duplicates_dict_order('mississippi')}")
    print(f"Bookkeeping: {remove_duplicates_dict_order('bookkeeping')}")
