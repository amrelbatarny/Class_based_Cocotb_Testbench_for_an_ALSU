# Makefile

# defaults
GUI=1
WAVES=1
SIM ?= questa
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/../RTL/ALSU.sv $(PWD)/../RTL//ALSU_ref.sv $(PWD)/../RTL//ALSU_top.sv
# use VHDL_SOURCES for VHDL files

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = ALSU_top

# MODULE is the basename of the Python test file
MODULE = ALSU_test

include $(shell cocotb-config --makefiles)/Makefile.sim