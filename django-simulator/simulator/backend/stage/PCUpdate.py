from simulator.backend.const import *
def PCUpdata(now,nextp,cpi):   
    D_bubble = False
    E_bubble = False
    M_bubble = False
    F_stall = False
    D_stall = False     
    W_stall = False
    #贼坑 
    """
    if nextp.W[stat] in [ADR, INS, HALT] or now.W[stat] in [ADR, INS, HALT]:
        M_bubble = True
        W_stall = True
    elif now.E[icode] in [IJXX] and not nextp.M[Cnd]:
        D_bubble = True
        E_bubble = True
    elif IRET in [now.D[icode], now.E[icode], now.M[icode]]:
        F_stall = True
        D_bubble =True
    elif now.E[icode] in [IMRMOVQ,IPOPQ] and ( now.E[dstM] in [nextp.E[srcA],nextp.E[srcB]]) :
        F_stall = True
        D_stall = True        
        E_bubble = True
    """
    if (IRET in [now.D[icode], now.E[icode], now.M[icode]] )\
        or( now.E[icode] in [IMRMOVQ,IPOPQ] and ( now.E[dstM] in [nextp.E[srcA],nextp.E[srcB]]) ):
        F_stall = True
    if now.E[icode] in [IMRMOVQ,IPOPQ] and ( now.E[dstM] in [nextp.E[srcA],nextp.E[srcB]]) :
        D_stall = True
    if nextp.W[stat] in [ADR, INS, HLT] or now.W[stat] in [ADR, INS, HLT]:
        W_stall = True
#   加入not D_stall
    if (not D_stall and IRET in [now.D[icode], now.E[icode], now.M[icode]] )\
        or ( now.E[icode] in [IJXX] and not nextp.M[Cnd]):
        D_bubble = True
    if (now.E[icode] in [IJXX] and not nextp.M[Cnd] ) or ( now.E[icode] in [IMRMOVQ,IPOPQ] and ( now.E[dstM] in [nextp.E[srcA],nextp.E[srcB]]) ):
        E_bubble = True
    if nextp.W[stat] in [ADR, INS, HLT] or now.W[stat] in [ADR, INS, HLT]:
        M_bubble = True
    
    

#    print(M_bubble,"****")
#   print(now.W[stat]," ",nextp.W[stat])
    

    if F_stall:
        nextp.F.update(now.F)
        nextp.F.update(**{"stall": True})
    if D_stall:
        nextp.D.update(now.D)
        nextp.D.update(**{"stall": True})
    if W_stall:
        nextp.W.update(now.W)
        nextp.W.update(**{"stall": True})


    if D_bubble:
#        cpi.num_bubble += 1
        dict = {           
            'stat':now.D[stat],
            'instr':'10',
            'icode':'1',
            'ifunc':'0',
            'rA': 'f',
            'rB': 'f',
            'valC':'0',
            'valP':'0'
        }
        nextp.D.update(dict)
#    print(cpi.num_bubble,"########")
    if E_bubble:
#        cpi.num_bubble += 1
        dict = {           
            'stat':now.D[stat],
            'instr':'10',
            'icode':'1',
            'ifunc':'0',
            'valC':'0',
            'valA':'0',
            'valB':'0',
            'dstM':'f',
            'dstE':'f',
            'srcA':'f',
            'srcB':'f'
        }
        nextp.E.update(dict)
#    print(cpi.num_bubble,"########")
    if M_bubble:
    #    cpi.num_bubble += 1
        dict = {           
            'stat':now.D[stat],
            'instr':'10',
            'icode':'1',
            'Cnd':0,
            'valE':'0',
            'valA':'0',
            'dstM':'f',
            'dstE':'f'# '0'不行
        }
        nextp.M.update(dict)
    print(cpi.num_bubble,"########")
#    print(M_bubble ,D_bubble,D_stall,F_stall, E_bubble,W_stall)
    if now.W[instr] == '10':
        cpi.num_bubble += 1
    now.F = nextp.F
    now.D = nextp.D
    now.E = nextp.E
    now.M = nextp.M
    now.W = nextp.W