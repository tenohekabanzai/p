#1 create Car class with attributes like brand and model
# create an instance of this class

class Car:
    
    tot_car = 0; # Class variable
    
    # constructor
    def __init__(self,brand=None,model=None):
        self.brand = brand
        self.__model = model # making model pvt
        self.__pvt_var = 1000 # private variable
        Car.tot_car +=1; # Class variable updated
        
    def printName(self):
        print(f"'{self.brand} {self.model}!!!'")
        
    def getpvtvar(self): # getter for pvtvar
        print(self.__pvt_var);
        
    def setpvtvar(self,n): # setter from pvtvar
        self.__pvt_var = n
    
    def getFuelType(self):
        print('Hydrocarbons!!!')
        
    @staticmethod
    def gen_desc():
        print('Cars are means of transport');
        
    @property
    def model(self): # only getter available for model (model cannot be overwtiten once set)
        return self.__model
        
        
# child class inheriting from Parent Car
class ElectricCar(Car):
    def __init__(self, brand=None, model=None,range=None):
        super().__init__(brand, model)
        self.range = range
    def printStats(self):
        self.printName();
        print(f"range is {self.range} kms")
    def getFuelType(self): # func overriding
        print('Electricity baby !!!!!!')
    
    
    
my_car = Car(None,'Alto')
print(my_car)
print(my_car.brand,my_car.model)


my_car_2 = Car('Jeep','Meridian')
print(my_car_2.brand,my_car_2.model)

my_car_2.printName()



ec = ElectricCar('MG','Windsor','400')
ec.printStats()

ec.setpvtvar(1900)
ec.getpvtvar()
my_car_2.getpvtvar()

ec.getFuelType()
my_car.getFuelType()

print(ec.tot_car)  # changes thrice as constr called thrice 

# calling static methods -< only callable thru class names
Car.gen_desc()
ElectricCar.gen_desc()
# static method vnot callable thru any object

# calling model as a property
print(my_car.model)
print(my_car_2.model)
print(ec.model)