from .StringOperation import*
from .const import*
from .Memory import*
from .register import *
from .Pipeline import *
from .stage.WriteBack import*
from .stage.MemoryAccess import*
from .stage.Execute import*
from .stage.Decode import*
from .stage.Fetch import*
from .stage.PCUpdate import*

mem = Memory()
reg = Register()


def init(codelist):
    global pre_reg
    global pre_mem          
    mem.loadMemory(codelist) 
    pre_mem = mem.getInfo()
    pre_reg = reg.show()


def runkernel():
    now = Pipeline()   
    ret={}
    class CondCode:
        def __init__(self):
            self.ZF = True
            self.SF = False
            self.OF = False

    class Stat:
        def __init__(self):
            self.stat = "AOK"
    
    class Cpi:
        def __init__(self):
            self.num_bubble = 0

    cc = CondCode()
    ss = Stat()
    cpi = Cpi()
    cycle = 2
    max_cycle = 200
    ret[0]={

    }
    ret[1]={

    }
    global number
    while ss.stat in ["AOK"] and cycle < max_cycle:
        
        nextp = Pipeline()
        info = {}
        info1 = {}
        info1["memory"]={}
        info1["register"]={}
        info1["condition"]={}
        WriteBack(now,nextp,reg)
        MemoryAccess(now,nextp,mem,ss)
        Execute(now,nextp,cc)
        Decode(now,nextp,reg)
        Fetch(now,nextp,mem)
        PCUpdata(now,nextp,cpi)
        
        info['ss'] = ss.__dict__
        info['cc'] = cc.__dict__

        info1['ss'] = ss.__dict__
        info1['cc'] = cc.__dict__
        info1["condition"].update(cc.__dict__)
        info1["condition"].update(ss.__dict__)
        info1["condition"].update({
            "CPI":0,
        })
        """
        print("CYCLE:",cycle,
            ";  Conditioncode:",cc.__dict__,
            ";  Stat:",ss.__dict__,
            "\n")
        """

        info['F'] = now.F
        info1['F'] = {
            "f_pc":'0x'+ normalize(info['F']['f_pc'])[13:16] ,
            "FrePC":'0x'+normalize(info['F']['predPC'])[13:16] ,
        }
        print(info1["F"])
        """
        print("F:",
            "predPC:",'0x'+deletezero( normalize(info['F']['predPC']) ),
            "\n")
        """

        info['D'] = now.D
        info1['D'] = {
            "stat":info['D']['stat'],
            "instr":instrname[ info["D"]['instr'] ],
            "icode":info['D']["icode"],
            "ifun":info['D']['iFunc'],
            "rA":registername[info['D']['rA']],
            "rB":registername[info['D']['rB']],
            "valC":"0x"+deletezero(normalize(info['D']['valC'])),
            "valP":"0x"+deletezero(normalize(info['D']['valP'])),
        }
        """
        print("D: \n"
            "stat: ",info['D']['stat'],
            "instr: ",instrname[ info["D"]['instr'] ],
            "icode: ",info['D']["icode"],
            "ifunc: ",info['D']['iFunc'],
            ";  rA = ",registername[info['D']['rA']],
            ";  rB = ",registername[info['D']['rB']],
            ";  valC = 0x"+deletezero(normalize(info['D']['valC'])),
            ";  valP = 0x"+deletezero(normalize(info['D']['valP'])),
            "\n")
        """

        info['E'] = now.E
        info1['E'] = {
            "stat":info["E"]["stat"],
            "instr":instrname[ info["E"]['instr'] ],
            "icode":info['E']["icode"],
            "ifunc":info['E']['iFunc'],
            "valC": "0x"+deletezero(normalize(info['E']['valC'])),
            "valA":"0x"+deletezero(normalize(info['E']['valA'])),
            "valB": "0x"+deletezero(normalize(info['E']['valB'])),
            "dstE":registername[info['E']['dstE']],
            "dstM":registername[info['E']['dstM']],
            "srcA":registername[info['E']['srcA']],
            "srcB":registername[info['E']['srcB']],
        }
        """
        print("E: \n"
            "stat: ",info['E']['stat'],
            "instr: ",instrname[ info["E"]['instr'] ],
            "icode: ",info['E']["icode"],
            "ifunc: ",info['E']['iFunc'],
            "valC = 0x"+deletezero(normalize(info['E']['valC'])),
            "valA = 0x"+deletezero(normalize(info['E']['valA'])),
            "valB = 0x"+deletezero(normalize(info['E']['valB'])),
            "dstE = ",registername[info['E']['dstE']],
            "dstM = ",registername[info['E']['dstM']],
            "srcA = ",registername[info['E']['srcA']],
            "srcB = ",registername[info['E']['srcB']],
            "\n"
        )
        """
        info['M'] = now.M
        info1['M'] = {
            "stat":info['M']['stat'], 
            "instr":instrname[ info["M"]['instr'] ],
            "icode":info['M']["icode"],
            "valA":"0x"+deletezero(normalize(info['M']['valA'])),
            "valE":"0x"+deletezero(normalize(info['M']['valE'])),
            "dstE":registername[info['M']['dstE']],
            "dstM":registername[info['M']['dstM']],            
            "Cnd":str(info['M']['Cnd']),
        }
        """
        print(
            "M: \n"
            "stat: ",info['M']['stat'], 
            "instr: ",instrname[ info["M"]['instr'] ],
            "icode: ",info['M']["icode"],
            "valA = 0x"+deletezero(normalize(info['M']['valA'])),
            "valE = 0x"+deletezero(normalize(info['M']['valE'])),
            "dstE = ",registername[info['M']['dstE']],
            "dstM = ",registername[info['M']['dstM']],            
            "Cnd = ",str(info['M']['Cnd']),
            "\n"
        )
        """
        info['W'] = now.W
        info1["W"] = {
            "stat":info['W']['stat'], 
            "instr":instrname[ info["W"]['instr'] ],
            "icode":info['W']["icode"],
            "valE":"0x"+deletezero(normalize(info['W']['valE'])),
            "valM":"0x"+deletezero(normalize(info['W']['valM'])),
            "dstE":registername[info['W']['dstE']],
            "dstM":registername[info['W']['dstM']],
        }
        """
        print(
            "W: \n"
            "stat: ",info['W']['stat'], 
            "instr: ",instrname[ info["W"]['instr'] ],
            "icode: ",info['W']["icode"],
            "valE = 0x"+deletezero(normalize(info['W']['valE'])),
            "valM = 0x"+deletezero(normalize(info['W']['valM'])),
            "dstE = ",registername[info['W']['dstE']],
            "dstM = ",registername[info['W']['dstM']],                       
            "\n"
        )
        """
        REGISTER = reg.show()        
        MEMORY = mem.getInfo()
        for i in range(0,15):
            x=registername[hex(i)]
            info1["register"][x] = "0x"+normalize(REGISTER[registername[hex(i)]])
        for key in MEMORY.keys():
            x=hex(key)
            dict = {x:"0x"+normalize(MEMORY[key])}
            info1["memory"].update(dict) 
        ret[cycle] = info1
        cycle += 1
    ret[cycle-1]["condition"]["CPI"]=round( (cycle-3)/(cycle-3-(cpi.num_bubble-4)) , 2)
    for i in range(2,cycle-2):
        ret[i]["condition"]["stat"]="AOK"
    ret[cycle-1]["condition"]["stat"]="HLT"
    initial={}
    initial["register"]={}
    initial["memory"]={}
    for i in range(0,15):
        x=registername[hex(i)]
        initial["register"][x] = "0x"+"0000000000000000"
    for key in MEMORY.keys():
        x=hex(key)
        dict = {x:"0x"+"0000000000000000"}
        initial["memory"].update(dict) 
    initial["condition"]={
        "ZF": "true",
        "SF": "false",
        "OF": 'false',
        "stat": "AOK",
        "CPI": 0
    }
    initial["ss"]={
        "stat": "AOK"
    }
    initial["cc"]={
        "ZF": "true",
        "SF": "false",
        "OF": "false",
    }
    initial["F"]={
        "f_pc":"0x000",
        "FrePC": "0x000"
    }
    initial["D"]={
        "stat": "AOK",
        "instr": "NOP",
        "icode": "1",
        "ifun": "0",
        "rA": "null",
        "rB": "null",
        "valC": "0x0",
        "valP": "0x0"
    }
    initial["E"]={
        "stat": "AOK",
        "instr": "NOP",
        "icode": "1",
        "ifunc": "0",
        "valC": "0x0",
        "valA": "0x0",
        "valB": "0x0",
        "dstE": "null",
        "dstM": "null",
        "srcA": "null",
        "srcB": "null"
    }
    initial["M"]={
        "stat": "AOK",
        "instr": "NOP",
        "icode": "1",
        "valA": "0x0",
        "valE": "0x0",
        "dstE": "null",
        "dstM": "null",
        "Cnd": "1"     
    }
    initial["W"]={
        "stat": "AOK",
        "instr": "NOP",
        "icode": "1",
        "valE": "0x0",
        "valM": "0x0",
        "dstE": "null",
        "dstM": "null"
    }
    ret[0]=initial
    ret[1]=initial

    # info1["CPI"]=round( (cycle-3)/(cycle-3-(cpi.num_bubble-4)) , 2) 
    # REGISTER = reg.show()        
    # MEMORY = mem.getInfo()
#    print(cycle,cpi.num_bubble)
    # print("Changed Register State: \n")

    # for i in range(0,15):
    #     if (REGISTER[registername[hex(i)]] != pre_reg[registername[hex(i)]]):
    #         print(registername[hex(i)]," : ","0x"+pre_reg[registername[hex(i)]],"-->","0x"+normalize(REGISTER[registername[hex(i)]]))
        
    # print("Changed Memory State:   \n")

    # for key in MEMORY.keys():
    #     if MEMORY[key] != pre_mem[key]:
    #         print(hex(key), ": ", "0x"+normalize(pre_mem[key]), "-->", "0x"+normalize( MEMORY[key] ) )

    # print("CPI: "+str(cycle-3)+' cycles/'+str(cycle-3-(cpi.num_bubble-4))
    #     +' instructions =',round( (cycle-3)/(cycle-3-(cpi.num_bubble-4)) , 2) )

    return ret
