from collections import Counter


def isAnagram(s, t):
    if not isinstance(s, str) or not isinstance(t, str):
        raise TypeError("Both function inputs should be the type of string")
    elif len(s) != len(t):
        return False
    else:
        sCount = Counter(s)
        tCount = Counter(t)
        isA = True
        for count in sCount:
            if sCount[count] != tCount.get(count):
                isA = False
                break

        return isA


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
