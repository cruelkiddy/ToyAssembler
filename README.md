# ToyAssembler
A small tool for Project MCU
To Convert Assembly Language to Machine Code

### User Guide

You need to write code(more detail in ***Syntax Supported***) in a file (suppose filename = “SourceCode”) , 

then invoke `python3 main.py SourceCode`

and machine code will be generated in file "init.mem"

.mem file is used to initialize memory in Verilog by invoking `$readmemb("init.mem", rom);`, some changes should be made in the case of VHDL. 

### TODO

- Convert C Language to Machine Code If possible 

- Skip Blank Line in Compilation

### Syntax Supported

The compiler supports "Assembly Like" Language,
for example:

ADD A B 

SUB A B 

MUL A B 

MOV A ADDR

Attention should be paid that there is no "," between A and B. So technically this is not Assembly Language but "Assembly Like" Language

***Comment*** should be started with "#"

***No blank line*** is allowed between valid code line

***DATA and ADDR*** can be written in binary(eg:0b00100000) or hexadecimal(eg:0xab). 
