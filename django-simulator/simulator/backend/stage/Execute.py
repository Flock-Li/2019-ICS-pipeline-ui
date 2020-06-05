from simulator.backend.const import *
from simulator.backend.Alu import*

def Execute(now,nextp,cc):

    if now.E[icode] in [IRRMOVQ,IOPQ]:
        ALUA = now.E[valA]
    elif now.E[icode] in [IADDQ,IIRMOVQ,IRMMOVQ,IMRMOVQ]:
        ALUA = now.E[valC]
    elif now.E[icode] in [ICALL,IPUSHQ]:
        ALUA = 'f8'+'ff'*7
    elif now.E[icode] in [IRET,IPOPQ]:
        ALUA = '08'+"00"*7
    else:
        ALUA = '00'*8

#    print(ALUA)
    ALUfun = ALUADD
    if now.E[icode] in [IOPQ]:
        ALUfun = now.E['iFunc']
    else:
        ALUfun = ALUADD
    set_cc = True
#    print(now.E[icode])
    if now.E[icode] in [IOPQ,IADDQ] and nextp.W[stat] == 'AOK' and now.W[stat] == 'AOK':
        set_cc = True
    else :
        set_cc = False
#    print(set_cc,"()()()")
    if now.E[icode] in [IADDQ,IOPQ,IRMMOVQ,IMRMOVQ,ICALL,IRET,IPUSHQ,IPOPQ]:#不用,IRRMOVQ
        ALUB = now.E[valB]
    else:
        ALUB = '00'*8

#    print(ALUB)
#不在此加入set_cc的判断
#    print(ALUfun,"((((((((((((()))))))))))))")
    if  ALUfun == ALUXOR:
        e_valE =normalize( aluxor(ALUA,ALUB,set_cc,cc)  )
    elif ALUfun == ALUSUB:
        #(ALUA,"^&",ALUB)
        e_valE =normalize( alusub(ALUA,ALUB,set_cc,cc) )
    elif ALUfun == ALUAND:
        e_valE =normalize( aluand(ALUA,ALUB,set_cc,cc) )
    else:
        e_valE =normalize( aluadd(ALUA,ALUB,set_cc,cc) )
#    print(e_valE,"********")
    Cnd = True
#    print(now.E[icode],now.E[iFunc])
    if now.E[icode] in [IJXX, IRRMOVQ]:
        if now.E[iFunc] in [jmp, rrmovq]:
#            print("*")
            Cnd = True
        elif now.E[iFunc] in [jle, cmovle] and ((cc.SF ^ cc.OF) | cc.ZF):
            Cnd = True
#            print("**")
        elif now.E[iFunc] in [jl, cmovl] and (cc.SF ^ cc.OF):
            Cnd = True
#            print("***")
        elif now.E[iFunc] in [je, cmove] and cc.ZF:
            Cnd = True
#            print("****")
        elif now.E[iFunc] in [jne, cmovne] and not cc.ZF:
            Cnd = True
#            print("*****")
        elif now.E[iFunc] in [jge, cmovge] and not (cc.SF ^ cc.OF):
            Cnd = True
#            print("******")
        elif now.E[iFunc] in [jg, cmovg] and not (cc.SF ^ cc.OF) and not cc.ZF:
            Cnd = True
#            print("*******")
        else:
            Cnd = False
#            print("********")
#    print(Cnd,"(())")
    #如果是条件跳转语句且不跳转 dstE = none
    if now.E[icode] in [IJXX, IRRMOVQ] and (not Cnd):
        e_dstE = 'f'
    else :
        e_dstE = now.E[dstE]

    dict={
        'stat': now.E[stat],
        'instr': now.E['instr'],
        'icode': now.E[icode],
        'Cnd': int(Cnd),
        'valE': e_valE,
        'valA': now.E[valA],
        'dstE': e_dstE,
        'dstM': now.E[dstM]
    }

#    print(dict)
    nextp.M.update(dict)
#    print(nextp.M["icode"],"@")