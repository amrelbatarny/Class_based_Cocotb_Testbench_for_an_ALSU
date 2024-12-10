module ALSU_ref(A, B, cin, serial_in, red_op_A, red_op_B, opcode, bypass_A, bypass_B, clk, rst, direction, leds_ref, out_ref);
parameter INPUT_PRIORITY = "A";
parameter FULL_ADDER = "ON";
input clk, rst, cin, red_op_A, red_op_B, bypass_A, bypass_B, direction, serial_in;
input [2:0] opcode;
input signed [2:0] A, B;
output reg [15:0] leds_ref;
output reg [5:0] out_ref;

reg cin_reg, red_op_A_reg, red_op_B_reg, bypass_A_reg, bypass_B_reg, direction_reg, serial_in_reg;
reg [2:0] opcode_reg, A_reg, B_reg;

wire invalid_red_op, invalid_opcode, invalid;

assign invalid_red_op = (red_op_A_reg | red_op_B_reg) & (opcode_reg[1] | opcode_reg[2]);
assign invalid_opcode = opcode_reg[1] & opcode_reg[2];
assign invalid = invalid_red_op | invalid_opcode;

always @(posedge clk or posedge rst) begin
  if(rst) begin
    leds_ref <= 0;
    out_ref <= 0;
    cin_reg <= 0;
    red_op_B_reg <= 0;
    red_op_A_reg <= 0;
    bypass_B_reg <= 0;
    bypass_A_reg <= 0;
    direction_reg <= 0;
    serial_in_reg <= 0;
    opcode_reg <= 0;
    A_reg <= 0;
    B_reg <= 0;
  end
  else begin
    if (invalid)
      leds_ref <= ~leds_ref;
    else
    leds_ref <= 0;
    cin_reg <= cin;
    red_op_B_reg <= red_op_B;
    red_op_A_reg <= red_op_A;
    bypass_B_reg <= bypass_B;
    bypass_A_reg <= bypass_A;
    direction_reg <= direction;
    serial_in_reg <= serial_in;
    opcode_reg <= opcode;
    A_reg <= A;
    B_reg <= B;
    if (bypass_A_reg && bypass_B_reg)
      out_ref <= (INPUT_PRIORITY == "A")? A_reg: B_reg;
    else if (bypass_A_reg)
      out_ref <= A_reg;
    else if (bypass_B_reg)
      out_ref <= B_reg;
    else if (invalid) 
        out_ref <= 0;
    else begin
        case (opcode)
          3'h0: begin 
            if (red_op_A_reg && red_op_B_reg)
              out_ref = (INPUT_PRIORITY == "A")? |A_reg: |B_reg;
            else if (red_op_A_reg) 
              out_ref <= |A_reg;
            else if (red_op_B_reg)
              out_ref <= |B_reg;
            else 
              out_ref <= A_reg | B_reg;
          end
          3'h1: begin
            if (red_op_A_reg && red_op_B_reg)
              out_ref <= (INPUT_PRIORITY == "A")? ^A_reg: ^B_reg;
            else if (red_op_A_reg) 
              out_ref <= ^A_reg;
            else if (red_op_B_reg)
              out_ref <= ^B_reg;
            else 
              out_ref <= A_reg ^ B_reg;
          end
          3'h2: begin
            if (FULL_ADDER == "ON")
              out_ref <= A_reg + B_reg + cin_reg;
            else
              out_ref <= A_reg + B_reg;
          end
          3'h3: out_ref <= A_reg * B_reg;
          3'h4: begin
            if (direction_reg)
              out_ref <= {out_ref[4:0], serial_in_reg};
            else
              out_ref <= {serial_in_reg, out_ref[5:1]};
          end
          3'h5: begin
            if (direction_reg)
              out_ref <= {out_ref[4:0], out_ref[5]};
            else
              out_ref <= {out_ref[0], out_ref[5:1]};
          end
        endcase
    end 
  end
end

endmodule