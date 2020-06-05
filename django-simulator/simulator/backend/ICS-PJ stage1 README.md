#ICS-PJ   
##stage1-README
##需要安装Python 3.8.4 ，在Windows上运行   
###运行方式：
#####打开命令行：  
**按住键盘上面的shift键，然后在当前文件夹空白的地方鼠标右击，在弹出的选项卡中可以看到一个在此处打开命令行窗口的选项，输入python run.py，结果将在命令行中显示。**    
样例：
  
	PS D:\Desktop\ICS-PJcd ./ICS-PJ-18307130130  
	PS D:\Desktop\ICS-PJ\ICS-PJ-18307130130python run.py
  
**打开run.py文件，修改以下代码中的run(),有run(f0,f1,f2,~,f19),f0~f19对应文件在const.py中说明**

	if __name__ == '__main__':  
    result = run(f17)   

###文件结构：  
****ICS-PJ-18307130130****  
>****stage****
>>**__init__.py 空文件-建包** 

>>**Fetch.py  流水线取指阶段**
>
>>**Execute.py  流水线执行阶段**
>
>>**Decode.py  流水线译码阶段**
>
>>**MemoryAccess.py  流水线访存阶段**
>
>>**WriteBack.py  流水线写回阶段**
>
>>**PCUpdata.py  流水线更新阶段**

>**y86-code**
>>**测试样例**

>**__init__.py 空文件-建包**

>**run.py  运行测试样例** 
>
>**cpu.py  流水线逻辑控制**
>
>**const.py  常量说明**
>
>**Memory.py  内存类的定义，以及加载、读取函数**
>
>**Pipeline.py  流水线类的定义**
>
>**register.py  寄存器类的定义，以及加载、读取函数**
>
>**Alu.py 数字逻辑运算单元**
>
>**StringOperation.py  字符串操作函数**
>
>**show.txt 部分结果输出**

