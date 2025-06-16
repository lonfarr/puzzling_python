"""
The following code will behave differently whether if an optimization flag (`-O` or `-OO`)
is invoked when Python is launched.

Example invocations:
python3 ./dictionary_pop.py
python3 -O ./dictionary_pop.py
"""

import pprint


def main() -> None:
    # Log if the debug flag is set or not
    print(f"The `__debug__` flag is currently set to: {__debug__}")

    # This is an input message
    input_message: dict[str, str] = {
        "sender": "Descartes",
        "message": "I think, therefore I am",
        "valid": "true",
    }

    # Print out the message before the assert; use pprint
    # so that the dict will look nice and sorted on output
    print("input_message before `assert` is called:")
    pprint.pprint(input_message)

    # Run the assert, which will be ignored if `__debug__` if False
    assert input_message.pop("valid") == "true"

    # Print out the message after the assert; use pprint
    # so that the dict will look nice and sorted on output
    # If Python was run not run in an optimized mode, `valid`
    # will be removed, but if optimized it will still be present
    print("input_message after `assert` is called:")
    pprint.pprint(input_message)


if __name__ == "__main__":
    main()
