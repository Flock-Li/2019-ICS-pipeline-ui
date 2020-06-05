from .const import *

def normalize(s):
    result = s
    result = "0" * (16 - len(result)) + result
    return ''.join(reversed(split(result,2)))

def split(s,length):
    return [s[i:i+length] for i in range(0,len(s),length)]

def tobinary(s):
    s = int(s,16)#无符号转换
    result = [0]*64
    cnt = 0
    while s:
        result[cnt] = s%2
        s //= 2
        cnt += 1
    return result

def tosignedint(s):
    val = 0
    ans = 1
    for i in range(0,64):
        val += ans* int(s[i])
        ans *= 2
    if int(s[0]) == 1 :
        val -= ans
    return val

def deletezero(s):
    for i in range(0,len(s)-1):
        if s[i] != '0':
            break
    if s[i] == '0':
        s = ''.join(s[i+1:])
    else:
        s = ''.join(s[i:])
    return s

