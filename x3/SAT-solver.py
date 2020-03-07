from z3 import *

def is_hex(x):
    x = BV2Int(x,False)
    return Or((x == 0xA),
              (x == 0xB),
              (x == 0xC),
              (x == 0xD),
              (x == 0xE),
              (x == 0xF),
              (x == 0x0),
              (x == 0x1),
              (x == 0x2),
              (x == 0x3),
              (x == 0x4),
              (x == 0x5),
              (x == 0x6),
              (x == 0x7),
              (x == 0x8),
              (x == 0x9))

def check_digits(x):
    for i in range(0,32,4):
        hexdig = Extract(i+3,i,x)
        S.add(is_hex(hexdig))

S=Solver()
iVar4 = BitVec("arg1", 32)
iVar3 = BitVec("arg2", 32)
iVar2 = BitVec("arg3", 32) 
check_digits(iVar4)
check_digits(iVar3)
check_digits(iVar2)

# 2**32 converts to unsigned integer
S.add(((iVar4+iVar2)*2+iVar3*3)+2**32 - 1 == 0)
S.add(((iVar3+iVar4*2)*2 + iVar2*3)+2**32-1 == 0)
v3 = (iVar4*9+iVar2*7+iVar3*6)+2**32 - 1
S.add(v3 == 0)

print(S.check())
print(hex(int(S.model()[iVar4].as_string(),10)))
print(hex(int(S.model()[iVar3].as_string(),10)))
print(hex(int(S.model()[iVar2].as_string(),10)))
