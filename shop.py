####################### DO NOT MODIFY THIS CODE ########################
menu = {
	"original cupcake": 2,
	"signature cupcake": 2.750,
	"coffee": 1,
	"tea": 0.900,
	"bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "MG"
signature_flavors = ["spicy touch", "raw raspberry", "spaical signture"]
order_list = []


def print_menu():
	"""
	Print the items in the menu dictionary.
	"""
	# your code goes here!
	print ("our menu")
	for item in menu:
		print ("- %s(KD %s)" % (item,menu[item]))


def print_originals():
	"""
	Print the original flavor cupcakes.
	"""
	print("Our original flavor cupcakes (KD %s each):" % original_price)

	# your code goes here!
	for item in original_flavors:
		print (("-%s")% item)
	   
def print_signatures():
	"""
	Print the signature flavor cupcakes.
	"""
	print("Our signature flavor cupcake (KD %s each):" % signature_price)
	# your code goes here!
	for item in signature_flavors:
		print (("- %s") % item)


def is_valid_order(order):
	"""
	Check if an order exists in the shop.
	"""
	# your code goes here!
	if order in menu or order in original_flavors or order in signature_flavors:
		print("added")
		return True
	else:
		print ("we dont have it anymore!")
		return False 
		
		


def get_order():
	"""
	Repeatedly ask customer for order until they end their order by typing "Exit".
	"""
	order_list = []
	# your code goes here!
	
	print("what's your order?")
	while True:
		order= input ()
		if order == "Exit":
				break
		elif is_valid_order(order): 
				order_list.append(order)
		else:
			print ("Your order is not in stock:%s" % order)
	return order_list


def accept_credit_card(total):
	"""
	Return whether an order is eligible for credit card payment.
	"""
	# your code goes here!
	if total >= 5:
		print("Credit card payment is acceptable")
	else:
		print("cash only")

def get_total_price(order_list):
	"""
	Calculate and return total price of the order.
	"""
	total = 0
	# your code goes here!
	for item in order_list:
		if item in menu:
			total += menu[item]
		elif item in original_flavors:
			total += original_price
		elif item in signature_flavors:
			total += signature_price
		
	return total


def print_order(order_list):
	"""
	Print the order of the customer.
	"""
	print(order_list)
	print("Your order is: ")
	# your code goes here!
	for item in order_list:
		print("%s \n" % item)


	print("%s \n" % get_total_price(order_list))


	print("Thank you for visiting")	