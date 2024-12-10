# Add signals to the waveform
add wave -color red 	sim:/ALSU_top/DUT/clk
add wave  			 	sim:/ALSU_top/DUT/rst
add wave  			 	sim:/ALSU_top/DUT/bypass_A
add wave  			 	sim:/ALSU_top/DUT/bypass_B
add wave  			 	sim:/ALSU_top/DUT/red_op_A
add wave  			 	sim:/ALSU_top/DUT/red_op_B
add wave  			 	sim:/ALSU_top/DUT/direction
add wave  			 	sim:/ALSU_top/DUT/serial_in
add wave  			 	sim:/ALSU_top/DUT/cin
add wave 			 	sim:/ALSU_top/DUT/opcode
add wave 			 	sim:/ALSU_top/DUT/A
add wave 			 	sim:/ALSU_top/DUT/B
add wave -color cyan 	sim:/ALSU_top/DUT/out
add wave -color gold 	sim:/ALSU_top/REF_MODEL/out_ref
add wave -color cyan 	sim:/ALSU_top/DUT/leds
add wave -color gold 	sim:/ALSU_top/REF_MODEL/leds_ref

# Remove leaf names
.vcop Action toggleleafnames

# Run the simulation indefinitely (or specify time, e.g., "run 1000ns")
run -all