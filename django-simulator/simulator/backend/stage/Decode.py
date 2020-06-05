from simulator.backend.StringOperation import *
from simulator.backend.const import*


def Decode(now, nextp, reg):
    d_srcA = 'f'
#    print(now.D['icode'],"**")
    if now.D['icode'] in [IRRMOVQ,IRMMOVQ,IOPQ,IPUSHQ]:#不需要mrmovq
        d_srcA = now.D['rA']
    elif now.D['icode'] in [IPOPQ,IRET]:
        d_srcA = RRSP
    else :
        d_srcA = 'f'

    d_srcB = 'f'
#   print(now.D['icode'],"**")
    if now.D['icode'] in [IADDQ,IOPQ,IRMMOVQ,IMRMOVQ]:#不需要irmovq,,IRRMOVQ
#   print("$$$",d_srcB,"&&&&&&&&&&&&&&&&&&")
        d_srcB = now.D['rB']
    elif now.D['icode'] in [IPUSHQ,IPOPQ,ICALL,IRET]:
     #   print("***",d_srcB,"&&&&&&&&&&&&&&&&&&")
        d_srcB = RRSP
    else:        
        d_srcB ='f'

#   print("***",d_srcB,"&&&&&&&&&&&&&&&&&&")

    if now.D['icode'] in [IADDQ,IRRMOVQ,IIRMOVQ,IOPQ]:
        d_dstE = now.D['rB']
    elif now.D['icode'] in [IPUSHQ,IPOPQ,ICALL,IRET]:
        d_dstE = RRSP
    else:
        d_dstE = 'f'

    if now.D['icode'] in [IMRMOVQ,IPOPQ]:
        d_dstM = now.D['rA']
    else:
        d_dstM = 'f'
#   pop rsp 先dstM 再dstE
    d_valA = "00"*8
    d_valB = "00"*8
    if now.D['icode'] in [ICALL,IJXX]:
        d_valA = now.D['valP']

    elif d_srcA == nextp.M[dstE] :
        d_valA = nextp.M[valE]

    elif d_srcA == now.M[dstM] :
        d_valA = nextp.W[valM]

    elif d_srcA == now.M[dstE] :
        d_valA = now.M[valE]

    elif d_srcA == now.W[dstM] :
        d_valA = now.W[valM]

    elif d_srcA == now.W[dstE] :
        d_valA = now.W[valE]

    elif d_srcA != 'f' :
        d_valA = reg.reg[int(d_srcA,16)]
#    print(reg.readregister(d_srcB),"&&&&&&&&&")
#    print(d_srcB,"#",now.M[dstM])
    if d_srcB == nextp.M[dstE] :
#        print(d_valB,"&&",nextp.M[valE])
        d_valB = nextp.M[valE]

    elif d_srcB == now.M[dstM] :
        
        d_valB = nextp.W[valM]

    elif d_srcB == now.M[dstE] :
        d_valB = now.M[valE]

    elif d_srcB == now.W[dstM] :
        d_valB = now.W[valM]

    elif d_srcB == now.W[dstE] :
        d_valB = now.W[valE]

    elif d_srcB != 'f' :
        d_valB = reg.readregister(d_srcB)
        
   # print(reg.readregister('7'),"^^^^^^^^^6")
    #print(reg.readregister('6'),"^^^^^^^^^6")
#    print(d_valB,"&&",nextp.W[valM])
    dict = {
        'stat': now.D['stat'],
        'instr': now.D['instr'],
        'icode': now.D['icode'],
        'iFunc': now.D['iFunc'],
        'valC': now.D['valC'],
        'valA': d_valA,
        'valB': d_valB,
        'dstE': d_dstE,
        'dstM': d_dstM,
        'srcA': d_srcA,
        'srcB': d_srcB
    }

    nextp.E.update(dict)



