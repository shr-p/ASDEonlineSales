import csv
# This code calculates the average monthly salary for each department in a CSV file.

# First, read the Employee.csv file into a dictionary. The keys of the dictionary will be the employee IDs and the values will be dictionaries containing the employee's department ID and name.
employee_data = {}
with open('Employees.csv', mode='r') as employee_file:
    employee_reader = csv.DictReader(employee_file)
    for row in employee_reader:
        employee_data[row['ID']] = {'deptid': row['DEPTID'], 'name': row['NAME']}

# Next, read the Department.csv file into a dictionary. The keys of the dictionary will be the department IDs and the values will be dictionaries containing the department name.
department_data = {}
with open('Departments.csv', mode='r') as department_file:
    department_reader = csv.DictReader(department_file)
    for row in department_reader:
        department_data[row['ID']] = {'name': row['NAME']}

# Finally, read the Salaries.csv file into a dictionary. The keys of the dictionary will be the employee IDs and the values will be dictionaries containing the employee's monthly salary.
salaries_data = {}
with open('Salaries.csv', mode='r') as salaries_file:
    salaries_reader = csv.DictReader(salaries_file)
    for row in salaries_reader:
        salaries_data[row['EMP_ID']] = {'amount': int(row['AMT (USD)'])}

# Now, we can calculate the average monthly salary for each department. First, we create two dictionaries: department_salary_totals and department_count. department_salary_totals will store the total salary for each department and department_count will store the number of employees in each department.
department_salary_totals = {}
department_count = {}

# Iterate over the employee data and add the salary of each employee to the total salary for the employee's department. We also increment the count for the employee's department.
for employee_id, employee_info in employee_data.items():
    dept_id = employee_info['deptid']
    salary = salaries_data.get(employee_id, {}).get('amount', 0)

    department_salary_totals[dept_id] = department_salary_totals.get(dept_id, 0) + salary
    department_count[dept_id] = department_count.get(dept_id, 0) + 1

# Now, we can calculate the average monthly salary for each department by dividing the total salary by the number of employees in the department.
average_monthly_salaries = {}
for dept_id, total_salary in department_salary_totals.items():
    count = department_count[dept_id]
    average_monthly_salaries[dept_id] = total_salary / (count )

# Finally, we sort the departments by average monthly salary in descending order and select the top 3 departments.
sorted_departments = sorted(average_monthly_salaries.items(), key=lambda x: x[1], reverse=True)
top_3_departments = sorted_departments[:3]

# Print the results to the console.
for dept_id, avg_salary in top_3_departments:
    dept_name = department_data.get(dept_id, {}).get('name', 'N/A')
    print(f'Department: {dept_name}, Average Monthly Salary: {avg_salary:.2f}')
