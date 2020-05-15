from django.shortcuts import render
from app.models import *
from django.db.models import Avg, Max, Min, Sum, Count
import json
from django.http import HttpResponse,JsonResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.
def home(request):
    return render(request,"index.html",{})

def index(request):
    return render(request,"index.html",{})

def logout(request):
    print ("logout_fn")
    if request.session.has_key('uid'):
        print ("session=: deleting ",request.session['uid'])
        del request.session['uid']
        print ("session deleted")
        return render(request,"index.html",{})

def signin(request):
    return render(request,"login.html",{})

def signup(request):
    return render(request,"register.html",{})

def maker_reg(request):
    return render(request,"maker_reg.html",{})

#---------------------------Registration-------------------------------------------

def customer(request):
    print("registration")
    if request.method=="POST":
        a=request.POST.get("user")
        if (a=="individual"):
            b=request.POST.get("name")
            c=request.POST.get("country")
            d=request.POST.get("place")
            e=request.POST.get("gender")
            f=request.POST.get("date")
            g=request.POST.get("phone")
            h=request.POST.get("email")
            i=request.POST.get("uname")
            j=request.POST.get("pass")
            k=request.POST.get("add")
            log=login_tb.objects.filter(user=i)
            if (log.count()>=1):
                return HttpResponse("<script>alert('Username Already exist. Choose another');window.location.href='/signup/';</script>")
            email=user_tb.objects.filter(email=h)
            if (email.count()>=1):
                return HttpResponse("<script>alert('Exisiting email. please login');window.location.href='/signin/';</script>")
            mob=user_tb.objects.filter(phone=g)
            if (mob.count()>=1):
                return HttpResponse("<script>alert('Exisiting mobile number. please login');window.location.href='/signin/';</script>")
            obb=login_tb(user=i,passw=j,usertype=a)
            obb.save()
            obje=login_tb.objects.get(user=i,passw=j)
            u_id=obje.lid
            obj=user_tb(u_lid=u_id,name=b,country=c,place=d,gender=e,date=f,phone=g,
                        email=h,username=i,passw=j,add=k)
            obj.save()
            return HttpResponse("<script>alert('Registration Successfull');window.location.href='/index/';</script>")
        if (a=="pharmacy"):
            z=request.POST.get("pname")
            y=request.POST.get("country")
            x=request.POST.get("place")
            w=request.POST.get("cname")
            v=request.POST.get("phone")
            u=request.POST.get("email")
            t=request.POST.get("uname")
            s=request.POST.get("pass")
            log=login_tb.objects.filter(user=t)
            if (log.count()>=1):
                return HttpResponse("<script>alert('Username Already exist. Choose another');window.location.href='/signup/';</script>")
            email=phar_tb.objects.filter(email=u)
            if (email.count()>=1):
                return HttpResponse("<script>alert('Exisiting email. please login');window.location.href='/signin/';</script>")
            mob=phar_tb.objects.filter(phone=v)
            if (mob.count()>=1):
                return HttpResponse("<script>alert('Exisiting mobile number. please login');window.location.href='/signin/';</script>")
            obb=login_tb(user=t,passw=s,usertype=a)
            obb.save()
            obje=login_tb.objects.get(user=t,passw=s)
            u_id=obje.lid
            obj=phar_tb(p_lid=u_id,name=z,country=y,place=x,contact=w,phone=v,
                        email=u,username=t,passw=s)
            obj.save()
            return HttpResponse("<script>alert('Registration Successfull');window.location.href='/index/';</script>")
        else:
            return HttpResponse("<script>alert('error');window.location.href='/index/';</script>")
    else:
        return HttpResponse("<script>alert('error');window.location.href='/index/';</script>")
