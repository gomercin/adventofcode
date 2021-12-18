import os, sys
import numpy as np
input = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    input = in_file.readlines()

#input_set = list(map(lambda x:int(x), input))

bits = ""

for ch in input[0].strip():
    d = int(ch, 16)
    b = np.base_repr(d, base=2)

    b = "0" * (4-len(b)) + b

    bits += b

print(bits)
"""
An operator packet contains one or more packets. To indicate which subsequent binary data represents its sub-packets, an operator packet can use one of two modes indicated by the bit immediately after the packet header; this is called the length type ID:

    If the length type ID is 0, then the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.
    If the length type ID is 1, then the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.

Finally, after the length type ID bit and the 15-bit or 11-bit field, the sub-packets appear.

For example, here is an operator packet (hexadecimal string 38006F45291200) with length type ID 0 that contains two sub-packets:

00111000000000000110111101000101001010010001001000000000
VVVTTTILLLLLLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBBBBBB

"""

class Package:
    def __init__(self, ci):
        self.start_index = ci
        self.version = bits[ci: ci+3]
        ci+=3
        self.typeid = bits[ci: ci+3]
        ci+=3

        if self.typeid == "100":
            val = ""
            #literal
            pstart = ci
            # print(bits)
            while True:
                # print(ci)
                if bits[ci] == '1':
                    val += bits[ci+1: ci+5]
                    # print(val)
                    ci +=5
                else:
                    # print("you are breaking my heart")
                    val += bits[ci+1: ci+5]
                    # print(val)

                    ci+=5
                    while ci %4 != 0:
                        ci+=1

                    break

            self.value = int(val, 2)
            # print(value)


        else:
            length_type_id = bits[ci]

            ci += 1
            if length_type_id == '0':
                length = int(bits[ci:ci+15], 2)

                ci += 15
                values = bits[ci: ci+length]
                ci += length
            else:
                length = int(bits[ci:ci+11], 2)

                ci += 11
                # here, continue parsing the sub packets
                # are they always literals?
                self.subpackage_count = int(length)

        self.current_counter = ci

def __part_1():
    ci = 0
    debug_str = ""

    total_version_number = 0
    while ci < len(bits):
        start=ci
        version = bits[ci:ci+3]
        debug_str += "vvv"
        ci+=3

        typeid = bits[ci: ci+3]
        debug_str += "ttt"
        ci+=3
        print(f"typeid: {typeid}")

        total_version_number += int(version)
        if typeid == "100":
            val = ""
            #literal
            pstart = ci
            # print(bits)
            while True:
                # print(ci)
                if bits[ci] == '1':
                    val += bits[ci+1: ci+5]
                    # print(val)
                    ci +=5
                    debug_str += ("#" * 5)
                else:
                    # print("you are breaking my heart")
                    val += bits[ci+1: ci+5]
                    # print(val)
                    debug_str += ("#" * 5)

                    ci+=5
                    while ci %4 != 0:
                        ci+=1
                        debug_str += "-"

                    break

            value = int(val, 2)
            # print(value)


        else:
            length_type_id = bits[ci]
            debug_str += "i"

            ci += 1
            if length_type_id == '0':
                length = int(bits[ci:ci+15], 2)
                debug_str += ("l" * 15)

                ci += 15
                values = bits[ci: ci+length]
                debug_str += "#" * length
                ci += length
            else:
                length = int(bits[ci:ci+11], 2)
                debug_str += ("l" * 11)

                ci += 11
                # here, continue parsing the sub packets
                # are they always literals?
                values = bits[ci: ci + (length * 11)]
                debug_str += "#" * length * 11

                ci += (length* 11)

        if len(bits) - ci < 10:
            break

    print(debug_str)
    print(total_version_number)

def part_2():
    pass



part_1()
part_2()