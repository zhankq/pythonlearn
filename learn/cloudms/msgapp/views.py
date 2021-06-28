from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
#from django.shortcuts import HttpResponse

# Create your views here.
def msgproc(request):
    datalist = []
    if request.method == "POST":
        userA = request.POST.get("userA",None)
        userB = request.POST.get("userB",None)
        msg = request.POST.get("msg",None)
        time = datetime.now()
        with open("msgdata.txt","a+") as f:
            f.write("{}--{}--{}--{}--\n".format(userB,userA,msg,time.strftime("%Y-%m-%d %H:%M:%S")))
    if request.method == "GET":

        userC = request.GET.get("userC",None)
        #print(type(userC))

        if userC != None:
            with open("msgdata.txt","r") as f:
                cnt = 0
                #print(f)
                for line in f:
                    linedata = line.split('--')
                    if linedata[0] == userC:
                        cnt= cnt+1
                        d = {"userA":linedata[1],"msg":linedata[2],"time":linedata[3]}
                        datalist.append(d)
                    if cnt >= 10:
                        break
        else:
            with open("msgdata.txt","r") as f:
                cnt = 0
                #print(f)
                for line in f:
                    linedata = line.split('--')
                    cnt= cnt+1
                    d = {"userA":linedata[1],"msg":linedata[2],"time":linedata[3]}
                    datalist.append(d)
                    if cnt >= 10:
                        break

    return render(request,"MsgSingleWeb.html", {"data":datalist})

def test(request):
    if request.method == "GET":
        return render(request,"MsgTest.html")
    #    return "good index"

def article(request,year):
    return HttpResponse("this {0}".format(year))

