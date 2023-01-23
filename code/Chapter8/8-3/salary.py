from employee import FullTimeEmployee
from employee import PartTimeEmployee

def main():
    employees = [
        FullTimeEmployee('Alice', 5783, 173),
        PartTimeEmployee('Bob', 150, 15)
    ]

    for employee in employees:
        print(
            employee.get_name() + ': $' + str(employee.get_salary())
        )

if __name__ == '__main__':
    main()