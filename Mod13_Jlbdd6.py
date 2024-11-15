import unittest
from datetime import datetime
import re



class TestStockVisualizerInputs(unittest.TestCase):
    def test_symbol(self):
        self.assertTrue(re.match(r"^[A-Z]{1,7}$", "IBM"), "Valid symbol failed")
        self.assertFalse(re.match(r"^[A-Z]{1,7}$", "IBM12"), "Invalid symbol passed")

    def test_chart_type(self):
        self.assertIn("1", ["1", "2"], "Valid chart type '1' failed")
        self.assertIn("2", ["1", "2"], "Valid chart type '2' failed")
        self.assertNotIn("3", ["1", "2"], "Invalid chart type passed")

    def test_time_series(self):
        self.assertIn("1", ["1", "2", "3", "4"], "Valid time series '1' failed")
        self.assertNotIn("5", ["1", "2", "3", "4"], "Invalid time series passed")

    def test_start_date_format(self):
        start_date = "2023-01-01"
        try:
            datetime.strptime(start_date, "%Y-%m-%d")
            valid = True
        except ValueError:
            valid = False
        self.assertTrue(valid, "Valid date format failed")

    def test_end_date_format(self):
        end_date = "2023-12-31"
        try:
            datetime.strptime(end_date, "%Y-%m-%d")
            valid = True
        except ValueError:
            valid = False
        self.assertTrue(valid, "Valid date format failed")

if __name__ == "__main__":
    unittest.main()
