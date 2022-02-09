

from msilib.schema import Class
from re import A


class Elevator:
     def __init__(self, starting_Floor):
        self.make = "The elevator company"
        self.floor = starting_Floor
        
elevator = Elevator(1)
print(elevator.make)
print(elevator.floor)
    
    
    
    
class Car:
    def __init__(self,color_name,maker_name):
        self.color = color_name
        self.maker = maker_name
        
output = Car('red','Benz')
print(output.color )


