patients = [[70, 1.8],[80, 1.9],[150, 1.7]]


def calculate_bmi(weight, height):
    return weight / (height**2)


for patient in patients:
    weight, height = patient[0]
    bmi = calculate_bmi(height, weight)
    print("Patients's BMI is: "%f %bmi)