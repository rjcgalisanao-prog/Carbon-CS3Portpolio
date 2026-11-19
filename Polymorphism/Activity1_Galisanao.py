class Patient:

    def __init__(self, name, bill_amount):
        self._name = name
        self.set_bill_amount(bill_amount)

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_bill_amount(self):
        return self._bill_amount

    def set_bill_amount(self, bill_amount):
        if bill_amount < 0:
            raise ValueError("Bill amount cannot be negative.")
        self._bill_amount = bill_amount

    def calculate_bill(self):
        return self._bill_amount

    def display_patient_type(self):
        return "Patient Type: Regular Patient"

    def display_info(self):
        print(f"Patient Name: {self._name}, "
              f"Patient Type: {self.display_patient_type()}, "
              f"Original Bill Amount: {self._bill_amount:,.2f}, "
              f"Final Bill Amount: {self.calculate_bill():,.2f}")


class SeniorPatient(Patient):
    DISCOUNT = 0.20

    def calculate_bill(self):
        return super().calculate_bill() * (1 - self.DISCOUNT)

    def display_patient_type(self):
        return "Patient Type: Senior Patient"


class PhilHealthPatient(Patient):
    DISCOUNT = 0.15

    def calculate_bill(self):
        return super().calculate_bill() * (1 - self.DISCOUNT)

    def display_patient_type(self):
        return "Patient Type: PhilHealth Patient"


if __name__ == "__main__":
    regular_patient = Patient("Juan Dela Cruz", 15000.00)
    senior_patient = SeniorPatient("Maria Santos", 20000.00)
    philhealth_patient = PhilHealthPatient("Pedro Garcia", 25000.00)

    for patient in (regular_patient, senior_patient, philhealth_patient):
        patient.display_info()

    regular_patient.set_bill_amount(18000.00)
    print("\nAfter updating the regular patient's bill:")
    regular_patient.display_info()

    try:
        regular_patient.set_bill_amount(-500)
    except ValueError as error:
        print(f"\nError caught: {error}")