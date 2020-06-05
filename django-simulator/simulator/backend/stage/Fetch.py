from simulator.backend.StringOperation import*
from simulator.backend.const import*

def Fetch(now,nextp,mem):
    if  now.M["icode"] in [IJXX] and (not now.M[Cnd]):
        f_pc = now.M[valA]
    elif now.W['icode'] in [IRET] :
        f_pc = now.W[valM]
    else:
        f_pc = now.F['predPC']
#    print(f_pc,"##")
    instr = 'ff'
    try:
        instr = mem.readMemory(int ( normalize(f_pc),16),1)
    except:
        imem_error = False
    icode = instr[0]
    ifunc = instr[1]
#   print(icode ," ^^^",ifunc)

    instr_valid = False
    if instr in instrname.keys():
        instr_valid = True
    else:
        instr = 'ff' 

    need_register = icode in [IRRMOVQ, IOPQ, IPUSHQ, IPOPQ, IIRMOVQ, IRMMOVQ, IMRMOVQ,IADDQ]
    need_valC = icode in [IIRMOVQ, IRMMOVQ, IMRMOVQ, IJXX, ICALL, IADDQ]
    
    valC = vNone
    imem_error = True
#   print(int ( normalize(f_pc),16) + int(need_register) + 1,"$$$")
    if need_valC:
        try:
            valC = mem.readMemory(   int ( normalize(f_pc),16) + int(need_register) + 1 ,8)
        except:
            imem_error = False
#   hex 带0x
    valP = normalize( hex( int(normalize(f_pc),16) + 1 + 1 * int(need_register) + 8 * int(need_valC) )[2:] )

    if icode in [IJXX,ICALL]:
        predPC = valC
    else:
        predPC = valP
    
    rA = 'f'
    rB = 'f'
    if need_register:
        try:
            r = mem.readMemory((int ( normalize(f_pc),16) + 1),1)
        except:
            imem_error = False       
        rA = r[0:1]
        rB = r[1:]
#   print(r ,"%%",rB)
        
    if not imem_error:
        stat = 'ADR'
#        op.append("Error: memory address Error!")
    elif not instr_valid:
        stat = 'INS'
#        op.append("Error: instruction Error!")
    elif icode in [Halt]:
        stat = 'HLT'
#   print(stat,'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
#        op.append("Halt: Halt !")
    else:
        stat = 'AOK'
#        op.append("Move on!")
    dict = {
        'stat': stat,#string
        'icode':icode,#strign
        'instr': instr,
        'iFunc':ifunc,#string
        'rA':rA,#string
        'rB':rB,#string
        'valC':valC,#strinh
        'valP':valP#string
    }
#   print(dict)
    nextp.D.update(dict)
    nextp.F['predPC'] = predPC#string
    nextp.F["f_pc"]=f_pc
    