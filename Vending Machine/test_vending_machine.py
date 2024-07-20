import unittest
from vending_machine import count_changes

class VendingMachineTest(unittest.TestCase):
    def test_count_changes(self):
        self.assertEqual(count_changes(5000, 50000), {
            20000: 2,
            5000: 1
        })

if __name__ == "__main__":
    unittest.main()