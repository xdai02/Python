class Employee:
    def __init__(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def get_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, basic_salary, bonus):
        super().__init__(name)
        self.__basic_salary = basic_salary
        self.__bonus = bonus
    
    def get_salary(self):
        return self.__basic_salary + self.__bonus
    
class PartTimeEmployee(Employee):
    def __init__(self, name, daily_wage, working_days):
        super().__init__(name)
        self.__daily_wage = daily_wage
        self.__working_days = working_days

    def get_salary(self):
        return self.__daily_wage * self.__working_days