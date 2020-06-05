from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.http import HttpResponse,JsonResponse,FileResponse,StreamingHttpResponse,HttpResponseNotFound
from django.template.loader import  get_template
from simulator.backend.run import *
import os
import json
pwd = os.getcwd()
from django.views.decorators.http import require_http_methods

from django.template import Template,Context

from simulator.backend.run import *
# Create your views here.

def main(request):
    return render(request,"main.html")

def load(request):
    datalist=[]
    filename = request.FILES.get("upload_file").name
    index = filename.find(".")
    str = filename[index+1:]
    if str=="yo":
        run(filename);
        # print(filename,"**********")
        with open(pwd+"\simulator\\backend\\y86-code\\"+filename,'r') as f:
            data=f.readlines()
        for item in data:
            if item.startswith("0x"):
                datalist.append(item)
        return render(request,"main.html",{"codedata":datalist})
    else:
        return render(request,"main.html",{"codedata":"0000000000000000"})

def step(request):
    with open('./show.json', 'r') as f:
        data = json.load(f)
    return HttpResponse(json.dumps(data))


def comment(request):
    print("asdfsad")
    request.encoding = 'utf-8'
    with open('./comment.json', 'r') as f:
        data = json.load(f)
    print(data)
    print(type(data))
    return HttpResponse(json.dumps(data))

res={}
cnt = 0
def postcomment(request):
    global cnt
    request.encoding = 'utf-8'
    date = request.POST.get("id")
    time = request.POST.get("time")
    print(time)
    result = {
        "id":date,
        "time": time,
        "acc":"0",
        "ref":"0",
    }
    res[cnt]=result
    cnt+=1
    with open('./comment.json', 'w') as f:
        json.dump(res,f,indent=4)
        f.write("\n")
    return HttpResponse(json.dumps(res))

def add(request):
    request.encoding = 'utf-8'
    content = request.POST.get("con")
    flag = request.POST.get("fla")
    print("****")
    print(flag)
    print(type(content))
    with open('./comment.json', 'r') as f:
        data = json.load(f)
    for key in data.keys():
        item = data[key]
        print("@")
        if item["id"]==content:
            print("$$")
            if flag == '0':
                print("!!!231")
                a = int(item["ref"])
                item["ref"]=str(a+1)
            else:
                print("^^^")
                a = int(item["acc"])
                item["acc"]=str(a+1)
            break
    with open('./comment.json', 'w') as f:
        json.dump(data,f,indent=4)
        f.write("\n")
    return HttpResponse(json.dumps(data))
