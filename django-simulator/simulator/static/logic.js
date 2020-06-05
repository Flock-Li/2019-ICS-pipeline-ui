var tabs = document.getElementById("tabs").getElementsByTagName("a");
var lists=document.getElementById("list").getElementsByTagName("ul");
var register = document.getElementById("Reg").getElementsByTagName("span");
var Regcontent = document.getElementById("Reg").getElementsByTagName("em");
var memorycon = document.getElementById("Mem").getElementsByTagName("span");
var Memcontent = document.getElementById("Mem").getElementsByTagName("em");


var writeback = document.getElementById("write").getElementsByTagName("span");
var Writeback = document.getElementById("write").getElementsByTagName("em");
var memory = document.getElementById("mem").getElementsByTagName("span");
var Memory = document.getElementById("mem").getElementsByTagName("em");
var execute = document.getElementById("exe").getElementsByTagName("span");
var Execute = document.getElementById("exe").getElementsByTagName("em");
var decode = document.getElementById("dec").getElementsByTagName("span");
var Decode = document.getElementById("dec").getElementsByTagName("em");
var fetch = document.getElementById("fet").getElementsByTagName("span");
var Fetch = document.getElementById("fet").getElementsByTagName("em");

var code = document.getElementById("codelist").getElementsByTagName("p");
var Code = document.getElementById("codelist").getElementsByTagName("span");
console.log(code[1].innerHTML.substring(0,5));
console.log(typeof code[1].innerHTML);

var condition =document.getElementById("status").getElementsByTagName("span");
var Condition =document.getElementById("status").getElementsByTagName("em");
for(var i=0; i<tabs.length;i++){
    tabs[i].onclick = showlist;
}

function showlist()
{
    for(var i=0;i<tabs.length;i++){
        if(tabs[i] === this){
            tabs[i].className = "active";
            lists[i].className = "active";
        }
        else{
            tabs[i].className = "";
            lists[i].className = "";
        }
    }
}
function change() {
    var value = document.getElementById('range').value ;
    document.getElementById('spevalue').innerHTML = value;
}
var cnt=0;
var flag = 0;
var mytime;
function step(){
    var formData = new FormData($("#insertForm")[0]);
    $.ajax({
        url:"/step/",
        type:"GET",
        data:formData,
        contentType: false,
        processData: false ,
        success:function(xhr){      
            data = JSON.parse(xhr);
            if(data[cnt]["condition"]["stat"]=="AOK"){
                cnt++;
                console.log(data[cnt]);
                for(var i=0; i<register.length;i++){
                    var reg = register[i].innerHTML;
                    var value = data[cnt]["register"][reg];
                    Regcontent[i].innerHTML = value;
                }
                for(var i=0; i<memorycon.length;i++){
                    var mem = memorycon[i].innerHTML;
                    var value = data[cnt]["memory"][mem];
                    Memcontent[i].innerHTML = value;
                }
                for(var i=0; i<writeback.length;i++){
                    
                    var text = writeback[i].innerHTML;
                    var value = data[cnt]["W"][text];
                    Writeback[i].innerHTML = value;
                }
                for(var i=0; i<memory.length;i++){
                    var text = memory[i].innerHTML;
                    var value = data[cnt]["M"][text];
                    Memory[i].innerHTML = value;
                }
                for(var i=0; i<execute.length;i++){
                    var text = execute[i].innerHTML;
                    var value = data[cnt]["E"][text];
                    Execute[i].innerHTML = value;
                }
                for(var i=0; i<decode.length;i++){
                    var text = decode[i].innerHTML;
                    var value = data[cnt]["D"][text];
                    Decode[i].innerHTML = value;
                }
                for(var i=0; i<fetch.length;i++){
                    var text = fetch[i].innerHTML;
                    var value = data[cnt]["F"][text];
                    Fetch[i].innerHTML = value;
                }
                for(var i=0; i<condition.length;i++){
                    var text = condition[i].innerHTML;
                    var value = data[cnt]["condition"][text];
                    Condition[i].innerHTML = value;
                }
                var flag= data[cnt]["F"]["f_pc"];
                for(var i=0;i<code.length;i++){
                    var value = code[i].innerHTML.substring(0,5);
                    if(flag == value){
                        Code[i].className="blockactive";
                    }
                    else{
                        Code[i].className="";
                    }
                }                         
            }
            else {
                clearInterval(mytime);
            }
        },
        error:function(xhr){
            console.log("error");          
        }
    }    
    );
}

function start(){
    if(flag==0){
        var spe = document.getElementById("spevalue").innerHTML;
        var speed = 500-spe*15;
        console.log(speed);
        mytime = setInterval(step,speed);
        flag=1;
    }
    else ; 
}

function pause(){
    clearInterval(mytime);
    flag=0;
}
function back(){
    clearInterval(mytime);
    flag=0;
    if(cnt>=2)
        cnt-=2;
    step();
}
function reset(){
    clearInterval(mytime);
    cnt=0;
    flag=0;
    step();
    
}






