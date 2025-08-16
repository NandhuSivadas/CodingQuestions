class Employee:
    def __init__(self, employee_name, designation, salary, overTimeContribution):
        self.employee_name = employee_name
        self.designation = designation
        self.salary = salary
        self.overTimeContribution = overTimeContribution 
        self.overTimeStatus = False 

class Organization:
    def __init__(self, employee_list):
        self.employee_list = employee_list

    def check_overtime_eligibility(self, overTimeThreshold):
        for emp in self.employee_list:
            total_hours = sum(emp.overTimeContribution.values())
            if total_hours >= overTimeThreshold:
                emp.overTimeStatus = True
            else:
                emp.overTimeStatus = False

    def calculate_total_bonus(self, rate_per_hour):
        total_bonus = 0
        for emp in self.employee_list:
            if emp.overTimeStatus:
                total_bonus += sum(emp.overTimeContribution.values()) * rate_per_hour
        return total_bonus



n = int(input())  
employees = []

for _ in range(n):
    name = input().strip()
    designation = input().strip()
    salary = float(input().strip())
    months_count = int(input().strip())
    
    overTimeContribution = {}
    for _ in range(months_count):
        month = input().strip()
        hours = int(input().strip())
        overTimeContribution[month.lower()] = hours
    
    emp = Employee(name, designation, salary, overTimeContribution)
    employees.append(emp)


org = Organization(employees)

overTimeThreshold = int(input().strip())
rate_per_hour = int(input().strip())

org.check_overtime_eligibility(overTimeThreshold)


for emp in employees:
    print(emp.employee_name, emp.overTimeStatus)

print(org.calculate_total_bonus(rate_per_hour))
