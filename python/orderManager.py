from order import Order, ORDER_STATUS
class OrderManager():
	"""docstring for OrderManager"""
	def __init__(self):
		self.orders = []

	def add_order(self, id, x, y, items):
		self.orders.append(Order(id, x, y, items))

	def next_unhandled_order(self):
		for order in self.orders:
			if order.status == ORDER_STATUS.UNHANDELD:
				return order
		return None

	def has_unhandled_command(self):
		for order in self.orders:
			if order.status == ORDER_STATUS.UNHANDELD:
				return True
		return False
