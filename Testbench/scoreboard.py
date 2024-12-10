from cocotb.queue import QueueEmpty, Queue

class Scoreboard:
	def __init__(self, monitor):
		self.monitor = monitor
		self.error_count = 0
		self.correct_count = 0

	async def check(self):
		while True:
			sb_item = await self.monitor.mon_item_queue.get()
			if sb_item.out != sb_item.out_ref:
				self.monitor.dut._log.info(f"Error: out_ref = {sb_item.out_ref}, while out = {sb_item.out}")
				self.error_count += 1
			else:
				self.correct_count += 1