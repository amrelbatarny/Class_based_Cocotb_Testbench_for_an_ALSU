import logging
from cocotb.triggers import *
from cocotb.queue import QueueEmpty, Queue

#Coroutine for driving the DUT
class Driver:
	def __init__(self, dut, sequencer):
		self.dut = dut
		self.sequencer = sequencer

	async def drive(self):
		i = 0
		while True:
			try:
				dvr_item = await self.sequencer.get_item()
				self.dut._log.info(f"Driving DUT with: {i}: {dvr_item}")
				"""Create the Item object and randomize the values."""
				self.dut.A.value 			= dvr_item.A 
				self.dut.B.value 			= dvr_item.B 
				self.dut.cin.value 			= dvr_item.cin 
				self.dut.serial_in.value 	= dvr_item.serial_in 
				self.dut.red_op_A.value 	= dvr_item.red_op_A 
				self.dut.red_op_B.value 	= dvr_item.red_op_B 
				self.dut.opcode.value 		= dvr_item.opcode 
				self.dut.bypass_A.value 	= dvr_item.bypass_A 
				self.dut.bypass_B.value 	= dvr_item.bypass_B 
				self.dut.direction.value 	= dvr_item.direction
				await FallingEdge(self.dut.clk) # wait for falling edge/"negedge"
				i += 1
			except QueueEmpty:
				break