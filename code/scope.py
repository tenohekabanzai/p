'''
LEGB
Local,Enclosing, Global, Built-in
'''

x = 'global x'

def test():
    y = 'local y'
    global z
    z = 100
    print(y)
    print(x)

test()
print(z)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def outer():
    x = 'outer x'
    def inner():
        x = '_inner x'
        print(x)
        print(x)
    inner()
    print(x)

outer()

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def of():
    x = 'outer x'
    def inf():
        nonlocal x
        x = 'modified by inner func'
    inf()
    print(x)

of()