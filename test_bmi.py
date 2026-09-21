import unittest
from bmi_calculator import calculate_bmi, get_bmi_category, normalize_lang


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

    def test_zh_tw_categories(self):
        cat_under, _ = get_bmi_category(17.0, lang="zh-tw")
        self.assertEqual(cat_under, "體重過輕")

        cat_normal, _ = get_bmi_category(22.0, lang="zh-tw")
        self.assertEqual(cat_normal, "正常體重")

        cat_over, _ = get_bmi_category(26.0, lang="zh-tw")
        self.assertEqual(cat_over, "體重過重")

        cat_obese1, _ = get_bmi_category(31.0, lang="zh-tw")
        self.assertIn("第一級", cat_obese1)

        cat_obese2, _ = get_bmi_category(36.0, lang="zh-tw")
        self.assertIn("第二級", cat_obese2)

        cat_obese3, _ = get_bmi_category(42.0, lang="zh-tw")
        self.assertIn("第三級", cat_obese3)

    def test_japanese_categories(self):
        cat_under, _ = get_bmi_category(17.0, lang="ja")
        self.assertEqual(cat_under, "低体重 (痩せ型)")

        cat_normal, _ = get_bmi_category(22.0, lang="ja")
        self.assertEqual(cat_normal, "普通体重")

        cat_over, _ = get_bmi_category(26.0, lang="ja")
        self.assertEqual(cat_over, "前肥満 (過体重)")

        cat_obese1, _ = get_bmi_category(31.0, lang="ja")
        self.assertIn("肥満度1", cat_obese1)

        cat_obese2, _ = get_bmi_category(36.0, lang="ja")
        self.assertIn("肥満度2", cat_obese2)

        cat_obese3, _ = get_bmi_category(42.0, lang="ja")
        self.assertIn("肥満度3", cat_obese3)

    def test_normalize_lang(self):
        self.assertEqual(normalize_lang("en"), "en")
        self.assertEqual(normalize_lang("zh-tw"), "zh-tw")
        self.assertEqual(normalize_lang("zh_TW"), "zh-tw")
        self.assertEqual(normalize_lang("ja"), "ja")
        self.assertEqual(normalize_lang("jp"), "ja")
        self.assertEqual(normalize_lang("japanese"), "ja")
        self.assertEqual(normalize_lang("3"), "ja")
        self.assertEqual(normalize_lang("unknown"), "en")


if __name__ == "__main__":
    unittest.main()
