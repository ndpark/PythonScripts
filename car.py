#! python3
# car.py - practice using classes and instances

class Car():
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.milage = 0
		
	def get_name(self):
		long_name = str(self.year) +' ' + self.make + ' '+ self.model
		return long_name
		
	def get_milage(self):
		print('The milage is ' + str(self.milage))
		
	def update_milage(self,miles):
		self.milage += int(miles)
		
		
"""myCar = Car('Audi', 'A4', '2015')
print(myCar.get_name())
myCar.get_milage()
myCar.update_milage(input())
myCar.get_milage()"""


#Inheritance
class BetterCar(Car):
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.batterySize = 70
		
	def battery(self):
		print('Battery size is'+ str(self.batterySize))
		
tesla = BetterCar('Tesla','S','2016')

print(tesla.get_name())