"""
This file simply prints out some test cases, showing some
interesting results if `is` and `in` are thought of as
having an order of operations.

This can be run with `python3 ./examples.py`
"""


def main() -> None:
    print(
        f"""
When evaluating an expression like `value_1 is value_2 in [list_values]`
my initial inclination is that there must be an order of operations.

Creating a test case of `False is False in [False, True]` would give me
two different results based on if `is` or `in` is evaluated first as
shown with the following:
{(False is False) in [False, True]=}
{False is (False in [False, True])=}

Comparing this to the expression without parenthesis yields:
{False is False in [False, True]=}

This indicates that `is` must be evaluated first.

But another example of `False is True in [False, True]` yields
contradictory results showing `in` has precedence:
{False is True in [False, True]=}
{(False is True) in [False, True]=}
{False is (True in [False, True])=}

The reality is that these are chained together, so
`value_1 is value_2 in [list_values]` actually tests
`value_1 is value_2 and value_2 in [list_values]`

Therefore, the above statements now make sense if broken apart:
{False is False and False in [False, True]=}
{False is True and True in [False, True]=}
"""
    )


if __name__ == "__main__":
    main()
