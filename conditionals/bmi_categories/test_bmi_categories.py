def test_bmi_categories(solution):
    cases = [
        (45, 1.65, "Underweight"),
        (50, 1.70, "Underweight"),
        (55, 1.70, "Normal weight"),
        (70, 1.75, "Normal weight"),
        (60, 1.60, "Normal weight"),
        (75, 1.75, "Normal weight"),
        (85, 1.75, "Overweight"),
        (90, 1.80, "Overweight"),
        (80, 1.60, "Obese"),
        (100, 1.75, "Obese"),
        (120, 1.70, "Obese"),
    ]

    for weight, height, expected_output in cases:
        solution.check_output(
            input_text=f"{weight}\n{height}\n", expected_output=expected_output
        )
