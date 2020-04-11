from z3 import *

s = Solver()

input = BitVec("input", 8*26)

for i in range(0,8*26, 8):
    val = Extract(i+7,i,input)
    s.add(And(val >= 97,
          val <= 122))

#['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
rules=['0','0','1','00','01','10','11','000','001','010','011','100','101','110','111','0000','0001','0010','0011','0100',
       '0101','0110','0111','1000','1001','1010']#,'1011']
# rules len = 26

first_char = Extract(7,0,input)
second_char = Extract(15,8,input)
third_char = Extract(23,16,input)
s.add(first_char>second_char)
s.add(first_char<third_char)
for i in rules[3:]:
    k=rules.index(i)
    x=len(i)-1
    current_highest_bit = (rules.index(i)+1)*8 - 1
    val = Extract(current_highest_bit,current_highest_bit-7, input)
    while x!=-1:
        curr_move = i[x]
        if curr_move == '1':
            k -= 2
            k /= 2
            k = int(k)
            if(k == 0):
                prev_val = first_char
            else:
                prev_val = Extract((k+1) * 8 - 1, (k+1) * 8 - 8, input)
            s.add(val > prev_val)
        else:
            k -= 1
            k /= 2
            k = int(k)
            if k==0:
                prev_val = first_char
            else:
                prev_val = Extract((k+1) * 8 - 1, (k+1) * 8 - 8, input)
            s.add(val < prev_val)
        x-=1
input_str=""
print(s.check())
ans = s.model()
print(ans[input].as_long())
ans = hex(int(ans[input].as_string(),10))[2:]

for i in range(0,len(ans),2):
    input_str+=chr(int(ans[i]+ans[i+1],16))

print(input_str[::-1])
