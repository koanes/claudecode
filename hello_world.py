#!/usr/bin/env python3
"""
A simple Hello World module.
"""

def get_greeting() -> str:
    """
    Returns a greeting message.
    
    Returns:
        str: A greeting message
    """
    return "Hello, World!"

if __name__ == "__main__":
    print(get_greeting())