import os, sys

input = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    input = in_file.readlines()

dmap = {}
dmap[2] = 1
dmap[4] = 4
dmap[3] = 7
dmap[7] = 8

nmap = {}
nmap[0] = "a,b,c,e,f,g".split(',')
nmap[1] = "c,f".split(',')
nmap[2] = "a,c,d,e,g".split(',')
nmap[3] = "a,c,d,f,g".split(',')
nmap[4] = "b,c,d,f".split(',')
nmap[5] = "a,b,d,f,g".split(',')
nmap[6] = "a,b,d,e,f,g".split(',')
nmap[7] = "a,c,f".split(',')
nmap[8] = "a,b,c,d,e,f,g".split(',')
nmap[9] = "a,b,c,d,f,g".split(',')


pmap = {}
pmap[2] = [1]
pmap[3] = [7]
pmap[4] = [4]
pmap[5] = [2, 3, 5]
pmap[6] = [0, 6, 9]
pmap[7] = [8]
"""
length 5 ise:
ab d fg -> 5
a cde g
a cd fg

abc efg
ab defg
abcd fg

cdef

ded1
kural:

1: acdeg
4: bcdf
7: acf

x: 2 ile 7'nin kesisimi: a c
c: ac ile 4'un kesisimi
a: ac ile 4'un kesisiminden artan

b: 2 ile 7'nin birlesimininde olup 4'te olmayan

d: 2 ile 4'un kesisimi: a, d, bunlardan 7'de olmayan

e ve g ihtimalleri: 2'de bilmediklerimiz

6 harflilerden abcd iceren 9'dur, diger iki harf: f, g
g: bunun 2'den artanla kesisimi g
oteki de f
geriye kalan da e

1: cf
4: bcdf
7: acf

a: 7'de olup 1'de olmayan
"""



def part_1():
    count = 0
    for line in input:
        ps = line.split('|')
        left = ps[0]
        right = ps[1]

        segments = right.strip().split()

        for s in segments:
            if len(s) in dmap:
                count += 1

    print(count)
            
def map_numbers():
    pass

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def inanotinb(a, b):
    l = []

    for ch in a:
        if ch not in b:
            l.append(ch)

    return l

def part_2():

    total = 0
    for line in input:
        ps = line.split('|')
        left = ps[0]
        right = ps[1]

        signals = left.strip().split()
        segments = right.strip().split()

        letter_map = {}
        smap = {}
        nummap = {}
        for s in signals:
            if len(s) in dmap:
                smap[s] = dmap[len(s)]
                nummap[dmap[len(s)]] = list(s)
        
                
        a = inanotinb(nummap[7], nummap[1])[0]
        letter_map['a'] = a

        b_or_d = inanotinb(nummap[4], nummap[1] + nummap[7])
        e_or_g = inanotinb(list("abcdefg"), nummap[4] + nummap[1] + nummap[7]) 
        c_or_f = nummap[1]
        
        # length 5 olanlardaki tek sayidakiler: b_or_e 
        fivecounts = {}
        for s in signals:
            if len(s) != 5: continue
            for ch in s:
                if ch not in fivecounts:
                    fivecounts[ch] = 0
                fivecounts[ch] += 1
        
        b_or_e = []
        for k, v in fivecounts.items():
            if v == 1:
                b_or_e.append(k)

        c_or_e_or_d = []
        sixcounts = {}
        for s in signals:
            if len(s) != 6: continue
            for ch in s:
                if ch not in sixcounts:
                    sixcounts[ch] = 0
                sixcounts[ch] += 1

        for k, v in sixcounts.items():
            if v == 2:
                c_or_e_or_d.append(k)

        b = intersection(b_or_d, b_or_e)[0]
        d = inanotinb(b_or_d, [b])[0]

        c_or_e_or_d.remove(d)
        c_or_e = c_or_e_or_d

        c = intersection(c_or_e, c_or_f)[0]
        e = inanotinb(c_or_e, [c])[0]
        f = inanotinb(c_or_f, [c])[0]
        g = inanotinb(e_or_g, [e])[0]

        print(a, b, c,d,e,f,g)

        ofmap = {}
        ofmap[a] = 'a'
        ofmap[b] = 'b'
        ofmap[c] = 'c'
        ofmap[d] = 'd'
        ofmap[e] = 'e'
        ofmap[f] = 'f'
        ofmap[g] = 'g'

        print(ofmap)

        def rename_digit(dig):
            new_dig = ""

            for ch in dig:
                new_dig += ofmap[ch]

            return new_dig


        digmap = {}
        digmap["abcefg"] = 0
        digmap["cf"] = 1
        digmap["acdeg"] = 2
        digmap["acdfg"] = 3
        digmap["bcdf"] = 4
        digmap["abdfg"] = 5
        digmap["abdefg"] = 6
        digmap["acf"] = 7
        digmap["abcdefg"] = 8
        digmap["abcdfg"] = 9


        num = ""
        for s in segments:
            fixed = ''.join(sorted(rename_digit(s)))

            dig = digmap[fixed]

            num += str(dig)
        print(num)
        total += int(num)

    print(total)

part_1()
part_2()