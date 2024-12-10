from cocotb.triggers import *
from cocotb.queue import QueueEmpty, Queue
from item import Item

class Sequencer:
	def __init__(self):
		self.item_queue = Queue()

	async def put_item(self, item):
		await self.item_queue.put(item)  # Send stimulus to the driver

	async def get_item(self):
		item = self.item_queue.get_nowait() # Recieves stimulus for the driver
		return item