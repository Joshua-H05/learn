import time
from mock import patch


# scenario 1 - I built this, I test this


def doit_slowly(something):
    if something == "1":
        time.sleep(60)
        return True
    return False


# scenario 2 - I built this, it uses doit_slowly

def do_something(number):
    return doit_slowly(number)


"""class TestDoSomething(unittest.TestCase):
    def test_scenario_1_true(self):
        result = doit_slowly(1)
        self.assertEqual(result, True)

    def test_scenario_1_false(self):
        result = doit_slowly(2)
        self.assertEqual(result, False)

    def test_scenario_2_true(self):
        doit_slowly = Mock()
        doit_slowly.return_value = True
        result = do_something(1)
        self.assertEqual(result, True)

    def test_scenario_2_false(self):
        doit_slowly = Mock()
        doit_slowly.return_value = False
        result = do_something(2)
        self.assertEqual(result, False)"""
