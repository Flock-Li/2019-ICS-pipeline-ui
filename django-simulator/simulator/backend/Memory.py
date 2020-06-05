from .StringOperation import*

from .const import*

class Memory:
    
    def __init__(self):
        self.mem = ['00'] * memorysize

    def loadMemory(self,codelist):
        """
        read data from file and load it into Memory
        codelist:list
        """

        result = {}
        for line in codelist:
            s="".join(line)
            if s.startswith('0x'):
                pos1=s.find(':')
                pos2=s.find('|')
#              if pos1 != -1 and pos2 != -1 and pos1 < pos2:
                key=s[:pos1] #0x000
                value=s[pos1+2 : pos2-1]
#              print(key,"  ",value,type(key))
                result[key] = value
        for key in result.keys():
            try:
                str = key[2:] #000          
                self.writeMemory(str,result[key])               
            except Exception as e:
                print(e)
                raise Exception("Memory error in key: " + key + "val : " + result[key]) 

    def writeMemory(self, str, val):
        """
        write data in Memory 
        str:string
        val:string(小端法)
        """
        pos = int(str , 16)        
        if pos < 0 or pos + len(val)//2 >= memorysize :
            raise Exception(("Trying to write data from %d to %d" % pos, pos + len(val)))
        length = len(val)//2
        write = split(val, 2)
#       for i in range(0,length):
#            print(write[i])
        for i in range(0,length):
            if write[i] == '  ':
                self.mem[pos+i ] = "00"
            else: 
                self.mem[pos+i ] = write[i] 
#       result = self.readMemory(str,length)
#       print(result)
#       print(pos,"*",self.mem[pos:pos+length])
        
    def readMemory(self, pos, length):
        """
        read memory by dst
        pos：int in decimal
        length：int in decimal
        return result：string
        """
        if pos < 0 or pos + length >= memorysize :
            raise Exception(("Trying to write data from %d to %d" % pos, pos + length))
        result=""
        for i in range(0,length):
            result += self.mem[pos+i]
#       print(result)
        return result

    def getInfo(self):
        """
        get detail from Memory
        return ans：dict
        """
        ans = {}
        for i in range (0, memorysize, 8):
            val = ''.join(self.mem[i: i+8])
            ans[i]=val
        
        return ans
    """
    try:
        password = input("please enter your password:")
        # 输入的密码不是123456就抛出自定的的PasswordException异常
        if password != "123456":
            raise PasswordException(password)
    # 我们自定义的异常有password变量，所以我们可以直接选择把变量打印出来
    except PasswordException as e:
        print(f"PasswordException: {e.password}")
    """