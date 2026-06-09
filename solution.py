def isAnagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


EXAMPLE_TEST_CASES = [
    {
        "name": "example_1",
        "input": ["anagram", "nagaram"],
        "expected": True,
        "description": "Main example from README - both strings are anagrams",
    },
    {
        "name": "example_2",
        "input": ["rat", "car"],
        "expected": False,
        "description": "Main example from README - not anagrams",
    },
    {
        "name": "edge_case_empty_strings",
        "input": ["", ""],
        "expected": True,
        "description": "Both empty strings are anagrams",
    },
    {
        "name": "edge_case_different_lengths",
        "input": ["abc", "ab"],
        "expected": False,
        "description": "Different lengths cannot be anagrams",
    },
    {
        "name": "edge_case_single_char_same",
        "input": ["a", "a"],
        "expected": True,
        "description": "Single identical characters",
    },
    {
        "name": "edge_case_single_char_different",
        "input": ["a", "b"],
        "expected": False,
        "description": "Single different characters",
    },
    {
        "name": "case_same_string",
        "input": ["listen", "listen"],
        "expected": True,
        "description": "Identical strings are anagrams",
    },
]
