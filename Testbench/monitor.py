from cocotb.triggers import *
from cocotb.queue import QueueEmpty, Queue
from item import Item

class Monitor:
  def __init__(self, dut):
    self.dut = dut
    self.mon_item_queue = Queue()

  async def monitor(self):
    while True:
      mon_item = Item(self.dut)
      mon_item.A			= self.dut.A.value
      mon_item.B			= self.dut.B.value
      mon_item.cin			= self.dut.cin.value
      mon_item.serial_in	= self.dut.serial_in.value
      mon_item.red_op_A		= self.dut.red_op_A.value
      mon_item.red_op_B		= self.dut.red_op_B.value
      mon_item.opcode		= self.dut.opcode.value
      mon_item.bypass_A		= self.dut.bypass_A.value
      mon_item.bypass_B		= self.dut.bypass_B.value
      mon_item.direction	= self.dut.direction.value
      mon_item.out			= self.dut.out.value
      mon_item.out_ref		= self.dut.out_ref.value
      mon_item.leds			= self.dut.leds.value
      mon_item.leds_ref		= self.dut.leds_ref.value
      self.mon_item_queue.put_nowait(mon_item)
      await FallingEdge(self.dut.clk) # wait for falling edge/"negedge"