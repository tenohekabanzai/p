class Duck:
    def quack(self):
        print("Quack Quack");
    def fly(self):
        print("Flap Flap");

class Person:
    def quack(self):
        print("I`m quacking like a duck")
    def fly(self):
        print("I`m flapping")

def check(thing):
    if isinstance(thing,Duck):
        thing.quack()
        thing.fly()
    else:
        print('Object is not a duck')

def check2(thing):
    try:
        thing.quack()
        thing.fly()
    except Exception as e:
        print(e)

d = Duck();
p = Person();
check(d)
check(p)
check2(p)

print("------------------------------------------------------------------")

p = {'name':'Jess','age':30,'job':'doctor'}

try:
    print(f"I`m {p['name']}, I`m {p['age']} years old and I am a {p['job']}")
except Exception as e:
    print(e)

print("------------------------------------------------------------------")


l1 = [1,2,3,4,5]
try:
    print(l1[5])
except IndexError:
    print('That index does not exist')

    
print("------------------------------------------------------------------")