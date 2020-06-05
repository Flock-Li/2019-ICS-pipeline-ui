from simulator.backend.StringOperation import *
from simulator.backend.Memory import*
from simulator.backend.const import*
from simulator.backend.Pipeline import*


def MemoryAccess(now, nextp,mem, ss):
    if now.M[icode] in [IRMMOVQ,IPUSHQ,ICALL,IMRMOVQ]:
        Addr = now.M[valE]
#   print( now.M[valE])
    elif now.M[icode] in [IPOPQ,IRET]:  #M 和 W 艹
        Addr = now.M[valA]
    else:
        Addr = "00"*8
#   print(Addr,mem.readMemory(int( normalize(Addr),16),8))
    if now.M[icode] in [IMRMOVQ,IPOPQ,IRET]:
        Mem_read = True
    else:
        Mem_read = False

    if now.M[icode] in [IRMMOVQ,IPUSHQ,ICALL]:
        Mem_write = True
    else:
        Mem_write = False

    m_valM = vNone
    dmem_error = True
    if Mem_read:
        try:
            m_valM = mem.readMemory(int( normalize(Addr),16),8)
        except:
            dmem_error = False
            m_valM = vNone
#   print(Addr," ",now.M[valA])
    
    if Mem_write:
        try:
#   print(dmem_error)
            mem.writeMemory(normalize(Addr),now.M[valA])
        except:
            dmem_error = False
#   print(dmem_error)
    if dmem_error == False:
        m_stat = 'ADR'
    else:
        m_stat = now.M[stat]

    ss.stat = m_stat

    dict = {
        stat:m_stat,
        instr: now.M['instr'],
        icode:now.M[icode],
        dstE:now.M[dstE],
        dstM:now.M[dstM],
        valE:now.M[valE],
        valM:m_valM
    }
    nextp.W.update(dict)