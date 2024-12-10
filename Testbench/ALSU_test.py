import cocotb
import logging
from cocotb.handle import SimHandle
from cocotb.regression import TestFactory
from cocotb.clock import Clock
from reset_utils import reset
from driver import Driver
from sequence import Sequence
from sequencer import Sequencer
from monitor import Monitor
from scoreboard import Scoreboard
from cocotb.triggers import *

@cocotb.test()
async def ALSU_test(dut):

	"""Generate clock pulses."""
	c = Clock(dut.clk, 2, 'ps')
	await cocotb.start(c.start())

	"""Resetting the design."""
	await reset(dut)
	await FallingEdge(dut.clk) # wait for falling edge/"negedge"

	"""Building the verification environment."""
	ALSU_sequencer = Sequencer()
	ALSU_driver = Driver(dut, ALSU_sequencer)
	ALSU_sequence = Sequence(ALSU_driver, ALSU_sequencer)
	ALSU_monitor = Monitor(dut)
	ALSU_scoreboard = Scoreboard(ALSU_monitor)

	"""Running sequence and driver in parallel"""
	sequence_task = cocotb.start_soon(ALSU_sequence.start()) # Run the sequence to generate and send stimuli
	driver_task = cocotb.start_soon(ALSU_driver.drive()) # Run the driver in the background
	cocotb.start_soon(ALSU_monitor.monitor())
	cocotb.start_soon(ALSU_scoreboard.check())
	await Combine(sequence_task, driver_task)
	dut._log.info(f"correct_count = {ALSU_scoreboard.correct_count}")
	dut._log.info(f"error_count = {ALSU_scoreboard.error_count}")