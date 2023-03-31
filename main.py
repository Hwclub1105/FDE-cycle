import sys
 
class Register:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Alu:
    def __init__(self):
        self.swap = 1
        self.R1 = Register('Data','')
        self.R2 = Register('Data','')
        
    def execute(self, instruction):
        eval(f'I{instruction}({ACC}, {self.value})')

def I0000(R0, R1, R2): #ADD
    R0.value = R1.value + R2.value

def I0001(R0, R1, R2): #SUB
    R0.value = R1.value - R2.value

def I0010(R0,R1): #MOV
    R0.value = R1.value

def I0011(R0, M0): #LDR
    R0.value = main_memory[M0]
    
def I0100(M0): #OUT
    print(main_memory[M0])

def I0110(branch): #BGT
    pass
        
def I0111(branch): #BLT
    pass
        
def I1000(branch): #BEQ
    pass
        
def I1010(R0,R1,temp_CMP): #CMP
    pass      
        
def I1011(R1,M1): #STR
    main_memory[M1] = registers[R1]
    
def binary(num):
    ans = ''
    while True:
        ans += str(num % 2)
        if num == 1 or num == 0:
            break
        num = num // 2
    ans = ans[::-1]
    while len(ans) < 8:
        ans = (ans[::-1]+'0')[::-1]
    return ans

def decimal(num):
    values = [(int(num[::-1][i]))*(2**i) for i in range(8)]
    return sum(values)
#main_memory = {f'{i:08b}' : i for i in range(100)}
main_memory = {'00000000': 13, '00000001': 28, '00000010': '0000', '00000011': '0100', '00000100': 4, '00000101': 5, '00000110': 6, '00000111': 7, '00001000': 8, '00001001': 9, '00001010': 10, '00001011': 11, '00001100': 12, '00001101': 13, '00001110': 14, '00001111': 15}
instruction_set = {'ADD':'0000','SUB':'0001','MOV':'0010','LDR':'0011','OUT':'0100','HAlT':'0101','BGT':'0110','BLT':'0111','BEQ':'1000','BRA':'1001','CMP':'1010','STR':'1011','BNE':'1100'}
        
MAR = Register('Address','00000000')
MDR = Register('Data','00000000')
PC = Register('Address','00000000')
ACC = Register('Data','00000000')
CIR = Register('Instruction','00000000')
SR = Register('Status','')
ALU = Alu()
        

        
def fetch():
    MAR.value = PC.value
    PC.value = binary(decimal(PC.value)+1)
    MDR.value = main_memory[MAR.value]
    print(MDR.value)
    if ALU.swap == 1:
        ALU.R1.value = MDR.value
    else:
        ALU.R2.value = MDR.value
    ALU.swap *= -1
    

fetch()
fetch(print(ALU.R2.value,ALU.R1.value))
    
print(main_memory)
     
            
    
        