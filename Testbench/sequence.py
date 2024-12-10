from cocotb.triggers import *
from item import Item

class Sequence:
	def __init__(self, driver, sequencer):
		self.driver = driver
		self.sequencer = sequencer

	async def start(self):
		for i in range(1000):
			randomized_stimulus = Item(self.driver.dut)
			ALSU_item = await randomized_stimulus.randomize()
			await self.sequencer.put_item(ALSU_item)
			self.driver.dut._log.info(f"Sent stimulus: {i}: {ALSU_item}")