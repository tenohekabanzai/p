li = [4,5565,23,556,765,5214335,878];
sli = sorted(li);
rli = sorted(li,reverse=1);
print(sli)
print(rli)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
l2 = [-6,-5,-4,1,2,3];
# // sorted according to absolute val
sli = sorted(l2,key=abs)
print(sli)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __repr__(self):
        return f"{self.name} {self.age} {self.salary}"


e1 = Employee("Abc",37,70000)
e2 = Employee("Def",29,80000)
e3 = Employee("Ghi",43,90000)

# def comp_by_salary(emp):
#     return emp.salary;
# def comp_by_age(emp):
#     return emp.age;

emp = [e1,e2,e3];
# emp_s = sorted(emp,key=comp_by_salary)
# emp_a = sorted(emp,key=comp_by_age,reverse=1)

emp_s = sorted(emp,key= lambda e : e.salary)
emp_a = sorted(emp,key= lambda e : e.age)
emp_n = sorted(emp,key= lambda e : e.name)

print(emp_s);
print(emp_a);
print(emp_n);