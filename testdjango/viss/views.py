from django.shortcuts import render
import time
from datetime import datetime

# Create your views here.

def result1(request,result_id):
    dt = datetime.now()
    s=str(dt.microsecond)
    new="reqid-0"+str(result_id)
    #result_id에 따라서 respon값을 달리해서 context변수 전송해주기 
    respon={"action":"get", "requestId":new,"value":"2372","timestamp":s}
    context={"result":respon}
    return render(request,'viss/0130-get-success.html',context)


def RPM(request):
    dt = datetime.now()
    s=str(dt.microsecond)
    data={
            "path":"Vehicle/Drivetrain/InternalCombustionEngine/RPM/",
            "dp":{
                "value":"2372",
                "ts":s
            }
    }

    context={"result":data}
    return render(request,'viss/version2.html',context)


def SPEED(request):
    dt = datetime.now()
    s=str(dt.microsecond)
    data={
            "path":"Vehicle/Speed",
            "dp":{
                "value":"2372",
                "ts":s
            }
    }
    context={"result":data}
    return render(request,'viss/version2.html',context)
