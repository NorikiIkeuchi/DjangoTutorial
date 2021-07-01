from django.contrib import admin
from django.urls import include, path

# 全体のルーティングをィングを示す
urlpatterns = [
    # サーバアドレスの後に続くアドレスによってルーディングを変化
    path('hello/', include('bbs.urls')),
    path('bbs/', include('bbs.urls')),
    path('admin/', admin.site.urls),
]
