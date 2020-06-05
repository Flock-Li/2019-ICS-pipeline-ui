from .const import *

ZF = 'ZF'
SF = 'SF'
OF = 'OF'
ins = 'ins'
prePC = 'prePC'
f_pc = "f_pc"
stall = 'stall'
bubble = 'bubble'
stat = 'stat'
S_tat = 'Stat'
iCode = 'iCode'
iFunc = 'iFunc'
rA = 'rA'
rB = 'rB'
valA = 'valA'
valB = 'valB'
valC = 'valC'
valP = 'valP'
valM = 'valM'
valE = 'valE'
srcA = 'srcA'
srcB = 'srcB'
dstA = 'dstA'
dstB = 'dstB'
dstE = 'dstE'
dstM = 'dstM'
Cnd = 'Cnd'

class Pipeline:
    def __init__(self):
        self.F = {
            f_pc:"00"*8,
            predPC: "00"*8,
            bubble: False,
            stall: False,
        }
        self.D = {
            stat: AOK,
            instr: '10',
            icode: NOP,
            iFunc: '0',
            rA: 'f',
            rB: 'f',
            valC: "00"*8,
            valP: "00"*8,
            bubble: False,
            stall: False,
        }
        self.E = {
            stat: AOK,
            instr: '10',
            icode: NOP,
            iFunc: '0',
            valC: vNone,
            valA: vNone,
            valB: vNone,
            dstE: 'f',
            dstM: 'f',
            srcA: 'f',
            srcB: 'f',
            bubble: False,
            stall: False,
        }
        self.M = {
            stat: AOK,
            instr: '10',
            icode: NOP,
            Cnd: int(True),
            valE: vNone,
            valA: vNone,
            dstE: 'f',
            dstM: 'f',
            bubble: False,
            stall: False,
        }

        self.W = {
            stat: AOK,
            instr: '10',
            icode: NOP,
            dstE: 'f',
            dstM: 'f',
            valE: 'f',
            valM: 'f',
            bubble: False,
            stall: False,
        }

        

