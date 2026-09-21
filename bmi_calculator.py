"""Body Mass Index (BMI) Calculator.

Calculates BMI and categorizes it according to World Health Organization (WHO) standards.
Supports both Metric (kg, cm/m) and Imperial (lbs, feet/inches) units.
"""

from typing import Tuple


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


def get_bmi_category(bmi: float) -> Tuple[str, str]:
    """Return the WHO category and a short health description for a given BMI.

    Args:
        bmi: Body Mass Index value.

    Returns:
        Tuple of (Category Name, Health Insight).
    """
    if bmi < 18.5:
        return "Underweight", "Possible nutritional deficiency or other health issues."
    elif 18.5 <= bmi < 25.0:
        return "Normal weight", "Healthy weight range for most adults."
    elif 25.0 <= bmi < 30.0:
        return "Overweight", "Increased risk of cardiovascular and metabolic issues."
    elif 30.0 <= bmi < 35.0:
        return "Obesity Class I (Moderate)", "Moderate risk of obesity-related health conditions."
    elif 35.0 <= bmi < 40.0:
        return "Obesity Class II (Severe)", "Severe risk of obesity-related health conditions."
    else:
        return "Obesity Class III (Very severe / Morbid)", "Very high risk of obesity-related complications."


def get_positive_float(prompt: str) -> float:
    """Prompt the user until a valid positive float is entered."""
    while True:
        try:
            val = float(input(prompt).strip())
            if val <= 0:
                print("Error: Value must be greater than zero. Please try again.")
                continue
            return val
        except ValueError:
            print("Error: Invalid number. Please enter a numerical value.")


def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description="Calculate Body Mass Index (BMI).")
    parser.add_argument("-w", "--weight", type=float, help="Weight in kilograms (or lbs if --imperial is set)")
    parser.add_argument("-H", "--height", type=float, help="Height in meters/cm (or inches if --imperial is set)")
    parser.add_argument("--imperial", action="store_true", help="Interpret inputs as imperial units (lbs, inches)")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

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
        print("=" * 45)
        print("             BMI CALCULATOR                  ")
        print("=" * 45)
        print("Choose your preferred unit system:")
        print("  1. Metric (kilograms, meters or centimeters)")
        print("  2. Imperial (pounds, feet and inches)")
        
        while True:
            choice = input("\nEnter choice (1 or 2): ").strip()
            if choice in ("1", "2"):
                break
            print("Invalid choice. Please enter 1 or 2.")

        if choice == "1":
            # Metric
            weight_kg = get_positive_float("\nEnter your weight in kilograms (kg): ")
            height_input = get_positive_float("Enter your height in centimeters (cm) or meters (m): ")
            
            # If input is greater than 3, assume centimeters and convert to meters
            if height_input > 3.0:
                height_m = height_input / 100.0
                print(f"Interpreted {height_input} as centimeters ({height_m:.2f} m).")
            else:
                height_m = height_input
        else:
            # Imperial
            weight_lbs = get_positive_float("\nEnter your weight in pounds (lbs): ")
            print("\nEnter height:")
            feet = get_positive_float("  Feet: ")
            inches = float(input("  Inches (press Enter for 0): ").strip() or "0")
            if inches < 0:
                inches = 0.0

            total_inches = (feet * 12.0) + inches
            # 1 lb = 0.45359237 kg, 1 inch = 0.0254 m
            weight_kg = weight_lbs * 0.45359237
            height_m = total_inches * 0.0254

    try:
        bmi = calculate_bmi(weight_kg, height_m)
    except ValueError as e:
        print(f"Error: {e}")
        return

    category, description = get_bmi_category(bmi)

    print("\n" + "=" * 45)
    print("                 RESULTS                     ")
    print("=" * 45)
    print(f"Weight (kg)  : {weight_kg:.2f} kg")
    print(f"Height (m)   : {height_m:.2f} m")
    print(f"Your BMI     : {bmi}")
    print(f"Category     : {category}")
    print(f"Insight      : {description}")
    print("=" * 45)


if __name__ == "__main__":
    main()