def reg_maker(request):
    print("maker reg")
    if request.method=="POST":
        b=request.POST.get("name")
        c=request.POST.get("country")
        d=request.POST.get("place")
        e=request.POST.get("number")
        f=request.POST.get("cname")
        g=request.POST.get("phone")
        h=request.POST.get("email")
        i=request.POST.get("uname")
        j=request.POST.get("pass")
        log=login_tb.objects.filter(user=i)
        if (log.count()>=1):
            return HttpResponse("<script>alert('Username Already exist. Choose another');window.location.href='/signup/';</script>")
        email=maker_tb.objects.filter(email=h)
        if (email.count()>=1):
            return HttpResponse("<script>alert('Exisiting email. please login');window.location.href='/signin/';</script>")
        mob=maker_tb.objects.filter(phone=g)
        if (mob.count()>=1):
            return HttpResponse("<script>alert('Exisiting mobile number. please login');window.location.href='/signin/';</script>")
        obb=login_tb(user=i,passw=j,usertype="maker")
        obb.save()
        obje=login_tb.objects.get(user=i,passw=j)
        u_id=obje.lid
        obj=maker_tb(p_lid=u_id,name=b,country=c,place=d,licence=e,contact=f,phone=g,
                    email=h,username=i,passw=j)
        obj.save()
        return HttpResponse("<script>alert('Registration Successfull');window.location.href='/index/';</script>")
    else:
        return HttpResponse("<script>alert('error');window.location.href='/index/';</script>")
def ck_login(request):
    print("login")
    count=0
    if request.method=="POST":
        a=request.POST.get("uname")
        b=request.POST.get("passw")
        if("admin"==a and "admin"==b):
            request.session['uid']=120
            data=user_tb.objects.all()
            return render(request,"admin/admin.html",{"data":data})
        log=login_tb.objects.filter(user=a,passw=b)
        count=log.count()
        if(count==0):
            return HttpResponse("<script>alert('Invalid user. Enter correct username and password');window.location.href='/signin/';</script>")
        else:
            for i in log:
                typ=i.usertype
                llid=i.lid
        print("type",typ,"lid",llid)
        if(count==1 and typ=="individual"):
            user_dt=user_tb.objects.get(u_lid=llid)
            request.session['uid']=user_dt.u_lid
            print ("session=: created ",request.session['uid'])
            if request.session.has_key('uid'):
                user=user_tb.objects.get(username=a,passw=b)
                print(request.session['uid'])
                data=stock.objects.all()
                return render(request,"user/user_home.html",{"user":user,"data":data})
        if(count==1 and typ=="maker"):
            user_dt=maker_tb.objects.get(p_lid=llid)
            request.session['uid']=user_dt.p_lid
            print ("session=: created ",request.session['uid'])
            if request.session.has_key('uid'):
                maker=maker_tb.objects.get(username=a,passw=b)
                print(request.session['uid'])
                return render(request,"maker/maker_home.html",{"maker":maker})

def u_home(request):
    if request.session.has_key('uid'):
        log=login_tb.objects.get(lid=request.session['uid'])
        a=log.user
        b=log.passw
        user=user_tb.objects.get(username=a,passw=b)
        data=stock.objects.all()
        print(request.session['uid'])
        return render(request,"user/user_home.html",{"user":user,"data":data})

def prof_user(request):
    if request.session.has_key('uid'):
        log=login_tb.objects.get(lid=request.session['uid'])
        a=log.user
        b=log.passw
        user=user_tb.objects.get(username=a,passw=b)
        print(request.session['uid'])
        return render(request,"user/edit_prof.html",{"user":user})

def update_prof(request):
    if request.session.has_key('uid'):
        a=request.POST.get("uname")
        b=request.POST.get("pass")
        print(request.session['uid'])
        print(a,b)
        log=login_tb.objects.filter(user=a)
        if(log.count()>=1):
            return HttpResponse("<script>alert('Username already taken. Choose another');window.location.href='/prof_user/';</script>")
        obj=user_tb.objects.get(u_lid=request.session['uid'])
        obj.username=a
        obj.passw=b
        obj.save()
        obje=login_tb.objects.get(lid=request.session['uid'])
        obje.user=a
        obje.passw=b
        obje.save()
        return HttpResponse("<script>alert('username and password successfully updated');window.location.href='/u_home/';</script>")
    return HttpResponse("<script>alert('please login');window.location.href='/signin/';</script>")

