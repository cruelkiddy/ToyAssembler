# ToyCompiler
A small tool for Project MCU
To Convert Assembly Language to Machine Code

### User Guide

You need to write code(more details in ***Syntax Supported***) in file "source" , 

invoke `python3 main.py`

and machine code will be generated in file "init.mem"

.mem file is used to initialize memory in Verilog by invoking `$readmemb("init.mem", rom);`, some changes should be made in the case of VHDL. 

### TODO and Limitations

- Convert C Language to Machine Code If possible 

- Support syntax in MCU3 

### Syntax Supported

The compiler supports "Assembly Like" Language,
for example:

ADD A B 

SUB A B 

MUL A B 

MOV A ADDR

Attention should be paid that there is no "," between A and B. So technically this is not Assembly Language but "Assembly Like" Language

Notice:DATA and ADDR can be written in binary(eg:0b00100000) or hexadecimal(eg:0xab). 
