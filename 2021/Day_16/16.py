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
hamsterz0_input = \
'''E0529D18025800ABCA6996534CB22E4C00FB48E233BAEC947A8AA010CE1249DB51A02CC7DB67EF33D4002AE6ACDC40101CF0449AE4D9E4C071802D400F84BD21CAF3C8F2C35295EF3E0A600848F77893360066C200F476841040401C88908A19B001FD35CCF0B40012992AC81E3B980553659366736653A931018027C87332011E2771FFC3CEEC0630A80126007B0152E2005280186004101060C03C0200DA66006B8018200538012C01F3300660401433801A6007380132DD993100A4DC01AB0803B1FE2343500042E24C338B33F5852C3E002749803B0422EC782004221A41A8CE600EC2F8F11FD0037196CF19A67AA926892D2C643675A0C013C00CC0401F82F1BA168803510E3942E969C389C40193CFD27C32E005F271CE4B95906C151003A7BD229300362D1802727056C00556769101921F200AC74015960E97EC3F2D03C2430046C0119A3E9A3F95FD3AFE40132CEC52F4017995D9993A90060729EFCA52D3168021223F2236600ECC874E10CC1F9802F3A71C00964EC46E6580402291FE59E0FCF2B4EC31C9C7A6860094B2C4D2E880592F1AD7782992D204A82C954EA5A52E8030064D02A6C1E4EA852FE83D49CB4AE4020CD80272D3B4AA552D3B4AA5B356F77BF1630056C0119FF16C5192901CEDFB77A200E9E65EAC01693C0BCA76FEBE73487CC64DEC804659274A00CDC401F8B51CE3F8803B05217C2E40041A72E2516A663F119AC72250A00F44A98893C453005E57415A00BCD5F1DD66F3448D2600AC66F005246500C9194039C01986B317CDB10890C94BF68E6DF950C0802B09496E8A3600BCB15CA44425279539B089EB7774DDA33642012DA6B1E15B005C0010C8C917A2B880391160944D30074401D845172180803D1AA3045F00042630C5B866200CC2A9A5091C43BBD964D7F5D8914B46F040
'''
version = 0

def parse(binary):
    global version
    version += int(binary[:3],2)
    binary = binary[3:]
    type = int(binary[:3],2)
    binary = binary[3:]
    if type == 4:
        for i in range(0,len(binary),5):
            if binary[i] == '0':
                return binary[i+5:]
    else:
        length = binary[0]
        binary = binary[1:]
        if length == '0':
            length_sub_pkts=int(binary[:15],2)
            binary = binary[15:]
            sub_pkts = binary[:length_sub_pkts]
            binary = binary[length_sub_pkts:]
            while sub_pkts:
                sub_pkts = parse(sub_pkts)
            return binary
        else:
            num_of_sub_pkts=int(binary[:11],2)
            binary = binary[11:]
            for i in range(num_of_sub_pkts) :
                binary = parse(binary)
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
        if length == '0':
            length_sub_pkts=int(binary[:15],2)
            binary = binary[15:]
            sub_pkts = binary[:length_sub_pkts]
            binary = binary[length_sub_pkts:]
            x = []
            while sub_pkts:
                sub_pkts,s = parse_2(sub_pkts)
                x.append(s)
        else:
            num_of_sub_pkts=int(binary[:11],2)
            binary = binary[11:]
            x = []
            for i in range(num_of_sub_pkts) :
                binary,s = parse_2(binary)
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
    linesTest = hamsterz0_input.splitlines()[0]
    solve_1(linesTest)
    solve_2(linesTest)