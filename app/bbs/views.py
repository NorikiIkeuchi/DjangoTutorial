from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse('Hello world')
    # render:データとテンプレートを組み合わせてwebページを返すショートカット関数
    return render(request, 'bbs/index.html')