import unittest
import ModuleForTesting
class TestCalcModule(unittest.TestCase):

    def test_add(self):
        result = ModuleForTesting.add(10, 5)
        self.assertEqual(result, 15)

unittest.main()