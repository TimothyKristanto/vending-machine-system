import unittest
from vending_machine import count_changes

class VendingMachineTest(unittest.TestCase):
    def test_count_changes(self):
        self.assertEqual(count_changes(10000, 100000), {
            50000: 1,
            20000: 2
        })

        # self.assertEqual(count_changes(1000, 50000), {
        #     20000: 2,
        #     5000: 1,
        #     2000: 1,
        #     1000: 2
        # })

if __name__ == "__main__":
    unittest.main()