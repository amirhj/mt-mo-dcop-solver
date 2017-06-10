import math

class Functions:
	def __init__(self, fg):
		self.fg = fg

	def calculate(self, name, values):
		function = getattr(self, name)
		return function(values)

		
	def a1_money(self, values):
		w_a1_a2 = values["w_a1_a2"]
		w_a1_a4 = values["w_a1_a4"]
		w_a4_a1 = values["w_a4_a1"]
		
		tp_a1_a4 = self.fg.constants["tp_a1_a4"]
		tp_a1_a2 = self.fg.constants["tp_a1_a2"]
		price = self.fg.constants["price"]
		
		in_water = w_a4_a1
		out_water = w_a1_a4 + w_a1_a2
		value = (out_water - in_water) * price - (w_a1_a2*tp_a1_a2 + w_a1_a4*tp_a1_a4)
		
		return value * -1
		
	def a1_supply(self, values):
		w_a1_a2 = values["w_a1_a2"]
		w_a1_a4 = values["w_a1_a4"]
		w_a4_a1 = values["w_a4_a1"]
		
		in_water = w_a4_a1
		out_water = w_a1_a4 + w_a1_a2
		
		max_delivery_a1 = self.fg.constants["max_delivery_a1"]
		demand_a1 = self.fg.constants["demand_a1"]
		
		value = abs(demand_a1 - in_water + out_water - max_delivery_a1)
		
		return value
		
	def a2_money(self, values):
		w_a1_a2 = values["w_a1_a2"]
		w_a2_a4 = values["w_a2_a4"]
		w_a2_a5 = values["w_a2_a5"]
		w_a3_a2 = values["w_a3_a2"]
		w_a5_a2 = values["w_a5_a2"]
		
		tp_a2_a4 = self.fg.constants["tp_a2_a4"]
		tp_a2_a5 = self.fg.constants["tp_a2_a5"]
		price = self.fg.constants["price"]
		
		in_water = w_a5_a2 + w_a1_a2 + w_a3_a2
		out_water = w_a2_a4 + w_a2_a5
		value = (out_water - in_water) * price - (w_a2_a5*tp_a2_a5 + w_a2_a4*tp_a2_a4)
		
		return value * -1
		
	def a2_supply(self, values):
		w_a1_a2 = values["w_a1_a2"]
		w_a2_a4 = values["w_a2_a4"]
		w_a2_a5 = values["w_a2_a5"]
		w_a3_a2 = values["w_a3_a2"]
		w_a5_a2 = values["w_a5_a2"]
		
		in_water = w_a5_a2 + w_a1_a2 + w_a3_a2
		out_water = w_a2_a4 + w_a2_a5
		
		max_delivery_a2 = self.fg.constants["max_delivery_a2"]
		demand_a2 = self.fg.constants["demand_a2"]
		
		value = abs(demand_a2 - in_water + out_water - max_delivery_a2)
		
		return value
		
	def a3_money(self, values):
		w_a3_a2 = values["w_a3_a2"]
		w_a3_a4 = values["w_a3_a4"]
		w_a3_a5 = values["w_a3_a5"]
		
		tp_a3_a2 = self.fg.constants["tp_a3_a2"]
		tp_a3_a5 = self.fg.constants["tp_a3_a5"]
		tp_a3_a4 = self.fg.constants["tp_a3_a4"]
		price = self.fg.constants["price"]
		
		in_water = 0
		out_water = w_a3_a5 + w_a3_a4 + w_a3_a2
		value = (out_water - in_water) * price - (w_a3_a5*tp_a3_a5 + w_a3_a2*tp_a3_a2 + w_a3_a4*tp_a3_a4)
		
		return value * -1
		
	def a3_supply(self, values):
		w_a3_a2 = values["w_a3_a2"]
		w_a3_a4 = values["w_a3_a4"]
		w_a3_a5 = values["w_a3_a5"]
		
		in_water = 0
		out_water = w_a3_a5 + w_a3_a4 + w_a3_a2
		
		max_delivery_a3 = self.fg.constants["max_delivery_a3"]
		demand_a3 = self.fg.constants["demand_a3"]
		
		value = abs(demand_a3 - in_water + out_water - max_delivery_a3)
		
		return value
		
	def a4_money(self, values):
		w_a1_a4 = values["w_a1_a4"]
		w_a2_a4 = values["w_a2_a4"]
		w_a3_a4 = values["w_a3_a4"]
		w_a4_a1 = values["w_a4_a1"]
		w_a5_a4 = values["w_a5_a4"]
		
		tp_a4_a1 = self.fg.constants["tp_a4_a1"]
		price = self.fg.constants["price"]
		
		in_water = w_a3_a4 + w_a1_a4 + w_a2_a4 + w_a5_a4
		out_water = w_a4_a1
		value = (out_water - in_water) * price - (w_a4_a1*tp_a4_a1)
		
		return value * -1
		
	def a4_supply(self, values):
		w_a1_a4 = values["w_a1_a4"]
		w_a2_a4 = values["w_a2_a4"]
		w_a3_a4 = values["w_a3_a4"]
		w_a4_a1 = values["w_a4_a1"]
		w_a5_a4 = values["w_a5_a4"]
		
		in_water = w_a3_a4 + w_a1_a4 + w_a2_a4 + w_a5_a4
		out_water = w_a4_a1
		
		max_delivery_a4 = self.fg.constants["max_delivery_a4"]
		demand_a4 = self.fg.constants["demand_a4"]
		
		value = abs(demand_a4 - in_water + out_water - max_delivery_a4)
		
		return value
		
	def a5_money(self, values):
		w_a2_a5 = values["w_a2_a5"]
		w_a3_a5 = values["w_a3_a5"]
		w_a5_a2 = values["w_a5_a2"]
		w_a5_a4 = values["w_a5_a4"]
		
		tp_a5_a2 = self.fg.constants["tp_a5_a2"]
		tp_a5_a4 = self.fg.constants["tp_a5_a4"]
		price = self.fg.constants["price"]
		
		in_water = w_a3_a5 + w_a2_a5
		out_water = w_a5_a2 + w_a5_a4
		value = (out_water - in_water) * price - (w_a5_a2*tp_a5_a2 + w_a5_a4*tp_a5_a4)
		
		return value * -1
		
	def a5_supply(self, values):
		w_a2_a5 = values["w_a2_a5"]
		w_a3_a5 = values["w_a3_a5"]
		w_a5_a2 = values["w_a5_a2"]
		w_a5_a4 = values["w_a5_a4"]
		
		in_water = w_a3_a5 + w_a2_a5
		out_water = w_a5_a2 + w_a5_a4
		
		max_delivery_a5 = self.fg.constants["max_delivery_a5"]
		demand_a5 = self.fg.constants["demand_a5"]
		
		value = abs(demand_a5 - in_water + out_water - max_delivery_a5)
		
		return value