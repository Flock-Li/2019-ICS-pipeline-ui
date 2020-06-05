import os

pwd = os.getcwd() #获取当前工作目录路径
# os.path.abspath('.') #获取当前工作目录路径
#为什么是//
"""
f0=open(pwd+"\y86-code\\"+"prog1.yo","r").readlines()
f1=open(pwd+"\y86-code\\"+"prog2.yo","r").readlines()
f2=open(pwd+"\y86-code\\"+"prog3.yo","r").readlines()
f3=open(pwd+"\y86-code\\"+"prog4.yo","r").readlines()
f4=open(pwd+"\y86-code\\"+"prog5.yo","r").readlines()
f5=open(pwd+"\y86-code\\"+"prog6.yo","r").readlines()
f6=open(pwd+"\y86-code\\"+"prog7.yo","r").readlines()
f7=open(pwd+"\y86-code\\"+"prog8.yo","r").readlines()
f8=open(pwd+"\y86-code\\"+"prog9.yo","r").readlines()
f9=open(pwd+"\y86-code\\"+"prog10.yo","r").readlines()

f10=open(pwd+"\y86-code\\"+"pushquestion.yo","r").readlines()
f11=open(pwd+"\y86-code\\"+"pushtest.yo","r").readlines()
f12=open(pwd+"\y86-code\\"+"ret-hazard.yo","r").readlines()
f13=open(pwd+"\y86-code\\"+"abs-asum-cmov.yo","r").readlines()
f14=open(pwd+"\y86-code\\"+"abs-asum-jmp.yo","r").readlines()
f15=open(pwd+"\y86-code\\"+"asum.yo","r").readlines()
f16=open(pwd+"\y86-code\\"+"asumi.yo","r").readlines()
f17=open(pwd+"\y86-code\\"+"asumr.yo","r").readlines()
f18=open(pwd+"\y86-code\\"+"cjr.yo","r").readlines()
f19=open(pwd+"\y86-code\\"+"j-cc.yo","r").readlines()
"""
number = 0

RRSP = '4'

INS = 'INS'
ADR = 'ADR'
AOK = 'AOK'
HLT = 'HLT'


dstM = 'dstM'
dstE = 'dstE'
valM = 'valM'
valE = 'valE'
valC = 'valC'
valP = 'valP'
valA = 'valA'
valB = 'valB'
stat = 'stat'
srcA = 'srcA'
srcB = 'srcB'
instr = 'instr'
icode = 'icode'
iFunc = 'iFunc'
ifunc = 'ifunc'
Cnd = 'Cnd'
predPC = 'predPC'
rA = 'rA'
rB = 'rB'

ALUADD = '0'
ALUSUB = '1'
ALUAND = '2'
ALUXOR = '3'

#register name
registername = {
    '0x0': '%rax',
    '0x1': '%rcx',
    '0x2': '%rdx',
    '0x3': '%rbx',
    '0x4': '%rsp',
    '0x5': '%rbp',
    '0x6': '%rsi',
    '0x7': '%rdi',
    '0x8': '%r8',
    '0x9': '%r9',
    '0xa': '%r10',
    '0xb': '%r11',
    '0xc': '%r12',
    '0xd': '%r13',
    '0xe': '%r14',
    '0xf': 'null',

    '0': '%rax',
    '1': '%rcx',
    '2': '%rdx',
    '3': '%rbx',
    '4': '%rsp',
    '5': '%rbp',
    '6': '%rsi',
    '7': '%rdi',
    '8': '%r8',
    '9': '%r9',
    'a': '%r10',
    'b': '%r11',
    'c': '%r12',
    'd': '%r13',
    'e': '%r14',
    'f': 'null'
}

#memory
memorysize = 1<<10
cachesize = 1<<6

vNone="00"*8

instrname = {
    '00':'HALT',
    '10':'NOP',
    '20':'IRRMOVQ',
    '21':'ICMOVLE',
    '22':'ICMOVL',
    '23':'ICMOVE',
    '24':'ICMOVNE',
    '25':'ICMOVGE',
    '26':'ICMOVG',
    '30':'IIRMOVQ',
    '40':'IRMMOVQ',
    '50':'IMRMOVQ',
    '60':'addq',
    '61':'subq',
    '62':'andq',
    '63':'xorq',
    '70':'jmp',
    '71':'jle',
    '72':'jl',
    '73':'je',  
    '74':'jne',
    '75':'jge',
    '76':'jg',
    '80':'ICALL',
    '90':'IRET',
    'a0':'IPUSHQ',
    'b0':'IPOPQ',
    'c0':"IADDQ",
    'ff':'Invalid_instr'
}

Halt = '0'
NOP = '1'
IRRMOVQ = '2'
IIRMOVQ = '3'
IRMMOVQ = '4'
IMRMOVQ = '5'
IOPQ = '6'
IJXX = '7'
ICALL = '8'
IRET = '9'
IPUSHQ = 'a'
IPOPQ = 'b'
IADDQ = 'c'

jmp = '0'
jle = '1'
jl = '2'
je = '3'
jne = '4'
jge = '5'
jg = '6'

rrmovq = '0'
cmovle = '1'
cmovl = '2'
cmove = '3'
cmovne = '4'
cmovge = '5'
cmovg = '6'