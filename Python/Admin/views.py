from django.shortcuts import render

# Create your views here.

def add(request):
    if request.method == "POST":
        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        tot = int(num1) + int(num2)
        return render(request,"Admin/Add.html",{"total":tot})
    else:
        return render(request,"Admin/Add.html")

def larger(request):
    if request.method == "POST":
        num1=int(request.POST.get("num1"))
        num2=int(request.POST.get("num2"))
        num3=int(request.POST.get("num3"))
        # num1=int(num1)
        # num2=int(num2)
        # num3=int(num3)
        if(num1>num2) & (num1>num3):
            return render(request,"Admin/Greaterthan.html",{"result":num1})
        elif(num2>num1) & (num2>num3):
            return render(request,"Admin/Greaterthan.html",{"result":num2})
        else:
            return render(request,"Admin/Greaterthan.html",{"result":num3})
    else:
        return render(request,"Admin/Greaterthan.html") 
def calc(request):
    if request.method =="POST":
        num1=int(request.POST.get("num1"))
        num2=int(request.POST.get("num2"))
        
        btn = request.POST.get("btn")
        if btn == "+":
            total=num1+num2
            return render(request,"Admin/Calculator.html",{"result":total})
        elif btn == "-":
            total=num1-num2
            return render(request,"Admin/Calculator.html",{"result":total})
        elif btn == "*":
            total=num1*num2
            return render(request,"Admin/Calculator.html",{"result":total})
        elif btn == "/":
            total=num1/num2
            return render(request,"Admin/Calculator.html",{"result":total})
        else:
            return render(request,"Admin/Calculator.html")
    else:
        return render(request,"Admin/Calculator.html")
def salary(request):
    if request.method=="POST":
        a=request.POST.get("fname")
        b=request.POST.get("lname")
        name=a+" "+b
        gen=request.POST.get("gender")
        m=request.POST.get("marital")
        if gen =="Male":
            name="Mr "+name
        elif gen=="Female":
            if m=="Single":
                name="Ms "+name
            else:
                name="Mrs "+name
        dep=request.POST.get("dept")
        BS=int(request.POST.get("bs"))
        TA=0
        DA=0
        HRA=0
        LIC=0
        PF=0
        if BS >= 10000:
            TA=0.4*BS
            DA=0.35*BS
            HRA=0.3*BS
            LIC=0.25*BS
            PF=0.2*BS
        elif BS>=5000 & BS<10000:
            TA=0.35*BS
            DA=0.3*BS
            HRA=0.25*BS
            LIC=0.2*BS
            PF=0.15*BS
        elif BS<5000:
            TA=0.3*BS
            DA=0.25*BS
            HRA=0.2*BS
            LIC=0.15*BS
            PF=0.1*BS
        DED=int(LIC+PF)
        NET=BS+TA+DA+HRA-(LIC+PF)
        return render(request,"Admin/Salary.html",{"result2":gen,"result1":name,"result3":m,"result4":dep,"result5":BS,"result6":TA,"result7":DA,"result8":HRA,"result9":LIC,"result10":PF,"result11":DED,"result12":NET})
    else:
        return render(request,"Admin/Salary.html")
    
def district(request):
    if request.method=="POST":
        d=request.POST.get("dist")
        return render(request,"Admin/District.html",{"result":d})
    else:
        return render(request,"Admin/District.html")
    