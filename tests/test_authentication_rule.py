# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class AutheticationRuleTestCase(ModuleTestCase):
    'Test Authentication Rule module'
    module = 'authentication_rule'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(AutheticationRuleTestCase))
    return suite
