import sys
 
class Register:
    def __init__(self, type):
        self.type = type
        self.value = None
        
MAR = Register('Address')
MDR = Register('Data')
PC = Register('Address')
ACC = Register('Data')
CIR = Register('Instruction')
SR = Register('Status')

def ALU(instruction):
    eval(f'I{instruction}({ACC})')
    

main_memory = {f'{i:08b}' : '' for i in range(100)}
instruction_set = {'ADD':'0000','SUB':'0001','MOV':'0010','LDR':'0011','OUT':'0100','HAlT':'0101','BGT':'0110','BLT':'0111','BEQ':'1000','BRA':'1001','CMP':'1010','STR':'1011','BNE':'1100'}
registers = [MAR, MDR, PC, ACC, CIR, SR]

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

        
def fetch():
     
            
    
        