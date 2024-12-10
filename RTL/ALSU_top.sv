module ALSU_top();

  parameter INPUT_PRIORITY = "A";
  parameter FULL_ADDER = "ON";
  logic clk, rst, cin, red_op_A, red_op_B, bypass_A, bypass_B, direction, serial_in;
  logic [2:0] opcode;
  logic signed [2:0] A, B;
  logic [15:0] leds;
  logic [5:0] out;
  logic [5:0] out_ref;
  logic [15:0] leds_ref;

  ALSU DUT(A, B, cin, serial_in, red_op_A, red_op_B, opcode, bypass_A, bypass_B, clk, rst, direction, leds, out);
  ALSU_ref REF_MODEL(A, B, cin, serial_in, red_op_A, red_op_B, opcode, bypass_A, bypass_B, clk, rst, direction, leds_ref, out_ref);
endmodule