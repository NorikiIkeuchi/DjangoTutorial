from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse('Hello world')
    context = {
        'message':'Welcome my BBS',
        'players':['勇者','戦士','魔法使い','忍者']
    }

    # render:データとテンプレートを組み合わせてwebページを返すショートカット関数
    return render(request, 'bbs/index.html',context)