def orders(request):
    if request.session.has_key('uid'):
        a=request.POST.get("count")
        b=request.POST.get("rate")
        c=request.POST.get("typ")
        d=request.POST.get("comname")
        print(d)
        obj=maker_tb.objects.get(name=d)
        obb=user_tb.objects.get(u_lid=request.session['uid'])
        ob=order(o_lid=request.session['uid'],name=d,typ=c,status="Not Accepted",rate=b,track="N/A",address=obb.add)
        ob.save()
        return HttpResponse("<script>alert('cart added');window.location.href='/u_home/';</script>")

def track(request):
    if request.session.has_key('uid'):
        obj=user_tb.objects.get(u_lid=request.session['uid'])
        a=obj.u_lid
        data=order.objects.filter(o_lid=a)
        return render(request,"user/orders.html",{"data":data})

#----------------------------------------maker--------------------------------------------------------
def prd_home(request):
    if request.session.has_key('uid'):
        log=login_tb.objects.get(lid=request.session['uid'])
        a=log.user
        b=log.passw
        maker=maker_tb.objects.get(username=a,passw=b)
        print(request.session['uid'])
        return render(request,"maker/maker_home.html",{"maker":maker})

def mkr_prf(request):
    if request.session.has_key('uid'):
        log=login_tb.objects.get(lid=request.session['uid'])
        a=log.user
        b=log.passw
        maker=maker_tb.objects.get(username=a,passw=b)
        print(request.session['uid'])
        return render(request,"maker/edit_prof.html",{"maker":maker}) 

def ipmkr_prof(request):
    if request.session.has_key('uid'):
        a=request.POST.get("uname")
        b=request.POST.get("pass")
        c=request.POST.get("cname")
        print(request.session['uid'])
        print(a,b,c)
        log=login_tb.objects.filter(user=a)
        if(log.count()>=1):
            return HttpResponse("<script>alert('Username already taken. Choose another');window.location.href='/mkr_prf/';</script>")
        obj=maker_tb.objects.get(p_lid=request.session['uid'])
        obj.username=a
        obj.passw=b
        obj.contact=c
        obj.save()
        obje=login_tb.objects.get(lid=request.session['uid'])
        obje.user=a
        obje.passw=b
        obje.save()
        return HttpResponse("<script>alert('username and password successfully updated');window.location.href='/prd_home/';</script>")
    return HttpResponse("<script>alert('please login');window.location.href='/signin/';</script>")

def vw_stock(request):
    if request.session.has_key('uid'):
        z=request.session['uid']
        obj=login_tb.objects.filter(lid=z)
        for i in obj:
            typ=i.usertype
        print(typ)
        if request.session.has_key('uid') and typ=="maker":
            ob=maker_tb.objects.get(p_lid=z)
            print("ob",ob)
            aa=ob.name
            print("aa",aa)
            data=stock.objects.filter(name=aa)
            print("data",data.count())
            return render(request,"maker/stock_vw.html",{"data":data})
        return HttpResponse("<script>alert('Please login');window.location.href='/signin/';</script>")

def ad_stock(request):
    if request.session.has_key('uid'):
        obj=maker_tb.objects.get(p_lid=request.session['uid'])
        return render(request,"maker/stock.html",{"maker":obj})
        
def lv_stock(request):
    if request.session.has_key('uid'):
        a=request.POST.get("name")
        b=request.POST.get("country")
        c=request.POST.get("code")
        d=request.POST.get("add")
        e=request.POST.get("typ")
        f=request.POST.get("rate")
        i=request.POST.get("stock")
        obj=stock(s_lid=request.session['uid'],stock=i,name=a,country=b,code=c,des=d,typ=e,rate=f)
        obj.save()
        return HttpResponse("<script>alert('Stock successfully updated');window.location.href='/prd_home/';</script>")
        
    
            
    
