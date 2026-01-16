name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
department = input("Enter Department: ")
basic_salary = float(input("Enter Basic Salary: "))


DA = 0.92 * basic_salary
HRA = 0.58 * basic_salary
TA = 0.30 * basic_salary
LIC = 500

gross_salary = basic_salary + DA + HRA + TA
net_salary = gross_salary - LIC

print("\n----- Employee Salary Details -----")
print("Name          :", name)
print("Employee ID   :", emp_id)
print("Department    :", department)
print("Basic Salary  :", basic_salary)
print("Net Salary    :", net_salary)
