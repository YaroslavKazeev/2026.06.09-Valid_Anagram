import pytest

from solution import EXAMPLE_TEST_CASES, isAnagram


@pytest.mark.parametrize("case", EXAMPLE_TEST_CASES, ids=lambda case: case["name"])
def test_isAnagram(case):
    s, t = case["input"]
    result = isAnagram(s, t)
    assert (
        result == case["expected"]
    ), f'{case["name"]} failed: expected {case["expected"]}, got {result}'


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
