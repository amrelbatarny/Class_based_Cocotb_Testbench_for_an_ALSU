import logging
from cocotb.triggers import *

# Coroutine to reset the DUT
async def reset(dut):
	dut._log.info("--------------------------------------------------------------------------------------")
	dut._log.info("Resetting the DUT")
	dut.rst.value = 1;
	await FallingEdge(dut.clk) # wait for falling edge/"negedge"
	dut.rst.value = 0;
	dut._log.info("DUT is resetted")
	dut._log.info("--------------------------------------------------------------------------------------")