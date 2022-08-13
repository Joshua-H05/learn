import unittest
from mock import patch
import time
import terrible
# Rule: If I wrote it myself, I mock it, if someone else wrote it, I should patch it


def test_scenario_1_true():
    result = terrible.doit_slowly("1")
    assert result is True


def test_scenario_1_false():
    result = terrible.doit_slowly("2")
    assert result is False


def test_scenario_2_true():
    with patch("terrible.doit_slowly") as doit_slowly_mock:
        # With is a context manager--> allocates resources--> Guarantee that the patch will "die" and things will return
        # to normal
        # Key: Patch overrides something and guarantees that it will revert everything at the end
        doit_slowly_mock.return_value = True
        result = terrible.do_something(1)
    assert result is True


def test_scenario_2_false():
    with patch("terrible.doit_slowly") as doit_slowly_mock:
        doit_slowly_mock.return_value = False
        result = terrible.do_something(2)
    assert result is False
