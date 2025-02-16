import unittest
from tests.login_tests import LoginTest

# Ladujemy testy do Test Suity

login_tests = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

# lista testow do uruchomienia
tests_for_run = [
    login_tests,
    # ...
    # ...
]

# Laczymy testy w Test Suite
test_suite = unittest.TestSuite(tests_for_run)

# odpalanie testow
unittest.TextTestRunner().run(test_suite)