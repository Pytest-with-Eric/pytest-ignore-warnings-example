import warnings
import pytest
from examples.my_module import old_function


def test_function():
    old_function()


def api_v1():
    # This function generates a warning with a specific message.
    warnings.warn("api v1, should use functions from v2", UserWarning)
    return 1

@pytest.mark.filterwarnings("ignore:api v1")
def test_one():
    # This test will ignore warnings with the message containing "api v1".
    assert api_v1() == 1



def test_myfunction_deprecated():
    with pytest.deprecated_call():
        old_function()