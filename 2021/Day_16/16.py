import os
import copy
import collections

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''D2FE28
'''
test_input_2 = \
'''A0016C880162017C3686B18A3D4780
'''
def hexToBin(lines):
    d = {}
    for i in range(16):
        bin_key = f'{i:04b}'
        if i < 10:
            d[str(i)] = bin_key
        else:
            key = chr(i - 10 + ord('A'))
            d[key] = bin_key
    binary = ''
    for hex in lines:
        binary += d[hex]
    return binary

version = 0

def parse(binary):
    global version
    version += int(binary[:3],2)
    binary = binary[3:]
    type = int(binary[:3],2)
    binary = binary[3:]
    if type == 4:
        for i in range(0,len(binary),5):
            if binary[i] == "0":
                return binary[i+5:]
    else:
        length = binary[0]
        binary = binary[1:]
        if length == "1":
            pkts=int(binary[:11],2)
            binary = binary[11:]
            for i in range(pkts) :
                binary = parse(binary)
            return binary
        else:
            pkts=int(binary[:15],2)
            binary = binary[15:]
            sub_pkts = binary[:pkts]
            binary = binary[pkts:]
            while sub_pkts:
                sub_pkts = parse(sub_pkts)
            return binary

def parse_2(binary):
    binary = binary[3:]
    type = int(binary[:3],2)
    binary = binary[3:]
    if type == 4:
        x = ""
        for i in range(0,len(binary),5):
            x += binary[i+1:i+5]
            if binary[i] == '0':
                binary = binary[i+5:]
                break
        x = int(x,2)
        return binary,x
    else:
        length = binary[0]
        binary = binary[1:]
        if length == "1":
            pkts=int(binary[:11],2)
            binary = binary[11:]
            x = []
            for i in range(pkts) :
                binary,s = parse_2(binary)
                x.append(s)
        else:
            pkts=int(binary[:15],2)
            binary = binary[15:]
            sub_pkts = binary[:pkts]
            binary = binary[pkts:]
            x = []
            while sub_pkts:
                sub_pkts,s = parse_2(sub_pkts)
                x.append(s)
        
        if type == 0:
            return binary,sum(x)
        elif type == 1:
            val = 1
            for v in x:
                val*=v
            return binary,val
        elif type == 2:
            return binary,min(x)
        elif type == 3:
            return binary,max(x)
        elif type == 5:
            return binary, 1 if (x[0] > x[1]) else 0
        elif type == 6:
            return binary, 1 if (x[0] < x[1]) else 0
        elif type == 7:
            return binary, 1 if (x[0] == x[1]) else 0


def solve_1(lines):
    global version
    # Stackoverflow gg!
    binary = (bin(int(lines,16)))[2:].zfill(len(lines)*4)
    parse(binary)
    print(version)

def solve_2(lines):
    # Stackoverflow gg!
    binary = (bin(int(lines,16)))[2:].zfill(len(lines)*4)
    print(parse_2(binary)[1])

if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()[0]
    linesTest = test_input_2.splitlines()[0]
    solve_1(lines)
    solve_2(lines)