from django.urls import path
from . import views

urlpatterns = [
    # app/urls.pyから読み込まれ，その後のアドレスが空欄の場合views.pyのindex関数を呼び出す
    path('', views.index, name='index'),
]