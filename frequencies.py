"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    items = [str(item) for item in items]
    frequencies = {item: items.count(item) for item in items}
    print(frequencies)
    return frequencies
