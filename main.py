global Done
Done = 0
def generate_operator(CookedExp):
    global Done
    identifier = CookedExp[0]
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
        elif A == "B" and B == "A":
            Done = 1
            return "00100011"
        elif A == "A" and B == "PIN":
            Done = 1
            return "01100000"
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
        if A != "A" and A != "B":
            address = A
        elif B != "A" and B != "B":
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


file = open('source', 'r')
obj = open('init.mem', 'w')
line_buffer = ""
LineCounter = 0
while True:
    LineCounter += 1
    print(LineCounter)
    line = file.readline().strip('\n')
    if not line:
        break
    else:
        CookedExp = line.split(' ')
        line_buffer += generate_operator(CookedExp)
        if Done == 1:
            Done = 0
            line_buffer += "00000000"
            obj.writelines(line_buffer)
            obj.writelines("\n")
            line_buffer = ""
            continue
        line_buffer += generate_address(CookedExp)
        obj.writelines(line_buffer)
        obj.writelines("\n")
        line_buffer = ""



