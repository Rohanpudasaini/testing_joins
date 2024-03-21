from database_connection import session, engine
from models1 import Company, Employee, Department, Select, Employee2

statement = Select(
    Employee.name, Department.name, Company.name, Employee.salary, Employee2.address
    ).select_from(Employee).join(Department).join(Company).join(Employee2, Employee.id==Employee2.department_id)
results = session.execute(statement).all()
# for result in results:
#     for result2 in result:
#         print(result2.__dict__) 

# for employee, department, company in results:
    # print(employee.name , department.name, company.name)
print('Employee Name,', 'Department Name,', 'Company Name,', 'Salary,', 'Address')
for result in results:
    print(result)
