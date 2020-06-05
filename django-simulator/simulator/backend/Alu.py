from .StringOperation import *

def aluxor(aluA,aluB,set_cc,cc):
    result = [0]*64
    A = tobinary(normalize(aluA))
    B = tobinary(normalize(aluB))
#    print(A,"@@",B)
    for i in range(0,64):
        result[i] = A[i] ^ B[i]
#    print(result)    
    result = reversed(result)
    A = reversed(A)
    B = reversed(B)
    
    result = "".join('%s' %i for i in result) 
#    print(hex(int(result,2)))
    A = "".join('%s' %i for i in A)
    B = "".join('%s' %i for i in B)
#    print(int(A,2),"^^^",int(B,2))
    if set_cc:
        if result == '0'*64 :
            cc.ZF = True
        else :
            cc.ZF = False

        if result[0] == '1':
            cc.SF = True
        else:
            cc.SF = False

        cc.OF = False
    
    else:
        pass

    return  hex(int(result,2))[2:]  #有时这个【2：】


def aluand(aluA,aluB,set_cc,cc):
    result = [0]*64
    A = tobinary(normalize(aluA))
    B = tobinary(normalize(aluB))
#   print(A,"@@",B)
    for i in range(0,64):
        result[i] = A[i] & B[i]
#   print(result)    
    result = reversed(result)
    A = reversed(A)
    B = reversed(B)
    
    result = "".join('%s' %i for i in result) 
#   print(hex(int(result,2)))
    A = "".join('%s' %i for i in A)
    B = "".join('%s' %i for i in B)
#   print(int(A,2),"^^^",int(B,2))
    if set_cc:
        if result == '0'*64 :
#   print(result,'****')
            cc.ZF = True
        else :
#   print(result,'****')
            cc.ZF = False

        if result[0] == '1':
            cc.SF = True
        else:
            cc.SF = False

        cc.OF = False
    
    else:
        pass

    return  hex(int(result,2))[2:] 

def aluadd(aluA,aluB,set_cc,cc):
    
    result = [0]*65
    A = tobinary(normalize(aluA))
    B = tobinary(normalize(aluB))
#    print(A,"@@",B)
    for i in range(0,64):
        result[i] += A[i] +B[i]
        if result[i] > 1:
            result[i] %= 2
            result[i+1] = 1 
     
    result = result[0:64]
#    print(result)   
    valA = tosignedint(A)
    valB = tosignedint(B)
    valr = tosignedint(result) 
    result = reversed(result)
    A = reversed(A)
    B = reversed(B)
    
    result = "".join('%s' %i for i in result) 
#   print(hex(int(result,2)))
    A = "".join('%s' %i for i in A)
    B = "".join('%s' %i for i in B)
#   print(A,"***",B)
#   print(set_cc)
    if set_cc:
        if result == '0'*64 :
          #  print(result,'****')
            cc.ZF = True
        else :
          #  print(result,'****')
            cc.ZF = False

        if result[0] == '1':
            cc.SF = True
        else:
            cc.SF = False
#   print(cc.SF)
        if (valB > 0 and valA > 0 and valr < 0  )\
           or (valB < 0 and valA < 0 and valr >= 0 ) :
            cc.OF = True
        else:
            cc.OF = False
    
    else:
        pass

    return  hex(int(result,2))[2:] 


def alusub(aluA,aluB,set_cc,cc):
    result = [0]*65
    A = tobinary(normalize(aluA))
    B = tobinary(normalize(aluB))
#    print(A,"@@",B)
    for i in range(0,64):
        
        if result[i] + B[i] - A[i] < 0:
            result[i] += 2 + B[i] - A[i]
            result[i+1] = -1 
        else:
            result[i] += B[i] - A[i]
     
    
    result = result[0:64]
#    print(result)   
    valA = tosignedint(A)
    valB = tosignedint(B)
    valr = tosignedint(result) 
    result = reversed(result)
    result = "".join('%s' %i for i in result) 
#    print(hex(int(result,2)))
    A = reversed(A)
    B = reversed(B)
    A = "".join('%s' %i for i in A)
    B = "".join('%s' %i for i in B)
#    print(int(A,2),"^^^",int(B,2))
#    print(result,"&&&&&&&&&&",type(result)) 
    if set_cc:
        
        if result == '0'*64 :
            cc.ZF = True
        else :
            cc.ZF = False

        if result[0] == '1':
            cc.SF = True
        else:
            cc.SF = False

        if (valB > 0 and valA < 0 and valr < 0 )\
          or  (valB < 0 and valA > 0 and valr >= 0) :
            cc.OF = True
        else:
            cc.OF = False
    
    else:
        pass
    return  hex(int(result,2))[2:] 
        


