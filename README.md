# Valid Anagram

Given two strings, s and t, write a function isAnagram(s, t) that returns true if t is an anagram of s, and false otherwise.

**Definition:** An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Input/Output Examples

### Example 1:

**Input:** s = "anagram", t = "nagaram"

**Output:** true

**Explanation:** Both strings contain the characters: a (3 times), n, g, r, and m.

### Example 2:

**Input:** s = "rat", t = "car"

**Output:** false

**Explanation:** The characters in t are not the same as in s. 'r' and 'a' appear in both, but s has a 't' while t has a 'c'.

## Constraints & Assumptions

For the basic exercise, you may assume the following to simplify the problem:

- The strings contain only lowercase English letters (a-z).
- The strings can be of varying lengths.
- The maximum length of the strings is not a primary concern for the algorithm's design, but your solution should handle reasonably large inputs efficiently.

## Function Description

Complete the function `isAnagram(s, t)` in the editor with the following parameters:

**Parameters:**

- `string s`: the first string
- `string t`: the second string

**Returns:**

- `boolean`: true if t is an anagram of s, false otherwise

## Notes

Your solution should aim for an optimal balance of time and space complexity.
