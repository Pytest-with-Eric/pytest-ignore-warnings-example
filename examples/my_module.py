import warnings


def old_function():
    warnings.warn(
        "old_function() is deprecated; use new_function() instead.",
        DeprecationWarning,
        stacklevel=2,
    )


def new_function():
    print("This is the new function.")


# Example usage
old_function()
