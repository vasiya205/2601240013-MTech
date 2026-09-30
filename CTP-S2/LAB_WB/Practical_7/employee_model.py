from dataclasses import dataclass
import sys

class EmployeeTraditional:
    def __init__(self, emp_id: int, name: str, dept: str, salary: float):
        self.emp_id = emp_id
        self.name = name
        self.dept = dept
        self.salary = salary

    def __repr__(self) -> str:
        return f"EmployeeTraditional(emp_id={self.emp_id}, name='{self.name}', dept='{self.dept}', salary={self.salary})"

@dataclass
class EmployeeDataClass:
    emp_id: int
    name: str
    dept: str
    salary: float

if __name__ == "__main__":
    t_obj = EmployeeTraditional(101, "Alice Smith", "Cybersecurity", 75000.0)
    d_obj = EmployeeDataClass(101, "Alice Smith", "Cybersecurity", 75000.0)
    
    print("Traditional:", t_obj)
    print("Dataclass:  ", d_obj)
    print(f"Memory -> Traditional: {sys.getsizeof(t_obj)}B | Dataclass: {sys.getsizeof(d_obj)}B")
