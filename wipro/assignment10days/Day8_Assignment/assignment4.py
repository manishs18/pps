'''
Problem Statement

Care hospital wants to calculate the bill amount to be paid by patients visiting the hospital. 
Bill amount includes consultation fees and price of medicines purchased from their pharmacy.

Write a Python program to implement the class diagram given below.

Bill                                                                      Bill

-bill_id                                                                 -bill_id
-patient_name                                                            -patent_name
-bill_amount                                                             -bill_amount


__init__(bill_id, patient_name)                                          __init__(bill_id, patient_name)
+calculate bill amount(consultation fees, quantity list, price list)     +calculate bil amount(consultation fees, quantity list, price list)

+get_all_id()                                                            +get_all_id()
+get_patient_name()                                                      +get_patient_name()
+get_bill_amount()                                                       +get_bll_amount()

Method description:

calculate_bil_amount(consultation_fees, quantity_list, price_list): Accept consultation_fees, quantity_list (quantities of medicines purchased) and price_list (price per quantity of medicines purchased)

a. Calculate total bill amount to be paid by the patient. Bill amount includes consultation fees and price of medicines
b. Initialize attribute, bill amount with the total bill amount

Note: Quantity list and price list have one-to-one correspondence. Quantity and price per quantity of ist medicine purchased by the patient is present at Oth index of both lists, 2nd medicine is present at 1st index and so on.

For testing:

Create objects of Bill class
Invoke calculate bill amount(consultation fees, quantity list, price list) method on Bill object by passing consultation fees, quantity list and price list
Display bill id, patient name and bill amount
'''

class Bill:
    def __init__(self, bill_id, patient_name):
        self.bill_id = bill_id
        self.patient_name = patient_name
        self.bill_amount = 0  

    def calculate_bill_amount(self, consultation_fees, quantity_list, price_list):
        medicine_cost = sum(q * p for q, p in zip(quantity_list, price_list))
        self.bill_amount = consultation_fees + medicine_cost

    def get_bill_id(self):
        return self.bill_id

    def get_patient_name(self):
        return self.patient_name

    def get_bill_amount(self):
        return self.bill_amount


def main():
    patient1 = Bill("B101", "John Doe")
    patient2 = Bill("B102", "Jane Smith")

    patient1.calculate_bill_amount(
        consultation_fees=500, 
        quantity_list=[2, 3, 1], 
        price_list=[50, 30, 100]
    )
    patient2.calculate_bill_amount(
        consultation_fees=700, 
        quantity_list=[1, 4], 
        price_list=[200, 25]
    )

    print(f"Bill ID: {patient1.get_bill_id()}, Patient Name: {patient1.get_patient_name()}, Bill Amount: {patient1.get_bill_amount()}")
    print(f"Bill ID: {patient2.get_bill_id()}, Patient Name: {patient2.get_patient_name()}, Bill Amount: {patient2.get_bill_amount()}")


if __name__ == "__main__":
    main()
