class Engine:
    def __init__(self,size,power):
        self.size = size
        self.power = power
        
class Battery:
    def __init__(self,range,life):
        self.range = range
        self.life = life

class Hybrid(Engine,Battery):
    def __init__(self,size,power,range,life):
        Engine.__init__(self,size,power)
        Battery.__init__(self,range,life)

hc = Hybrid(2.4,300,200,10)
print(hc.life,hc.power)