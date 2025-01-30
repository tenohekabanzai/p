def greet(greeting,name='Tito'):
    print(f"{greeting} {name}")

greet("Good morn");
# *args -> tuple
# **kwargs -> dict

def info(*args,**kwargs):
    print(args)
    print(kwargs)

info('Maths','Phy',name="Abc",age=20);