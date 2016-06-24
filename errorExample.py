class Restaurant():
	#Initializer
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
	def describe_restaurant(self):
		print('The restauran\'s name is' + self.restaurant_name)
		print('It serves' + self.cuisine_type + 'cuisine')
		
	def open_restaurant(self):
		print('Restaurant is open')
	
	
restaurant = Restaurant('Italian','Soup')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant2= Restaurant('Doggy','Dog')
restaurant3= Restaurant('cat','caty')

restaurant2.describe_restaurant()
restaurant3.describe_restaurant()