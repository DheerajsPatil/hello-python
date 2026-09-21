import unittest
from bmi_calculator import calculate_bmi, get_bmi_category


class TestBMICalculator(unittest.TestCase):
    def test_normal_bmi(self):
        # 70 kg, 1.75 m -> 22.86
        self.assertEqual(calculate_bmi(70, 1.75), 22.86)
        category, _ = get_bmi_category(22.86)
        self.assertEqual(category, "Normal weight")

    def test_underweight(self):
        category, _ = get_bmi_category(17.5)
        self.assertEqual(category, "Underweight")

    def test_overweight(self):
        category, _ = get_bmi_category(27.3)
        self.assertEqual(category, "Overweight")

    def test_obesity_classes(self):
        cat1, _ = get_bmi_category(32.0)
        self.assertIn("Class I", cat1)

        cat2, _ = get_bmi_category(37.0)
        self.assertIn("Class II", cat2)

        cat3, _ = get_bmi_category(42.0)
        self.assertIn("Class III", cat3)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            calculate_bmi(-50, 1.75)
        with self.assertRaises(ValueError):
            calculate_bmi(70, 0)


if __name__ == "__main__":
    unittest.main()
