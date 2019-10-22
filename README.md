# ToyCompiler
A small tool for Project MCU
To
Convert Assembly Language to Machine Code

You need to write code in file "source" , and machine code will be generated in file "init.mem"

Will Do
Convert C Language to Machine Code 
If possible 

The compiler supports "Assembly Like" Language, all possibilities are listed below:

| ADD A B   |  SUB A B |     MUL A B |
| DIV A B    | AND A B   |  OR A B  |
| NOT A       | SHL A |       SHR A |
| MOV A ADDR | MOV ADDR A | MOV A B |
| MOV B A   | MOV AH DATA   | MOV AL DATA |
| MOV BL DATA |   MOV A HA |   JZ ADDR |
| JAB ADDR   | JDB ADDR    | AJMP ADDR |
| MOV A PIN   | MOV POUT A | --- |


Notice:DATA and ADDR can be written in binary(eg:0b00100000) or hexadecimal(eg:0xab)

