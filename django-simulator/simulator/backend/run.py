from .cpu import*
import json
import sys

def run(file):
    print(file,"***")
    codelist = open(pwd+"\simulator\\backend\\y86-code\\"+file,'r').readlines()
#    codelist = open((pwd+str(argv),'r').readlines()  
    init(codelist)
    res=runkernel()
    with open(pwd+"\show.json",'w') as f:
        json.dump(res,f,indent = 4)
    return 
#    f=open(os.path.dirname(pwd)+"\Y86-64_simulator\\"+"prof1.txt","w")
#    res = str(res).replace("\r\n","\\r\\n")
#    f.write(json.dumps(res))
    """
    # 写入 JSON 数据
    with open('data.json', 'w') as f:
    json.dump(data, f)
    # 读取数据
    with open('data.json', 'r') as f:
    data = json.load(f)cd 
    """
#if __name__ == '__main__':
#    print(pwd+sys.argv[1],type(sys.argv[1]))
#    f=open(pwd+"\y86-code\\"+sys.argv[1],'r').readlines()   
#    run(f)
#    print(result)
