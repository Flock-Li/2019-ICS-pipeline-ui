from .const import*
from .StringOperation import *

class Register:
    def __init__(self):
        self.reg = ["00"*8]*15

    def readregister(self,srcA):
        valA = '00'*8
        if srcA != 'f':
            x = int(srcA,16)
            valA = self.reg[x]
        
        return valA

    def writeregister(self,dstE,valE,dstM,valM):
        if dstE != 'f':
            self.reg[int(dstE,16)] = valE
        if dstM != 'f':
            self.reg[int(dstM,16)] = valM
        return 

    def show(self):
        ans={}
        for i in range(0,15):
            ans[registername[hex(i)]] = self.reg[i]
        return ans