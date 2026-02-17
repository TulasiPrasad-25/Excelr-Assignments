room_charge_per_day = 2000
doctor_fee = 1500
lab_test_charge = 300
days_stayed = 4
number_of_tests = 3
medicine_charges = 2400

# Calculating individual charges
room_charges = room_charge_per_day * days_stayed
lab_charges = lab_test_charge * number_of_tests

# Total bill before discount
total_bill = room_charges + doctor_fee + lab_charges + medicine_charges

# Applying discount if applicable
if total_bill > 10000:
    discount = 0.10 * total_bill
else:
    discount = 0

final_bill = total_bill - discount

# Displaying the bill details
print("----- Hospital Bill Details -----")
print(f"Room Charges      : Rs {room_charges}")
print(f"Doctor Fee        : Rs {doctor_fee}")
print(f"Lab Test Charges  : Rs {lab_charges}")
print(f"Medicine Charges  : Rs {medicine_charges}")
print(f"Discount Applied  : Rs {discount}")
print(f"Final Bill Amount : Rs {final_bill}")
