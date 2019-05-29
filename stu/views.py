from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from stu.models import registerstu


def index_views(request):
    if request.method == 'GET':
        return  render(request,'register.html')
    else:
        sname=request.POST.get('sname','')
        sid=request.POST.get('sid','')
        cname=request.POST.get('clsname','')
        coursename=request.POST.getlist('coursename',[])

        flag = registerstu(sname,sid,cname,*coursename)
        if flag:
            return HttpResponse('提交成功')
        else:
            return HttpResponse('提交失败')


