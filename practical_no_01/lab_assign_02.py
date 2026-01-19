vendor_name = input("Enter Vendor Name: ")
year_of_association = int(input("Enter Year of Association: "))
contact_number = input("Enter Contact Number: ")
email_id = input("Enter Email ID: ")

total = 0
monthly_purchases = []



print("\nEnter Monthly Purchase Amounts:")
for i in range(1, 13):
    amount = float(input("Enter purchase for month " + str(i) + ": "))
    monthly_purchases.append(amount)
    total = total + amount

print("\n--------- Annual Purchase / Billing Report ---------")
print("Vendor Name         :", vendor_name)
print("Year of Association :", year_of_association)
print("Contact Number      :", contact_number)
print("Email ID            :", email_id)

print("\nMonthly Purchases:")
for i in range(1, 13):
    print("Month", i, ":", monthly_purchases[i - 1])


print("\nTotal Annual Purchase :", total)