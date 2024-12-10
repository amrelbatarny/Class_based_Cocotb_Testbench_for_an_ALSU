import random
from cocotb_utils import max

class Item:
	"""Class to handle stimulus generation."""
	def __init__(self, dut):
		self.dut = dut
		# Grouping signals into a class
		self.A 			= 0
		self.B 			= 0
		self.cin 		= 0
		self.serial_in 	= 0
		self.red_op_A 	= 0
		self.red_op_B 	= 0
		self.opcode 	= 0
		self.bypass_A 	= 0
		self.bypass_B 	= 0
		self.direction 	= 0
		self.out 		= 0
		self.out_ref 	= 0
		self.leds 		= 0
		self.leds_ref 	= 0

	async def randomize(self):
		self.A 			= random.randint(0, max(self.dut.A)) 
		self.B 			= random.randint(0, max(self.dut.B)) 
		self.cin 		= random.randint(0, max(self.dut.cin)) 
		self.serial_in 	= random.randint(0, max(self.dut.serial_in)) 
		self.red_op_A 	= random.randint(0, max(self.dut.red_op_A)) 
		self.red_op_B 	= random.randint(0, max(self.dut.red_op_B)) 
		self.opcode 	= random.randint(0, max(self.dut.opcode)) 
		self.bypass_A 	= random.randint(0, max(self.dut.bypass_A)) 
		self.bypass_B 	= random.randint(0, max(self.dut.bypass_B)) 
		self.direction 	= random.randint(0, max(self.dut.direction))
		# Return self to use the randomized values
		return self