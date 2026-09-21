"""Body Mass Index (BMI) Calculator.

Calculates BMI and categorizes it according to World Health Organization (WHO) standards.
Supports both Metric (kg, cm/m) and Imperial (lbs, feet/inches) units.
Multilingual support: English, Traditional Chinese (zh-TW), and Japanese (ja).
"""

import sys
from typing import Dict, Tuple, Any

# Ensure UTF-8 output encoding across platforms (especially Windows PowerShell/cmd)
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


TRANSLATIONS: Dict[str, Dict[str, Any]] = {
    "en": {
        "title": "BMI CALCULATOR",
        "results_title": "RESULTS",
        "lang_name": "English",
        "unit_header": "Choose your preferred unit system:",
        "unit_metric": "  1. Metric (kilograms, meters or centimeters)",
        "unit_imperial": "  2. Imperial (pounds, feet and inches)",
        "unit_choice_prompt": "\nEnter choice (1 or 2): ",
        "invalid_choice": "Invalid choice. Please enter 1 or 2.",
        "prompt_weight_kg": "\nEnter your weight in kilograms (kg): ",
        "prompt_height_metric": "Enter your height in centimeters (cm) or meters (m): ",
        "interpreted_cm": "Interpreted {input_val} as centimeters ({height_m:.2f} m).",
        "prompt_weight_lbs": "\nEnter your weight in pounds (lbs): ",
        "prompt_height_header": "\nEnter height:",
        "prompt_feet": "  Feet: ",
        "prompt_inches": "  Inches (press Enter for 0): ",
        "err_positive": "Error: Value must be greater than zero. Please try again.",
        "err_invalid_num": "Error: Invalid number. Please enter a numerical value.",
        "err_weight_positive": "Weight must be greater than zero.",
        "err_height_positive": "Height must be greater than zero.",
        "label_weight": "Weight (kg)  ",
        "label_height": "Height (m)   ",
        "label_bmi": "Your BMI     ",
        "label_category": "Category     ",
        "label_insight": "Insight      ",
        "categories": {
            "underweight": ("Underweight", "Possible nutritional deficiency or other health issues."),
            "normal": ("Normal weight", "Healthy weight range for most adults."),
            "overweight": ("Overweight", "Increased risk of cardiovascular and metabolic issues."),
            "obese_1": ("Obesity Class I (Moderate)", "Moderate risk of obesity-related health conditions."),
            "obese_2": ("Obesity Class II (Severe)", "Severe risk of obesity-related health conditions."),
            "obese_3": ("Obesity Class III (Very severe / Morbid)", "Very high risk of obesity-related complications."),
        },
    },
    "zh-tw": {
        "title": "BMI 身體質量指數計算機",
        "results_title": "計算結果",
        "lang_name": "繁體中文",
        "unit_header": "請選擇偏好的單位系統：",
        "unit_metric": "  1. 公制 (公斤, 公尺或公分)",
        "unit_imperial": "  2. 英制 (磅, 呎與吋)",
        "unit_choice_prompt": "\n請輸入選項 (1 或 2): ",
        "invalid_choice": "無效選項，請輸入 1 或 2。",
        "prompt_weight_kg": "\n請輸入您的體重（公斤 kg）：",
        "prompt_height_metric": "請輸入您的身高（公分 cm 或公尺 m）：",
        "interpreted_cm": "已將 {input_val} 判斷為公分（{height_m:.2f} 公尺）。",
        "prompt_weight_lbs": "\n請輸入您的體重（磅 lbs）：",
        "prompt_height_header": "\n請輸入身高：",
        "prompt_feet": "  英呎 (Feet): ",
        "prompt_inches": "  英吋 (Inches，直接按 Enter 為 0): ",
        "err_positive": "錯誤：數值必須大於零，請重新輸入。",
        "err_invalid_num": "錯誤：無效數值，請輸入數字。",
        "err_weight_positive": "體重必須大於零。",
        "err_height_positive": "身高必須大於零。",
        "label_weight": "體重 (kg)    ",
        "label_height": "身高 (m)     ",
        "label_bmi": "您的 BMI     ",
        "label_category": "體重分類     ",
        "label_insight": "健康建議     ",
        "categories": {
            "underweight": ("體重過輕", "可能存在營養不良或其他健康問題。"),
            "normal": ("正常體重", "大多數成年人的健康體重範圍。"),
            "overweight": ("體重過重", "心血管與代謝疾病風險增加。"),
            "obese_1": ("輕度肥胖（第一級）", "與肥胖相關健康問題的中度風險。"),
            "obese_2": ("中度肥胖（第二級）", "與肥胖相關健康問題的重度風險。"),
            "obese_3": ("重度肥胖（第三級）", "與肥胖相關併發症的極高風險。"),
        },
    },
    "ja": {
        "title": "BMI 計算機 (肥満度指数)",
        "results_title": "計算結果",
        "lang_name": "日本語",
        "unit_header": "単位系を選択してください：",
        "unit_metric": "  1. メートル法 (キログラム、メートルまたはセンチメートル)",
        "unit_imperial": "  2. ヤード・ポンド法 (ポンド、フィートとインチ)",
        "unit_choice_prompt": "\n選択肢を入力 (1 または 2): ",
        "invalid_choice": "無効な選択です。1 または 2 を入力してください。",
        "prompt_weight_kg": "\n体重をキログラム (kg) で入力してください: ",
        "prompt_height_metric": "身長をセンチメートル (cm) またはメートル (m) で入力してください: ",
        "interpreted_cm": "{input_val} をセンチメートル ({height_m:.2f} m) として解釈しました。",
        "prompt_weight_lbs": "\n体重をポンド (lbs) で入力してください: ",
        "prompt_height_header": "\n身長を入力してください:",
        "prompt_feet": "  フィート (Feet): ",
        "prompt_inches": "  インチ (Inches, そのまま Enter で 0): ",
        "err_positive": "エラー: 0 より大きい数値を入力してください。",
        "err_invalid_num": "エラー: 有効な数値を入力してください。",
        "err_weight_positive": "体重は 0 より大きい必要があります。",
        "err_height_positive": "身長は 0 より大きい必要があります。",
        "label_weight": "体重 (kg)    ",
        "label_height": "身長 (m)     ",
        "label_bmi": "あなたの BMI ",
        "label_category": "判定区分     ",
        "label_insight": "アドバイス   ",
        "categories": {
            "underweight": ("低体重 (痩せ型)", "栄養不良などの健康リスクの可能性があります。"),
            "normal": ("普通体重", "成人の適正体重範囲です。"),
            "overweight": ("前肥満 (過体重)", "心血管疾患や生活習慣病のリスクが高まります。"),
            "obese_1": ("肥満度1 (軽度肥満)", "肥満に関連する健康障害のリスクが高まります。"),
            "obese_2": ("肥満度2 (中等度肥満)", "肥満に関連する重度な健康障害のリスクがあります。"),
            "obese_3": ("肥満度3 (高度肥満)", "肥満に関連する合併症のリスクが非常に高い状態です。"),
        },
    },
}


