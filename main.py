import sys
sourceFile = sys.argv[1]
global Done
global TotallyDone
Done = 0
TotallyDone = 0
def generate_operator(CookedExp):
    global Done
    global TotallyDone
    identifier = CookedExp[0]
    if identifier == "SETP":
        TotallyDone = 1
        return "1000000000010000"
    elif identifier == "CLRP":
        TotallyDone = 1
        return "1000000000010001"
    elif identifier == "RETI":
        TotallyDone = 1
        return "1000000000001010" 
    A = CookedExp[1]
    if identifier == "ADD":
        Done = 1
        return "00000001"
    elif identifier == "SUB":
        Done = 1
        return "00000010"
    elif identifier == "MUL":
        Done = 1
        return "00000011"
    elif identifier == "DIV":
        Done = 1
        return "00000100"
    elif identifier == "AND":
        Done = 1
        return "00000101"
    elif identifier == "OR":
        Done = 1
        return "00000110"
    elif identifier == "NOT":
        Done = 1
        return "00000111"
    elif identifier == "SHL":
        Done = 1
        return "00001000"
    elif identifier == "SHR":
        Done = 1
        return "00001001"
    elif identifier == "MOV":
        B = CookedExp[2]
        if A == "A" and B == "B":
            Done = 1
            return "00100010"
        elif A == "TDI" and B == "A":
            TotallyDone = 1
            return "1000000000000000"
        elif A == "TC" and B == "A":
            TotallyDone = 1
            return "1000000000000001"
        elif A == "A" and B == "TDO":
            TotallyDone = 1
            return "1000000000000010"
        elif A == "INTR" and B == "A":
            TotallyDone = 1
            return "1000000000001000"
        elif A == "A" and B == "INTR":
            TotallyDone = 1
            return "1000000000001001" 
        elif A == "B" and B == "A":
            Done = 1
            return "00100011"
        elif A == "A" and B == "PIN":
            Done = 1
            return "01100000"
        elif A == "A" and B == "HA":
            Done = 1
            return "00100110"
        elif B == "A" and A == "POUT":
            Done = 1
            return "01100001"
        elif A == "A" and B == "HA":
            Done = 1
            return "00100110"
        elif A == "A" and B != "B":
            return "00100000"
        elif B == "A" and A != "B":
            return "00100001"
        elif A == "AH":
            return "00100100"
        elif A == "AL":
            return "00100101"
        elif A == "BL":
            return "00101101"
    elif identifier == "JZ":
        return "01000000"
    elif identifier == "JAB":
        return "01000001"
    elif identifier == "JDB":
        return "01000010"
    elif identifier == "AJMP":
        return "01000011"           
    else:
        print("Operator Error")
        exit(0)
def generate_address(CookedExp):
    address = ""
    A = CookedExp[1]
    if CookedExp[0] == "MOV":
        B = CookedExp[2]
        if A != "A" and A != "B" and A != "AH" and A != "AL" and A != "BL":
            address = A
        elif B != "A" and B != "B" and B != "HA":
            address = B
        else:
            print("MOV Error")
            exit(1)
    else:
        address = A
    prefix = address[0:2]
    if prefix == "0b":
        return address[2:].zfill(8)
    elif prefix == "0x":
        num = int(address[2:], 16)
        return str(bin(num))[2:].zfill(8)


file = open(sourceFile, 'r')
obj = open('init.mem', 'w')
line_buffer = ""
LineCounter = 0
while True:
    LineCounter += 1
    print("Parsing Line {line_number} : ".format(line_number=str(LineCounter)), end="")
    line = file.readline().strip('\n')
    if not line:
        break
    else:
        if line[0] == "#": # Support Comment in source
            print("")
            continue
        CookedExp = line.split(' ')
        line_buffer += generate_operator(CookedExp)
        if TotallyDone == 1:
            TotallyDone = 0
            obj.writelines(line_buffer)
            obj.writelines("\n")
            print("{content}".format(content=str(hex(int(line_buffer, 2)))))
            line_buffer = ""
            continue  
        if Done == 1:
            Done = 0
            line_buffer += "00000000"
            obj.writelines(line_buffer)
            obj.writelines("\n")
            print("{content}".format(content=str(hex(int(line_buffer, 2)))))
            line_buffer = ""
            continue          
        line_buffer += generate_address(CookedExp)
        obj.writelines(line_buffer)
        obj.writelines("\n")
        print("{content}".format(content=str(hex(int(line_buffer, 2)))))
        line_buffer = ""
print("Compilation Done!")
file.close()
obj.close()