def normalize_lang(lang: str) -> str:
    """Normalize language code to 'en', 'zh-tw', or 'ja'."""
    cleaned = (lang or "").strip().lower().replace("_", "-")
    if cleaned in ("zh-tw", "zh", "tw", "zhtw", "chinese", "traditional-chinese", "2"):
        return "zh-tw"
    elif cleaned in ("ja", "jp", "japanese", "jpn", "nihongo", "3"):
        return "ja"
    return "en"


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI given weight in kilograms and height in meters.

    Args:
        weight_kg: Weight in kilograms. Must be > 0.
        height_m: Height in meters. Must be > 0.

    Returns:
        The calculated BMI value rounded to 2 decimal places.

    Raises:
        ValueError: If weight or height is non-positive.
    """
    if weight_kg <= 0:
        raise ValueError("Weight must be greater than zero.")
    if height_m <= 0:
        raise ValueError("Height must be greater than zero.")

    return round(weight_kg / (height_m ** 2), 2)


def get_bmi_category(bmi: float, lang: str = "en") -> Tuple[str, str]:
    """Return the WHO category and a short health description for a given BMI.

    Args:
        bmi: Body Mass Index value.
        lang: Language code ('en', 'zh-tw', or 'ja'). Defaults to 'en'.

    Returns:
        Tuple of (Category Name, Health Insight).
    """
    lang_key = normalize_lang(lang)
    categories = TRANSLATIONS[lang_key]["categories"]

    if bmi < 18.5:
        return categories["underweight"]
    elif 18.5 <= bmi < 25.0:
        return categories["normal"]
    elif 25.0 <= bmi < 30.0:
        return categories["overweight"]
    elif 30.0 <= bmi < 35.0:
        return categories["obese_1"]
    elif 35.0 <= bmi < 40.0:
        return categories["obese_2"]
    else:
        return categories["obese_3"]


def get_positive_float(prompt: str, err_positive: str = "Error: Value must be greater than zero. Please try again.", err_invalid: str = "Error: Invalid number. Please enter a numerical value.") -> float:
    """Prompt the user until a valid positive float is entered."""
    while True:
        try:
            val = float(input(prompt).strip())
            if val <= 0:
                print(err_positive)
                continue
            return val
        except ValueError:
            print(err_invalid)


def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description="Calculate Body Mass Index (BMI) / 計算身體質量指數 / BMI計算。")
    parser.add_argument("-w", "--weight", type=float, help="Weight in kilograms (or lbs if --imperial is set)")
    parser.add_argument("-H", "--height", type=float, help="Height in meters/cm (or inches if --imperial is set)")
    parser.add_argument("--imperial", action="store_true", help="Interpret inputs as imperial units (lbs, inches)")
    parser.add_argument("-l", "--lang", choices=["en", "zh-tw", "zh_TW", "ja", "jp"], default=None, help="Language / 語言 / 言語: en (English), zh-tw (繁體中文), ja (日本語)")
    return parser.parse_args()


def select_language() -> str:
    """Prompt user to choose language interactively."""
    print("=" * 45)
    print(" Select Language / 選擇語言 / 言語選択:")
    print("   1. English (Default)")
    print("   2. 繁體中文 (zh-TW)")
    print("   3. 日本語 (Japanese)")
    print("=" * 45)
    choice = input("Enter choice / 請選擇 / 選択 (1-3, Enter for 1): ").strip()
    if choice == "2":
        return "zh-tw"
    elif choice == "3":
        return "ja"
    return "en"


def main() -> None:
    args = parse_args()

    # Determine language
    if args.lang:
        lang = normalize_lang(args.lang)
    elif args.weight is not None and args.height is not None:
        # Non-interactive CLI with inputs supplied defaults to English
        lang = "en"
    else:
        # Interactive mode language prompt
        lang = select_language()

    t = TRANSLATIONS[lang]

    if args.weight is not None and args.height is not None:
        # Non-interactive CLI mode
        if args.imperial:
            weight_kg = args.weight * 0.45359237
            height_m = args.height * 0.0254
        else:
            weight_kg = args.weight
            height_m = args.height / 100.0 if args.height > 3.0 else args.height
    else:
        # Interactive mode
        print("\n" + "=" * 45)
        print(f"             {t['title']}")
        print("=" * 45)
        print(t["unit_header"])
        print(t["unit_metric"])
        print(t["unit_imperial"])

        while True:
            choice = input(t["unit_choice_prompt"]).strip()
            if choice in ("1", "2"):
                break
            print(t["invalid_choice"])

        if choice == "1":
            # Metric
            weight_kg = get_positive_float(t["prompt_weight_kg"], t["err_positive"], t["err_invalid_num"])
            height_input = get_positive_float(t["prompt_height_metric"], t["err_positive"], t["err_invalid_num"])

            # If input is greater than 3, assume centimeters and convert to meters
            if height_input > 3.0:
                height_m = height_input / 100.0
                print(t["interpreted_cm"].format(input_val=height_input, height_m=height_m))
            else:
                height_m = height_input
        else:
            # Imperial
            weight_lbs = get_positive_float(t["prompt_weight_lbs"], t["err_positive"], t["err_invalid_num"])
            print(t["prompt_height_header"])
            feet = get_positive_float(t["prompt_feet"], t["err_positive"], t["err_invalid_num"])
            inches_str = input(t["prompt_inches"]).strip() or "0"
            try:
                inches = float(inches_str)
                if inches < 0:
                    inches = 0.0
            except ValueError:
                inches = 0.0

            total_inches = (feet * 12.0) + inches
            weight_kg = weight_lbs * 0.45359237
            height_m = total_inches * 0.0254

    try:
        bmi = calculate_bmi(weight_kg, height_m)
    except ValueError as e:
        print(f"Error: {e}")
        return

    category, description = get_bmi_category(bmi, lang=lang)

    print("\n" + "=" * 45)
    print(f"                 {t['results_title']}")
    print("=" * 45)
    print(f"{t['label_weight']}: {weight_kg:.2f} kg")
    print(f"{t['label_height']}: {height_m:.2f} m")
    print(f"{t['label_bmi']}: {bmi}")
    print(f"{t['label_category']}: {category}")
    print(f"{t['label_insight']}: {description}")
    print("=" * 45)


if __name__ == "__main__":
    main()
